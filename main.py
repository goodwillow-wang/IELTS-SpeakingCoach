import sys, os, time, re
sys.path.insert(0, os.path.dirname(__file__))
from PyQt5.QtWidgets import (QDialog,    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,    QPushButton, QLabel, QTextEdit, QComboBox, QGroupBox,    QProgressBar, QMessageBox, QListWidget, QListWidgetItem, QMenu,)
from PyQt5.QtCore import Qt, QTimer, QThread, pyqtSignal
from PyQt5.QtGui import QFont
from data.question_bank import IELTS_SPEAKING_QUESTIONS, get_test, add_custom_test_set, delete_custom_test_set, get_custom_test_names
from engine.scorer import IELTSScorer
from engine.speech_engine import SpeechEngine
from engine.session_manager import SessionManager
from engine.sample_answers import generate_sample_answers, save_as_docx
from engine.correction_report import generate_correction_report, llm_evaluate_response

class ListenThread(QThread):
    result_ready = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.engine = SpeechEngine()
    def run(self):
        r = self.engine.listen_dictation(timeout=60)
        self.result_ready.emit(r)

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.scorer = IELTSScorer()
        self.session_mgr = SessionManager()
        self.book = None
        self.test = None
        self.part = None
        self.qidx = 0
        self.qdata = None
        self.history = []
        self.attempts = 0
        self.streak = 0
        self.eval = None
        self.active = False
        self.listen_thread = None
        self.is_rec = False
        self.current_topic = ""
        self.current_part_num = 1
        self.last_user_response = ""
        self.last_question_info = None
        self.init_ui()
        self.load_sessions()
    def init_ui(self):
        self.setWindowTitle("IELTS Speaking Coach")
        self.setMinimumSize(1450, 950)
        self.resize(1450, 950)
        self.setStyleSheet("""
            QMainWindow { background: #f0f2f5; }
            QGroupBox { font-weight: bold; border: 2px solid #ddd; border-radius: 8px; margin-top: 12px; padding: 15px; background: white; }
            QGroupBox::title { subcontrol-origin: margin; padding: 3px 10px; color: #1a73e8; }
            QPushButton { padding: 8px 16px; border-radius: 6px; border: 1px solid #ccc; font-size: 16pt; min-height: 48px; }
            QPushButton:hover { border-color: #1a73e8; }
            QPushButton#p { background: #1a73e8; color: white; border: none; font-weight: bold; padding: 10px 24px; }
            QPushButton#p:hover { background: #1557b0; }
            QPushButton#p:disabled { background: #aaa; }
            QPushButton#d { background: #d93025; color: white; border: none; }
            QPushButton#d:hover { background: #b3261e; }
            QPushButton#s { background: #188038; color: white; border: none; }
            QPushButton#s:hover { background: #146c2e; }
            QTextEdit, QComboBox { border: 1px solid #ddd; border-radius: 6px; padding: 8px; font-size: 16pt; }
            QProgressBar { border: 1px solid #ddd; border-radius: 6px; text-align: center; height: 22px; }
            QProgressBar::chunk { border-radius: 5px; background: #1a73e8; }
            QListWidget { border: 1px solid #ddd; border-radius: 6px; }
        """)
        
        c = QWidget()
        self.setCentralWidget(c)
        m = QVBoxLayout(c)
        m.setContentsMargins(15, 10, 15, 10)
        
        t = QHBoxLayout()
        ti = QLabel("IELTS Speaking Coach")
        ti.setStyleSheet("font-size: 28pt; font-weight: bold; color: #1a73e8;")
        t.addWidget(ti)
        t.addStretch()
        self.sl = QLabel("Ready")
        self.sl.setStyleSheet("color: #666;")
        t.addWidget(self.sl)
        m.addLayout(t)
        
        cx = QHBoxLayout()
        
        # LEFT
        lp = QWidget()
        lp.setMaximumWidth(260)
        ll = QVBoxLayout(lp)
        ll.setContentsMargins(0,0,0,0)
        
        sg = QGroupBox("Select Test")
        sl = QVBoxLayout(sg)
        sl.addWidget(QLabel("Book:"))
        self.bc = QComboBox()
        for b in IELTS_SPEAKING_QUESTIONS: self.bc.addItem(b)
        self.bc.currentTextChanged.connect(self.on_book)
        sl.addWidget(self.bc)
        sl.addWidget(QLabel("Test:"))
        self.tc = QComboBox()
        if IELTS_SPEAKING_QUESTIONS:
            fb = list(IELTS_SPEAKING_QUESTIONS.keys())[0]
            for t in IELTS_SPEAKING_QUESTIONS[fb]:
                self.tc.addItem(t)
        sl.addWidget(self.tc)
        self.part_container = QWidget()
        pcl = QVBoxLayout(self.part_container)
        pcl.setContentsMargins(0,0,0,0)
        pcl.addWidget(QLabel("Part:"))
        self.pc = QComboBox()
        self.pc.addItems(["Part 1 Interview", "Part 2 Long Turn", "Part 3 Discussion"])
        pcl.addWidget(self.pc)
        sl.addWidget(self.part_container)
        self.sb = QPushButton("Start Practice")
        self.sb.setObjectName("p")
        self.sb.clicked.connect(self.start)
        sl.addWidget(self.sb)
        self.rb = QPushButton("Resume Session")
        self.rb.clicked.connect(self.resume)
        self.rb.setEnabled(False)
        sl.addWidget(self.rb)
        ll.addWidget(sg)
        self.mcb = QPushButton("Manage\nCustom Questions")
        self.mcb.setObjectName("p")
        self.mcb.clicked.connect(self.manage_custom)
        self.mcb.setVisible(False)
        ll.addWidget(self.mcb)
        
        ig = QGroupBox("Session Info")
        self.il = QLabel("No active session")
        self.il.setWordWrap(True)
        QVBoxLayout(ig).addWidget(self.il)
        ll.addWidget(ig)
        ll.addStretch()
        cx.addWidget(lp)
        
        # CENTER
        cp = QWidget()
        cl = QVBoxLayout(cp)
        cl.setContentsMargins(0,0,0,0)
        
        qg = QGroupBox("Question")
        self.qa = QTextEdit()
        self.qa.setReadOnly(True)
        self.qa.setMaximumHeight(250)
        self.qa.setStyleSheet("font-size: 16pt; background: #f8f9fa; border: 2px solid #1a73e8;")
        QVBoxLayout(qg).addWidget(self.qa)
        cl.addWidget(qg)
        
        # Question navigation (for custom questions with multiple items)
        self.nav_row = QWidget()
        nrl = QHBoxLayout(self.nav_row)
        nrl.setContentsMargins(0,0,0,0)
        self.prev_q_btn = QPushButton("< Prev")
        self.prev_q_btn.clicked.connect(lambda: self.navigate_q(-1))
        nrl.addWidget(self.prev_q_btn)
        self.q_pos_label = QLabel("Q 0/0")
        self.q_pos_label.setAlignment(Qt.AlignCenter)
        self.q_pos_label.setStyleSheet("font-size: 14pt; font-weight: bold;")
        nrl.addWidget(self.q_pos_label)
        self.next_q_btn = QPushButton("Next >")
        self.next_q_btn.clicked.connect(lambda: self.navigate_q(1))
        nrl.addWidget(self.next_q_btn)
        self.nav_row.setVisible(False)
        cl.addWidget(self.nav_row)
        
        rg = QGroupBox("Your Response")
        self.rt = QTextEdit()
        self.rt.setPlaceholderText("Type or speak your answer...")
        self.rt.setMinimumHeight(200)
        rl = QVBoxLayout(rg)
        rl.addWidget(self.rt)
        rcl = QHBoxLayout()
        self.rec = QPushButton("Record")
        self.rec.setObjectName("p")
        self.rec.clicked.connect(self.toggle_rec)
        rcl.addWidget(self.rec)
        self.sub = QPushButton("Submit & Evaluate")
        self.sub.setObjectName("s")
        self.sub.clicked.connect(self.submit)
        self.sub.setEnabled(False)
        rcl.addWidget(self.sub)
        clb = QPushButton("Clear")
        clb.clicked.connect(lambda: self.rt.clear())
        rcl.addWidget(clb)
        self.seb = QPushButton("Save & Exit")
        self.seb.setObjectName("d")
        self.seb.clicked.connect(self.save_exit)
        self.seb.setEnabled(False)
        rcl.addWidget(self.seb)
        rl.addLayout(rcl)
        cl.addWidget(rg)
        
        tml = QHBoxLayout()
        self.tml = QLabel("Timer: Ready")
        tml.addWidget(self.tml)
        self.pb = QProgressBar()
        tml.addWidget(self.pb)
        cl.addLayout(tml)
        cx.addWidget(cp, 1)
        
        # RIGHT
        rp = QWidget()
        rp.setMaximumWidth(360)
        rl2 = QVBoxLayout(rp)
        rl2.setContentsMargins(0,0,0,0)
        
        fg = QGroupBox("Feedback & Scores")
        self.fa = QTextEdit()
        self.fa.setReadOnly(True)
        self.fa.setMinimumHeight(400)
        QVBoxLayout(fg).addWidget(self.fa)
        rl2.addWidget(fg, 1)
        
        bl = QHBoxLayout()
        self.bdl = QLabel("Band: --")
        self.bdl.setStyleSheet("font-size: 28pt; font-weight: bold; color: #1a73e8;")
        bl.addWidget(self.bdl)
        self.psl = QLabel("")
        self.psl.setStyleSheet("font-size: 18pt; font-weight: bold;")
        bl.addWidget(self.psl)
        bl.addStretch()
        rl2.addLayout(bl)
        
        self.sample_btn = QPushButton("[Ref] View Sample Answer")
        self.sample_btn.setObjectName("p")
        self.sample_btn.clicked.connect(self.show_sample_dialog)
        self.sample_btn.setEnabled(False)
        self.sample_btn.setVisible(False)
        rl2.addWidget(self.sample_btn)
        self.correction_btn = QPushButton("[PDF] Correction Report")
        self.correction_btn.setObjectName("s")
        self.correction_btn.clicked.connect(self.show_correction_report)
        self.correction_btn.setEnabled(False)
        self.correction_btn.setVisible(False)
        rl2.addWidget(self.correction_btn)
        
        hg = QGroupBox("Conversation History")
        self.hlw = QListWidget()
        self.hlw.itemClicked.connect(self.on_history_click)
        self.hlw.setContextMenuPolicy(Qt.CustomContextMenu)
        self.hlw.customContextMenuRequested.connect(self.on_history_context_menu)
        self.hlw.setMaximumHeight(200)
        QVBoxLayout(hg).addWidget(self.hlw)
        rl2.addWidget(hg)
        cx.addWidget(rp)
        
        m.addLayout(cx, 1)
        
        self.bs = QLabel("Tip: Select a test and click Start Practice to begin")
        self.bs.setStyleSheet("color: #666;")
        m.addWidget(self.bs)
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.tick)
        self.rec_start = None
        self.elapsed = 0
        self.max_secs = 60
    
    def on_book(self, book):
        self.tc.clear()
        if book in IELTS_SPEAKING_QUESTIONS:
            for t in IELTS_SPEAKING_QUESTIONS[book]:
                self.tc.addItem(t)
        is_custom = (book == "Custom Questions")
        self.part_container.setVisible(not is_custom)
        self.mcb.setVisible(is_custom)
    
    def load_sessions(self):
        ss = self.session_mgr.get_all_sessions()
        self.rb.setEnabled(len(ss) > 0)
        if ss: self.rb.setText(f"Resume Session ({len(ss)} available)")
    
    def start(self):
        book = self.bc.currentText()
        test = self.tc.currentText()
        if not book or not test:
            QMessageBox.warning(self, "Error", "Please select book and test")
            return
        td = get_test(book, test)
        if not td:
            QMessageBox.warning(self, "Error", "Test data not found")
            return
        if book == "Custom Questions":
            if "questions" not in td or not td["questions"]:
                QMessageBox.warning(self, "Error", "No questions in this test set.")
                return
            exist = self.session_mgr.load_session(book, test)
            if exist:
                r = QMessageBox.question(self, "Session Found", "Resume existing session?", QMessageBox.Yes | QMessageBox.No)
                if r == QMessageBox.Yes:
                    self.resume_from(exist)
                    return
            self.book = book; self.test = test; self.part = "Custom"
            self.hlw.clear(); self.qidx = 0; self.history = []; self.attempts = 0; self.streak = 0
            self.active = True; self.qdata = td
            self.seb.setEnabled(True); self.rb.setEnabled(False)
            self.show_q(); self.upd_info(); self.set_status("Started")
            return
        pi = self.pc.currentIndex()
        pns = ["Part 1 - Introduction & Interview", "Part 2 - Individual Long Turn", "Part 3 - Discussion"]
        pn = pns[pi]
        if pn not in td:
            QMessageBox.warning(self, "Error", "Test data not found")
            return
        
        exist = self.session_mgr.load_session(book, test)
        if exist and exist.get("part") == pn:
            r = QMessageBox.question(self, "Session Found", "Resume existing session?", QMessageBox.Yes | QMessageBox.No)
            if r == QMessageBox.Yes:
                self.resume_from(exist)
                return
        
        self.book = book; self.test = test; self.part = pn
        self.hlw.clear(); self.qidx = 0; self.history = []; self.attempts = 0; self.streak = 0
        self.active = True; self.qdata = td[pn]
        self.seb.setEnabled(True); self.rb.setEnabled(False)
        self.show_q(); self.upd_info(); self.set_status("Started")
    
    def show_q(self):
        d = self.qdata
        if not d: return
        pn = self.part
        self.sample_btn.setEnabled(False)
        self.sample_btn.setVisible(False)
        self.correction_btn.setEnabled(False)
        self.correction_btn.setVisible(False)
        if "questions" in d and "topic" not in d and "cue_card" not in d:
            qs = d["questions"]
            if self.qidx >= len(qs):
                self.qa.setText("All questions completed! Practice another test.")
                self.rt.clear(); self.fa.clear()
                return
            q = qs[self.qidx]
            qt = q.get("type", "P2")
            if qt == "P2":
                txt = f"[Question {self.qidx+1}/{len(qs)}]\n\n{q['cue_card']}\n"
                for ip, p in enumerate(q.get("prompts",[]), 1):
                    txt += f"  {ip}. {p}\n"
                txt += "\n[Speak for 1-2 minutes]"
                self.max_secs = 120
                self.current_topic = q['cue_card']
                self.current_part_num = 2
            else:
                txt = f"[Question {self.qidx+1}/{len(qs)}]\n\n{q.get('question','')}"
                if qt == "P1":
                    self.max_secs = 30; self.current_part_num = 1
                else:
                    self.max_secs = 45; self.current_part_num = 3
                self.current_topic = q.get('question','')[:60]
            self.qa.setText(txt)
            self.rt.clear(); self.fa.clear()
            self.bdl.setText("Band: --"); self.psl.setText("")
            self.sub.setEnabled(True)
            self.attempts = 0; self.eval = None
            self.elapsed = 0; self.rec_start = None
            self.tml.setText("Timer: Ready"); self.pb.setValue(0)
            self.timer.stop()
            # Show nav for custom flat format
            if "questions" in d and "topic" not in d and "cue_card" not in d:
                nq = len(d["questions"])
                self.nav_row.setVisible(nq > 1)
                self.q_pos_label.setText(f"Q {self.qidx+1} / {nq}")
                self.prev_q_btn.setEnabled(self.qidx > 0)
                self.next_q_btn.setEnabled(self.qidx < nq - 1)
            return
        
        if pn == "Part 1 - Introduction & Interview":
            qs = d.get("questions", [])
            if self.qidx < len(qs):
                self.qa.setText(f"[Part 1 Interview]\nTopic: {d.get('topic','')}\n\nQ{self.qidx+1}/{len(qs)}:\n{qs[self.qidx]}")
                self.max_secs = 30
                self.current_topic = d.get("topic","")
                self.current_part_num = 1
        elif pn == "Part 2 - Individual Long Turn":
            cue_cards = d.get("cue_cards", None)
            if cue_cards and isinstance(cue_cards, list) and self.qidx < len(cue_cards):
                card = cue_cards[self.qidx]
                txt = f"[Part 2 Long Turn - Cue Card {self.qidx+1}/{len(cue_cards)}]\n\n{card['cue_card']}\n"
                for i, p in enumerate(card.get("prompts",[]), 1): txt += f"  {i}. {p}\n"
                txt += "\n[Speak for 1-2 minutes]"
                self.current_topic = card['cue_card']
            else:
                txt = f"[Part 2 Long Turn]\n\n{d.get('cue_card','')}\n"
                for i, p in enumerate(d.get("prompts",[]), 1): txt += f"  {i}. {p}\n"
                txt += "\n[Speak for 1-2 minutes]"
                self.current_topic = d.get("cue_card","")
            self.qa.setText(txt); self.max_secs = 120
            self.current_part_num = 2
        else:
            qs = d.get("questions", [])
            if self.qidx < len(qs):
                self.qa.setText(f"[Part 3 Discussion]\nTopic: {d.get('topic','')}\n\nQ{self.qidx+1}/{len(qs)}:\n{qs[self.qidx]}")
                self.max_secs = 45
                self.current_topic = d.get("topic","")
                self.current_part_num = 3
        
        self.nav_row.setVisible(False)
        self.rt.clear(); self.fa.clear()
        self.bdl.setText("Band: --"); self.psl.setText("")
        self.sub.setEnabled(True)
        self.attempts = 0; self.eval = None
        self.elapsed = 0; self.rec_start = None
        self.tml.setText("Timer: Ready"); self.pb.setValue(0)
        self.timer.stop()
    
    def navigate_q(self, delta):
        if not self.qdata or "questions" not in self.qdata:
            return
        qs = self.qdata["questions"]
        new_idx = self.qidx + delta
        if new_idx < 0 or new_idx >= len(qs):
            return
        self.qidx = new_idx
        self.show_q()

    def toggle_rec(self):
        if not self.is_rec:
            self.is_rec = True
            self.rec.setText("Stop")
            self.rec.setObjectName("d")
            self.rec_start = time.time()
            self.timer.start(1000)
            self.listen_thread = ListenThread()
            self.listen_thread.result_ready.connect(self.on_rec)
            self.listen_thread.start()
        else:
            self.stop_rec()
    
    def stop_rec(self):
        self.is_rec = False
        self.rec.setText("Record")
        self.rec.setObjectName("p")
        self.timer.stop()
        if self.listen_thread:
            self.listen_thread.engine.stop_listening()
    
    def on_rec(self, result):
        self.is_rec = False
        self.rec.setText("Record")
        self.rec.setObjectName("p")
        self.timer.stop()
        if result and not result.startswith("[ERROR"):
            cur = self.rt.toPlainText()
            if cur.strip():
                self.rt.setText(cur + "\n" + result)
            else:
                self.rt.setText(result)
    
    def submit(self):
        if self.is_rec:
            self.stop_rec()
        text = self.rt.toPlainText().strip()
        if not text:
            QMessageBox.warning(self, "Empty", "Please provide a response")
            return
        self.attempts += 1
        d = self.qdata
        pi = 1
        qi = None
        if "questions" in d and "topic" not in d and "cue_card" not in d:
            q = d["questions"][self.qidx]
            qt = q.get("type", "P2")
            pi = int(qt[1]) if len(qt) >= 2 else 2
            qi = q
        elif self.part == "Part 2 - Individual Long Turn":
            pi = 2
            cue_cards = d.get("cue_cards", None)
            if cue_cards and isinstance(cue_cards, list) and self.qidx < len(cue_cards):
                qi = cue_cards[self.qidx]
            else:
                qi = d
        else:
            pi = self.pc.currentIndex() + 1 if hasattr(self, 'pc') else 1
            qs = d.get("questions", [])
            qi = [qs[self.qidx]] if self.qidx < len(qs) else qs
        
        # Try LLM-based evaluation first
        self.fa.setText("Analyzing with AI examiner...")
        self.bs.setText("AI analyzing your response...")
        self.bs.repaint()
        import time as _t
        _t.sleep(0.1)  # Allow UI update
        
        from engine.correction_report import llm_evaluate_response
        llm_ev, llm_err = llm_evaluate_response(pi, qi, text, self.current_topic)
        
        if llm_ev and not llm_err:
            ev = llm_ev
            self.eval = llm_ev
            self.fa.setText(llm_ev.get("feedback_text", ""))
        else:
            # Fallback to local scorer
            self.bs.setText("AI analysis unavailable, using local evaluation...")
            ev = self.scorer.evaluate_full_response(text, qi, pi)
            self.eval = ev
            self.fa.setText(self.scorer.generate_feedback(ev))
        
        band = ev.get("overall_band", 0)
        
        band = ev["overall_band"]
        self.bdl.setText(f"Band: {band}")
        
        meets_dur = ev.get("meets_duration_requirement", True)
        if band >= 7.0 and meets_dur:
            self.psl.setText("PASS - Band 7 Achieved!")
            self.psl.setStyleSheet("color: green; font-weight: bold;")
            self.streak += 1
        else:
            reasons = []
            if band < 7.0: reasons.append(f"Band {band} < 7.0")
            if not meets_dur: reasons.append("Too short")
            self.psl.setText("NEED IMPROVEMENT: " + "; ".join(reasons))
            self.psl.setStyleSheet("color: red; font-weight: bold;")
            self.streak = 0
        
        self.history.append({"q":self.qidx, "a":self.attempts, "band":band, "pass":band>=7.0, "response":text, "feedback":self.fa.toPlainText(), "question":self.qa.toPlainText()})
        icon = "+" if band >= 7 else "-"
        self.hlw.addItem(f"Q{self.qidx+1} A{self.attempts} Band {band} {icon}")
        self.hlw.scrollToBottom()
        self.sub.setEnabled(False)
        self.auto_save(); self.upd_info()
        self.last_user_response = text
        self.last_question_info = qi
        self.sample_btn.setEnabled(True)
        self.sample_btn.setVisible(True)
        self.correction_btn.setEnabled(True)
        self.correction_btn.setVisible(True)
    
    def on_history_click(self, item):
        row = self.hlw.row(item)
        if row < 0 or row >= len(self.history):
            return
        entry = self.history[row]
        if entry.get("question"):
            self.qa.setText(entry["question"])
        if entry.get("response"):
            self.rt.setText(entry["response"])
        else:
            self.rt.clear()
        if entry.get("feedback"):
            self.fa.setText(entry["feedback"])
        else:
            self.fa.clear()
        band = entry.get("band", 0)
        self.bdl.setText(f"Band: {band}")
        if entry.get("pass"):
            self.psl.setText("PASS")
            self.psl.setStyleSheet("color: green; font-weight: bold;")
        else:
            self.psl.setText(f"Band {band}")
            self.psl.setStyleSheet("color: red; font-weight: bold;")
        self.sub.setEnabled(True)
        self.qidx = entry.get("q", self.qidx)

    def on_history_context_menu(self, pos):
        """Right-click context menu for conversation history."""
        item = self.hlw.itemAt(pos)
        if not item:
            return
        row = self.hlw.row(item)
        menu = QMenu()
        delete_action = menu.addAction("Delete")
        action = menu.exec_(self.hlw.mapToGlobal(pos))
        if action == delete_action:
            reply = QMessageBox.question(self, "Confirm Delete",
                "Delete this conversation record?\nThis cannot be undone.",
                QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.hlw.takeItem(row)
                if row < len(self.history):
                    del self.history[row]

    def show_sample_dialog(self):
        from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QTextEdit
        from PyQt5.QtCore import Qt
        import datetime
        
        samples = generate_sample_answers(
            self.current_part_num, self.last_question_info,
            self.last_user_response, self.current_topic
        )
        if not samples or (samples[0] and samples[0].startswith("[")):
            QMessageBox.information(self, "Info", "Sample answers not available.")
            return
        
        dlg = QDialog(self)
        dlg.setWindowTitle("Sample Reference Answers - Band 7+")
        dlg.setMinimumSize(650, 550)
        layout = QVBoxLayout(dlg)
        
        ta = QTextEdit()
        ta.setReadOnly(True)
        ta.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)
        ta.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        ta.setStyleSheet("font-size: 14px; padding: 10px; background: #fafafa;")
        
        content = ""
        for i, sample in enumerate(samples, 1):
            content += "== Sample Answer " + str(i) + " ==\n\n"
            for para in sample.split("\n\n"):
                content += para.strip() + "\n\n"
            content += "-" * 40 + "\n\n"
        ta.setText(content.strip())
        layout.addWidget(ta)
        
        btn_layout = QHBoxLayout()
        save_btn = QPushButton("Save && Close")
        save_btn.setObjectName("s")
        close_btn = QPushButton("Close")
        btn_layout.addStretch()
        btn_layout.addWidget(save_btn)
        btn_layout.addWidget(close_btn)
        layout.addLayout(btn_layout)
        
        def on_save():
            ref_dir = os.path.join(os.path.dirname(__file__), "references")
            os.makedirs(ref_dir, exist_ok=True)
            ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            sc = str(self.book).replace(" ", "_") if self.book else "Unknown"
            st = str(self.test).replace(" ", "_") if self.test else "Unknown"
            sp = str(self.part).replace(" ", "_").replace("&", "and") if self.part else "Unknown"
            fname = sc + "_" + st + "_" + sp + "_Q" + str(self.qidx+1) + "_" + ts + ".docx"
            filepath = os.path.join(ref_dir, fname)
            try:
                save_as_docx(samples, filepath)
                QMessageBox.information(dlg, "Saved", "Saved to:\n" + filepath)
                dlg.accept()
            except Exception as ex:
                QMessageBox.warning(dlg, "Error", "Save failed:\n" + str(ex))
        
        def on_close():
            dlg.reject()
        
        save_btn.clicked.connect(on_save)
        close_btn.clicked.connect(on_close)
        dlg.exec_()
    
    def show_correction_report(self):
        """Generate and open the detailed PDF correction report."""
        if not self.eval:
            QMessageBox.information(self, "Info", "No evaluation data. Submit a response first.")
            return
        if not self.last_user_response:
            QMessageBox.information(self, "Info", "No response to evaluate.")
            return
        try:
            filepath = generate_correction_report(
                self.current_part_num,
                self.last_question_info,
                self.last_user_response,
                book=self.book or "IELTS",
                test=self.test or "Practice",
                qidx=self.qidx,
                topic=self.current_topic
            )
            import os as _os
            try:
                _os.startfile(filepath)
            except Exception:
                QMessageBox.information(self, "Saved", "Correction report saved to:\n" + filepath)
        except Exception as ex:
            QMessageBox.warning(self, "Error", "Failed to generate report:\n" + str(ex))
    
    def retry(self):
        self.rt.clear(); self.fa.clear()
        self.bdl.setText("Band: --"); self.psl.setText("")
        self.sub.setEnabled(True)
    
    def save_exit(self):
        import sys
        if not self.active: return
        if self.book and self.test and self.part:
            below = self.streak <= 0 and self.attempts > 0
            self.session_mgr.save_session(self.book, self.test, self.part,
                self.qidx, self.history, self.attempts, {"below_standard": below})
            QMessageBox.information(self, "Saved", "Session saved! You can resume later.")
        self.active = False; self.seb.setEnabled(False)
        self.load_sessions()
        QApplication.quit()
        try: sys.exit(99)
        except: pass
    
    def resume(self):
        ss = self.session_mgr.get_all_sessions()
        if not ss: return
        d = QDialog(self); d.setWindowTitle("Resume Session")
        dl = QVBoxLayout(d); lw = QListWidget()
        for s in ss:
            it = QListWidgetItem(f"{s['book']} - {s['test']} - {s['part']} [{s['last_updated'][:16]}]")
            it.setData(Qt.UserRole, s); lw.addItem(it)
        dl.addWidget(QLabel("Choose session:")); dl.addWidget(lw)
        bl = QHBoxLayout(); rb = QPushButton("Resume"); cb = QPushButton("Cancel")
        bl.addWidget(rb); bl.addWidget(cb); dl.addLayout(bl)
        def on_r():
            its = lw.selectedItems()
            if its:
                sd = its[0].data(Qt.UserRole); fd = self.session_mgr.load_session(sd["book"], sd["test"])
                if fd: self.resume_from(fd); d.accept()
        rb.clicked.connect(on_r); cb.clicked.connect(d.reject); d.exec_()
    
    def resume_from(self, data):
        self.book = data["book"]; self.test = data["test"]; self.part = data["part"]
        self.qidx = data["question_index"]; self.history = data.get("conversation_history",[])
        self.attempts = data.get("attempts_count", 0); self.active = True
        self.seb.setEnabled(True)
        self.hlw.clear()
        for e in self.history:
            icon = "+" if e.get("pass") else "-"
            self.hlw.addItem(f"Q{e['q']+1} A{e['a']} Band {e.get('band','?')} {icon}")
        i = self.bc.findText(self.book)
        if i >= 0: self.bc.setCurrentIndex(i)
        i = self.tc.findText(self.test)
        if i >= 0: self.tc.setCurrentIndex(i)
        if self.book == "Custom Questions":
            td = get_test(self.book, self.test)
            if td: self.qdata = td
        else:
            pns = ["Part 1 - Introduction & Interview", "Part 2 - Individual Long Turn", "Part 3 - Discussion"]
            if self.part in pns: self.pc.setCurrentIndex(pns.index(self.part))
            td = get_test(self.book, self.test)
            if td and self.part in td: self.qdata = td[self.part]
        self.show_q()
        for e in reversed(self.history):
            if e.get("q") == self.qidx:
                if e.get("response"):
                    self.rt.setText(e["response"])
                if e.get("feedback"):
                    self.fa.setText(e["feedback"])
                band = e.get("band", 0)
                self.bdl.setText(f"Band: {band}")
                if e.get("pass"):
                    self.psl.setText("PASS")
                    self.psl.setStyleSheet("color: green; font-weight: bold;")
                else:
                    self.psl.setText(f"Band {band}")
                    self.psl.setStyleSheet("color: red; font-weight: bold;")
                break
        self.upd_info(); self.set_status("Resumed")
    
    def auto_save(self):
        if self.book and self.test and self.part:
            below = self.streak <= 0 and self.attempts > 0
            self.session_mgr.save_session(self.book, self.test, self.part,
                self.qidx, self.history, self.attempts, {"below_standard": below})
    
    def upd_info(self):
        if self.active:
            if self.book == "Custom Questions" and self.qdata and "questions" in self.qdata:
                total = len(self.qdata["questions"])
                self.il.setText(f"{self.book}\n{self.test}\nQ{self.qidx+1}/{total}\nAttempts: {self.attempts}\nStreak: {self.streak}")
            else:
                self.il.setText(f"{self.book}\n{self.test}\n{self.part}\nQ{self.qidx+1}\nAttempts: {self.attempts}\nStreak: {self.streak}")
        else:
            self.il.setText("No active session")
    
    def tick(self):
        if self.rec_start: self.elapsed = int(time.time() - self.rec_start)
        else: self.elapsed += 1
        rem = max(0, self.max_secs - self.elapsed)
        self.tml.setText(f"Timer: {rem}s")
        self.pb.setValue(min(100, int(self.elapsed / self.max_secs * 100)))
        if rem <= 0 and self.is_rec:
            self.stop_rec()
            QMessageBox.information(self, "Time", "Time is up!")
    
    def set_status(self, msg):
        self.bs.setText(msg)



    def manage_custom(self):
        """Open dialog to manage custom question sets."""
        from PyQt5.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QPushButton,
            QLabel, QTextEdit, QLineEdit, QComboBox, QFormLayout, QListWidget, QListWidgetItem, QMessageBox)
        from PyQt5.QtCore import Qt

        dlg = QDialog(self)
        dlg.setWindowTitle("Manage Custom Questions")
        dlg.setMinimumSize(600, 450)

        layout = QVBoxLayout(dlg)

        layout.addWidget(QLabel("Existing Custom Test Sets:"))
        lw = QListWidget()
        layout.addWidget(lw)
        self._refresh_custom_list(lw)

        btn_row = QHBoxLayout()
        add_btn = QPushButton("Add New Test Set")
        add_btn.setObjectName("s")
        add_btn.clicked.connect(lambda: self._add_custom_dialog(lw))
        btn_row.addWidget(add_btn)
        edit_btn = QPushButton("Edit Selected")
        edit_btn.setObjectName("p")
        edit_btn.clicked.connect(lambda: self._edit_custom_dialog(lw))
        btn_row.addWidget(edit_btn)
        del_btn = QPushButton("Delete Selected")
        del_btn.setObjectName("d")
        del_btn.clicked.connect(lambda: self._delete_custom(lw))
        btn_row.addWidget(del_btn)
        close_btn = QPushButton("Close")
        close_btn.clicked.connect(dlg.accept)
        btn_row.addWidget(close_btn)
        layout.addLayout(btn_row)
        dlg.exec_()

    def _refresh_custom_list(self, lw):
        """Refresh the custom test sets list widget."""
        lw.clear()
        for name in get_custom_test_names():
            QListWidgetItem(name, lw)

    def _delete_custom(self, lw):
        """Delete selected custom test set."""
        item = lw.currentItem()
        if not item:
            QMessageBox.warning(self, "Warning", "Please select a test set to delete.")
            return
        name = item.text()
        reply = QMessageBox.question(self, "Confirm Delete",
            "Delete test set \"" + name + "\"?\nThis cannot be undone.",
            QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            delete_custom_test_set(name)
            self._refresh_custom_list(lw)
            # Refresh the test combo if Custom Questions is selected
            if self.bc.currentText() == "Custom Questions":
                current = self.bc.currentText()
                self.on_book(current)

    def _edit_custom_dialog(self, lw):
        """Edit selected custom test set - load existing data, allow modification."""
        from PyQt5.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QPushButton,
            QLabel, QTextEdit, QLineEdit, QComboBox, QFormLayout, QMessageBox)
        import json as _jj, os as _oo

        item = lw.currentItem()
        if not item:
            QMessageBox.warning(self, "Warning", "Please select a test set to edit.")
            return
        name = item.text()

        # Load existing data
        _jp = _oo.path.join(_oo.path.dirname(__file__), "data", "custom_questions.json")
        if not _oo.path.exists(_jp):
            QMessageBox.warning(self, "Error", "Data file not found.")
            return
        with open(_jp, "r", encoding="utf-8") as _f:
            _ad = _jj.load(_f)
        if name not in _ad:
            QMessageBox.warning(self, "Error", 'Test set "' + name + '" not found.')
            return
        _data = _ad[name]
        _questions = _data.get("questions", [])

        dlg = QDialog(self)
        dlg.setWindowTitle("Edit: " + name)
        dlg.setMinimumSize(650, 550)

        form = QFormLayout(dlg)

        name_edit = QLineEdit()
        name_edit.setText(name)
        form.addRow("Test Set Name:", name_edit)

        # Determine type from first question
        _ft = _questions[0].get("type", "P2") if _questions else "P2"
        _tm = {"P1": "Part 1 (Short Answer)", "P2": "Part 2 (Cue Card)", "P3": "Part 3 (Discussion)"}

        qtype_combo = QComboBox()
        qtype_combo.addItems(["Part 2 (Cue Card)", "Part 1 (Short Answer)", "Part 3 (Discussion)"])
        qtype_combo.setCurrentText(_tm.get(_ft, "Part 2 (Cue Card)"))
        form.addRow("Question Type:", qtype_combo)

        # Reconstruct text content from questions
        _cl = []
        for _q in _questions:
            if _q.get("type") == "P2":
                if _cl:
                    _cl.append("")
                _cl.append(_q.get("cue_card", ""))
                for _p in _q.get("prompts", []):
                    _cl.append(_p)
            else:
                if _cl:
                    _cl.append("")
                _cl.append(_q.get("question", ""))
        _ct = "\n".join(_cl)

        content_edit = QTextEdit()
        content_edit.setMinimumHeight(280)
        content_edit.setPlainText(_ct)
        form.addRow("Content:", content_edit)

        btn_row = QHBoxLayout()
        save_btn = QPushButton("Save Changes")
        save_btn.setObjectName("s")
        cancel_btn = QPushButton("Cancel")
        btn_row.addStretch()
        btn_row.addWidget(save_btn)
        btn_row.addWidget(cancel_btn)
        form.addRow(btn_row)

        def on_save():
            reply = QMessageBox.question(dlg, "Confirm Save",
                "Save changes to this test set?\nThis will overwrite the current data.",
                QMessageBox.Yes | QMessageBox.No)
            if reply != QMessageBox.Yes:
                return

            new_name = name_edit.text().strip()
            if not new_name:
                QMessageBox.warning(dlg, "Warning", "Test set name is required.")
                return

            qt = qtype_combo.currentText()
            raw = content_edit.toPlainText().strip()
            if not raw:
                QMessageBox.warning(dlg, "Warning", "Content cannot be empty.")
                return

            _new_qs = []
            if "Part 2" in qt:
                _blocks = re.split(r'\n\s*\n', raw)
                for _block in _blocks:
                    _block = _block.strip()
                    if not _block:
                        continue
                    _lines = _block.split("\n")
                    _card = _lines[0].strip()
                    _card = re.sub(r"^\d+[\)\.]\s*", "", _card).strip()
                    _pr = []
                    for _l in _lines[1:]:
                        _l = _l.strip()
                        if _l and _l.lower().strip(":") != "you should say":
                            _pr.append(_l)
                    if _card:
                        _new_qs.append({"type": "P2", "cue_card": _card, "prompts": _pr})
            else:
                _pf = "P1" if "Part 1" in qt else "P3"
                for _line in raw.split("\n"):
                    _line = _line.strip()
                    if _line:
                        _new_qs.append({"type": _pf, "question": _line})

            if not _new_qs:
                QMessageBox.warning(dlg, "Warning", "Could not parse any questions.")
                return

            # Delete old and save new
            from data.question_bank import delete_custom_test_set, add_custom_test_set
            delete_custom_test_set(name)
            add_custom_test_set(new_name, questions_data={"questions": _new_qs})

            QMessageBox.information(dlg, "Saved", 'Test set "' + new_name + '" updated!')
            dlg.accept()
            self._refresh_custom_list(lw)
            if self.bc.currentText() == "Custom Questions":
                self.on_book("Custom Questions")

        save_btn.clicked.connect(on_save)
        cancel_btn.clicked.connect(dlg.reject)
        dlg.exec_()

    def _add_custom_dialog(self, parent_list_widget=None):
        """Open dialog to add a new custom test set. Flat format - no Part concept."""
        from PyQt5.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QPushButton,
            QLabel, QTextEdit, QLineEdit, QComboBox, QFormLayout, QMessageBox)

        dlg = QDialog(self)
        dlg.setWindowTitle("Add Custom Test Set")
        dlg.setMinimumSize(650, 550)

        form = QFormLayout(dlg)

        name_edit = QLineEdit()
        name_edit.setPlaceholderText("e.g. Tutor Set 1, Week 3 Practice...")
        form.addRow("Test Set Name:", name_edit)

        qtype_combo = QComboBox()
        qtype_combo.addItems(["Part 2 (Cue Card)", "Part 1 (Short Answer)", "Part 3 (Discussion)"])
        form.addRow("Question Type:", qtype_combo)

        help_label = QLabel(
            "Part 2: paste cue cards separated by blank lines.\n"
            "  First line of each block = cue card, rest = prompts.\n"
            "Part 1/3: one question per line."
        )
        help_label.setStyleSheet("color: #666; font-size: 11pt;")
        form.addRow(help_label)

        content_edit = QTextEdit()
        content_edit.setMinimumHeight(280)
        content_edit.setPlaceholderText(
            "Paste your questions below.\n\n"
            "For Part 1 or Part 3: One question per line.\n\n"
            "For Part 2 (Cue Card): Separate each cue card with a blank line.\n"
            "  First line = cue card description.\n"
            "  Remaining lines = prompts.\n\n"
            "Example for Part 2:\n"
            "Describe a person who has strong opinions\n"
            "Who this person is\n"
            "How you knew him/her\n\n"
            "Describe an old friend you found again\n"
            "Who he/she is\n"
            "How you knew each other"
        )
        form.addRow("Content:", content_edit)

        def update_help():
            qt = qtype_combo.currentText()
            if "Part 2" in qt:
                help_label.setText(
                    "Part 2: paste cue cards separated by blank lines.\n"
                    "  First line of each block = cue card, rest = prompts."
                )
            else:
                help_label.setText("Part 1/3: one question per line.")

        qtype_combo.currentTextChanged.connect(update_help)

        btn_row = QHBoxLayout()
        save_btn = QPushButton("Save Test Set")
        save_btn.setObjectName("s")
        cancel_btn = QPushButton("Cancel")
        btn_row.addStretch()
        btn_row.addWidget(save_btn)
        btn_row.addWidget(cancel_btn)
        form.addRow(btn_row)

        def on_save():
            name = name_edit.text().strip()
            if not name:
                QMessageBox.warning(dlg, "Warning", "Test set name is required.")
                return

            qt = qtype_combo.currentText()
            raw = content_edit.toPlainText().strip()
            if not raw:
                QMessageBox.warning(dlg, "Warning", "Please enter at least one question.")
                return

            questions = []

            if "Part 2" in qt:
                blocks = re.split(r'\n\s*\n', raw)
                for block in blocks:
                    block = block.strip()
                    if not block:
                        continue
                    lines = block.split('\n')
                    card_text = lines[0].strip()
                    card_text = re.sub(r'^\d+[\)\.]\s*', '', card_text).strip()
                    prompts = []
                    for l in lines[1:]:
                        l = l.strip()
                        if l and l.lower().strip(":") != "you should say":
                            prompts.append(l)
                    if card_text:
                        questions.append({"type": "P2", "cue_card": card_text, "prompts": prompts})
            else:
                for line in raw.split('\n'):
                    line = line.strip()
                    if line:
                        prefix = "P1" if "Part 1" in qt else "P3"
                        questions.append({"type": prefix, "question": line})

            if not questions:
                QMessageBox.warning(dlg, "Warning", "Could not parse any questions.")
                return

            add_custom_test_set(name, questions_data={"questions": questions})
            QMessageBox.information(dlg, "Saved", 'Test set "' + name + '" saved successfully!')
            dlg.accept()
            if parent_list_widget:
                self._refresh_custom_list(parent_list_widget)
            if self.bc.currentText() == "Custom Questions":
                self.on_book("Custom Questions")

        save_btn.clicked.connect(on_save)
        cancel_btn.clicked.connect(dlg.reject)
        dlg.exec_()
def main():
    import sys, os
    os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "1"
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setFont(QFont("Segoe UI", 14))
    w = App()
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
