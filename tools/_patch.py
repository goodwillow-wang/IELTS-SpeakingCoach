import re, json as _json

# ===== 1) custom_questions.json - convert to flat format =====
cq_path = r"D:\EricWork\IELTS-SpeakingCoach\data\custom_questions.json"
with open(cq_path, 'r', encoding='utf-8') as f:
    old_data = _json.load(f)

new_data = {}
for name, content in old_data.items():
    questions = []
    p2 = content.get('Part 2 - Individual Long Turn', {})
    for cc in p2.get('cue_cards', []):
        questions.append({'type': 'P2', 'cue_card': cc['cue_card'], 'prompts': cc.get('prompts', [])})
    p1 = content.get('Part 1 - Introduction & Interview', {})
    for q in p1.get('questions', []):
        questions.append({'type': 'P1', 'question': q})
    p3 = content.get('Part 3 - Two-way Discussion', {})
    for q in p3.get('questions', []):
        questions.append({'type': 'P3', 'question': q})
    if not questions and 'questions' in content:
        questions = content['questions']
    if questions:
        new_data[name] = {'questions': questions}

with open(cq_path, 'w', encoding='utf-8') as f:
    _json.dump(new_data, f, ensure_ascii=False, indent=2)
print('custom_questions.json: OK')

# ===== 2) main.py - all changes =====
with open(r'D:\EricWork\IELTS-SpeakingCoach\main.py', 'r', encoding='utf-8') as f:
    m = f.read()

# 2a) init_ui: wrap Part selector in a container widget
old_part = '        sl.addWidget(QLabel("Part:"))\n        self.pc = QComboBox()\n        self.pc.addItems(["Part 1 Interview", "Part 2 Long Turn", "Part 3 Discussion"])\n        sl.addWidget(self.pc)'
new_part = '        self.part_container = QWidget()\n        pcl = QVBoxLayout(self.part_container)\n        pcl.setContentsMargins(0,0,0,0)\n        pcl.addWidget(QLabel("Part:"))\n        self.pc = QComboBox()\n        self.pc.addItems(["Part 1 Interview", "Part 2 Long Turn", "Part 3 Discussion"])\n        pcl.addWidget(self.pc)\n        sl.addWidget(self.part_container)'
m = m.replace(old_part, new_part)
print('  init_ui Part container: OK')

# 2b) on_book: hide part_container for Custom Questions
old_ob = '    def on_book(self, book):\n        self.tc.clear()\n        if book in IELTS_SPEAKING_QUESTIONS:\n            for t in IELTS_SPEAKING_QUESTIONS[book]:\n                self.tc.addItem(t)\n        self.mcb.setVisible(book == "Custom Questions")'
new_ob = '    def on_book(self, book):\n        self.tc.clear()\n        if book in IELTS_SPEAKING_QUESTIONS:\n            for t in IELTS_SPEAKING_QUESTIONS[book]:\n                self.tc.addItem(t)\n        is_custom = (book == "Custom Questions")\n        self.part_container.setVisible(not is_custom)\n        self.mcb.setVisible(is_custom)'
m = m.replace(old_ob, new_ob)
print('  on_book: OK')

# 2c) start(): add Custom Questions branch BEFORE Cambridge logic
old_start = '    def start(self):\n        book = self.bc.currentText()\n        test = self.tc.currentText()\n        pi = self.pc.currentIndex()\n        pns = ["Part 1 - Introduction & Interview", "Part 2 - Individual Long Turn", "Part 3 - Two-way Discussion"]\n        pn = pns[pi]\n        if not book or not test:\n            QMessageBox.warning(self, "Error", "Please select book and test")\n            return\n        td = get_test(book, test)\n        if not td or pn not in td:\n            QMessageBox.warning(self, "Error", "Test data not found")\n            return'
new_start = '    def start(self):\n        book = self.bc.currentText()\n        test = self.tc.currentText()\n        if not book or not test:\n            QMessageBox.warning(self, "Error", "Please select book and test")\n            return\n        td = get_test(book, test)\n        if not td:\n            QMessageBox.warning(self, "Error", "Test data not found")\n            return\n        if book == "Custom Questions":\n            if "questions" not in td or not td["questions"]:\n                QMessageBox.warning(self, "Error", "No questions in this test set.")\n                return\n            exist = self.session_mgr.load_session(book, test)\n            if exist:\n                r = QMessageBox.question(self, "Session Found", "Resume existing session?", QMessageBox.Yes | QMessageBox.No)\n                if r == QMessageBox.Yes:\n                    self.resume_from(exist)\n                    return\n            self.book = book; self.test = test; self.part = "Custom"\n            self.hlw.clear(); self.qidx = 0; self.history = []; self.attempts = 0; self.streak = 0\n            self.active = True; self.qdata = td\n            self.seb.setEnabled(True); self.rb.setEnabled(False)\n            self.show_q(); self.upd_info(); self.set_status("Started")\n            return\n        pi = self.pc.currentIndex()\n        pns = ["Part 1 - Introduction & Interview", "Part 2 - Individual Long Turn", "Part 3 - Two-way Discussion"]\n        pn = pns[pi]\n        if pn not in td:\n            QMessageBox.warning(self, "Error", "Test data not found")\n            return'
m = m.replace(old_start, new_start)
print('  start(): OK')

# 2d) show_q(): add flat format handler BEFORE existing logic
old_sq = '    def show_q(self):\n        d = self.qdata\n        if not d: return\n        pn = self.part\n        self.sample_btn.setEnabled(False)\n        self.sample_btn.setVisible(False)'
new_sq = '    def show_q(self):\n        d = self.qdata\n        if not d: return\n        pn = self.part\n        self.sample_btn.setEnabled(False)\n        self.sample_btn.setVisible(False)\n        if "questions" in d:\n            qs = d["questions"]\n            if self.qidx >= len(qs):\n                self.qa.setText("All questions completed! Practice another test.")\n                self.rt.clear(); self.fa.clear()\n                return\n            q = qs[self.qidx]\n            qt = q.get("type", "P2")\n            if qt == "P2":\n                txt = f"[Question {self.qidx+1}/{len(qs)}]\\n\\n{q[\'cue_card\']}\\n"\n                for ip, p in enumerate(q.get("prompts",[]), 1):\n                    txt += f"  {ip}. {p}\\n"\n                txt += "\\n[Speak for 1-2 minutes]"\n                self.max_secs = 120\n                self.current_topic = q[\'cue_card\']\n                self.current_part_num = 2\n            else:\n                txt = f"[Question {self.qidx+1}/{len(qs)}]\\n\\n{q.get(\'question\',\'\')}"\n                if qt == "P1":\n                    self.max_secs = 30; self.current_part_num = 1\n                else:\n                    self.max_secs = 45; self.current_part_num = 3\n                self.current_topic = q.get(\'question\',\'\')[:60]\n            self.qa.setText(txt)\n            self.rt.clear(); self.fa.clear()\n            self.bdl.setText("Band: --"); self.psl.setText("")\n            self.sub.setEnabled(True)\n            self.attempts = 0; self.eval = None\n            self.elapsed = 0; self.rec_start = None\n            self.tml.setText("Timer: Ready"); self.pb.setValue(0)\n            self.timer.stop()\n            return'
m = m.replace(old_sq, new_sq)
print('  show_q(): OK')

# 2e) submit(): add flat format handler
old_sp = '        self.attempts += 1\n        pi = self.pc.currentIndex() + 1\n        d = self.qdata\n        if self.part == "Part 2 - Individual Long Turn":\n            cue_cards = d.get("cue_cards", None)\n            if cue_cards and isinstance(cue_cards, list) and self.qidx < len(cue_cards):\n                qi = cue_cards[self.qidx]\n            else:\n                qi = d\n        else:\n            qs = d.get("questions", [])\n            qi = [qs[self.qidx]] if self.qidx < len(qs) else qs'
new_sp = '        self.attempts += 1\n        d = self.qdata\n        pi = 1\n        if "questions" in d:\n            q = d["questions"][self.qidx]\n            qt = q.get("type", "P2")\n            pi = int(qt[1]) if len(qt) >= 2 else 2\n            if qt == "P2":\n                qi = q\n            else:\n                qi = [q.get(\'question\',\'\')]\n        elif self.part == "Part 2 - Individual Long Turn":\n            pi = 2\n            cue_cards = d.get("cue_cards", None)\n            if cue_cards and isinstance(cue_cards, list) and self.qidx < len(cue_cards):\n                qi = cue_cards[self.qidx]\n            else:\n                qi = d\n        else:\n            pi = self.pc.currentIndex() + 1 if hasattr(self, \'pc\') else 1\n            qs = d.get("questions", [])\n            qi = [qs[self.qidx]] if self.qidx < len(qs) else qs'
m = m.replace(old_sp, new_sp)
print('  submit(): OK')

# 2f) resume_from(): handle custom format
old_rf = '        i = self.bc.findText(self.book)\n        if i >= 0: self.bc.setCurrentIndex(i)\n        i = self.tc.findText(self.test)\n        if i >= 0: self.tc.setCurrentIndex(i)\n        pns = ["Part 1 - Introduction & Interview", "Part 2 - Individual Long Turn", "Part 3 - Two-way Discussion"]\n        if self.part in pns: self.pc.setCurrentIndex(pns.index(self.part))\n        td = get_test(self.book, self.test)\n        if td and self.part in td: self.qdata = td[self.part]'
new_rf = '        i = self.bc.findText(self.book)\n        if i >= 0: self.bc.setCurrentIndex(i)\n        i = self.tc.findText(self.test)\n        if i >= 0: self.tc.setCurrentIndex(i)\n        if self.book == "Custom Questions":\n            td = get_test(self.book, self.test)\n            if td: self.qdata = td\n        else:\n            pns = ["Part 1 - Introduction & Interview", "Part 2 - Individual Long Turn", "Part 3 - Two-way Discussion"]\n            if self.part in pns: self.pc.setCurrentIndex(pns.index(self.part))\n            td = get_test(self.book, self.test)\n            if td and self.part in td: self.qdata = td[self.part]'
m = m.replace(old_rf, new_rf)
print('  resume_from(): OK')

# 2g) Replace entire _add_custom_dialog with flat-format version
old_ds = '    def _add_custom_dialog(self, parent_list_widget=None):\n        """Open dialog to add a new custom test set."""'
start_ds = m.find(old_ds)
end_ds = m.find('\ndef main():\n')
old_dialog = m[start_ds:end_ds]

new_dialog = '''    def _add_custom_dialog(self, parent_list_widget=None):
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
            "Part 2: paste cue cards separated by blank lines.\\n"
            "  First line of each block = cue card, rest = prompts.\\n"
            "Part 1/3: one question per line."
        )
        help_label.setStyleSheet("color: #666; font-size: 11pt;")
        form.addRow(help_label)

        content_edit = QTextEdit()
        content_edit.setMinimumHeight(280)
        content_edit.setPlaceholderText(
            "Paste your questions below.\\n\\n"
            "For Part 1 or Part 3: One question per line.\\n\\n"
            "For Part 2 (Cue Card): Separate each cue card with a blank line.\\n"
            "  First line = cue card description.\\n"
            "  Remaining lines = prompts.\\n\\n"
            "Example for Part 2:\\n"
            "Describe a person who has strong opinions\\n"
            "Who this person is\\n"
            "How you knew him/her\\n\\n"
            "Describe an old friend you found again\\n"
            "Who he/she is\\n"
            "How you knew each other"
        )
        form.addRow("Content:", content_edit)

        def update_help():
            qt = qtype_combo.currentText()
            if "Part 2" in qt:
                help_label.setText(
                    "Part 2: paste cue cards separated by blank lines.\\n"
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
                blocks = re.split(r'\\n\\s*\\n', raw)
                for block in blocks:
                    block = block.strip()
                    if not block:
                        continue
                    lines = block.split('\\n')
                    card_text = lines[0].strip()
                    card_text = re.sub(r'^\\d+[\\)\\.]\\s*', '', card_text).strip()
                    prompts = []
                    for l in lines[1:]:
                        l = l.strip()
                        if l and l.lower().strip(":") != "you should say":
                            prompts.append(l)
                    if card_text:
                        questions.append({"type": "P2", "cue_card": card_text, "prompts": prompts})
            else:
                for line in raw.split('\\n'):
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
        dlg.exec_()'''

m = m[:start_ds] + new_dialog + m[end_ds:]
print('  _add_custom_dialog(): OK')

# 2h) upd_info: show Q count for custom format
old_ui = '    def upd_info(self):\n        if self.active:\n            self.il.setText(f"{self.book}\\n{self.test}\\n{self.part}\\nQ{self.qidx+1}\\nAttempts: {self.attempts}\\nStreak: {self.streak}")\n        else:\n            self.il.setText("No active session")'
new_ui = '    def upd_info(self):\n        if self.active:\n            if self.book == "Custom Questions" and self.qdata and "questions" in self.qdata:\n                total = len(self.qdata["questions"])\n                self.il.setText(f"{self.book}\\n{self.test}\\nQ{self.qidx+1}/{total}\\nAttempts: {self.attempts}\\nStreak: {self.streak}")\n            else:\n                self.il.setText(f"{self.book}\\n{self.test}\\n{self.part}\\nQ{self.qidx+1}\\nAttempts: {self.attempts}\\nStreak: {self.streak}")\n        else:\n            self.il.setText("No active session")'
m = m.replace(old_ui, new_ui)
print('  upd_info(): OK')

with open(r'D:\EricWork\IELTS-SpeakingCoach\main.py', 'w', encoding='utf-8') as f:
    f.write(m)
print('main.py: ALL OK')
