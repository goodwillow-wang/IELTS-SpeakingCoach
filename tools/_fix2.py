import re
import json as _json
import os as _os

with open(r"D:\EricWork\IELTS-SpeakingCoach\main.py", "r", encoding="utf-8") as f:
    m = f.read()

# ===== 1) Fix Manage Custom Questions button - split to two lines =====
old_mcb = '        self.mcb = QPushButton("Manage Custom Questions")'
new_mcb = '        self.mcb = QPushButton("Manage\\nCustom Questions")'
m = m.replace(old_mcb, new_mcb)
print("1) Button text split: OK")

# ===== 2) Add Edit button + edit method in manage_custom =====

# Find manage_custom method and add Edit button
old_mc = '''    def manage_custom(self):
        """Open dialog to manage custom question sets."""
        from PyQt5.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QPushButton,
            QLabel, QTextEdit, QLineEdit, QListWidget, QListWidgetItem, QMessageBox)
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
        del_btn = QPushButton("Delete Selected")
        del_btn.setObjectName("d")
        del_btn.clicked.connect(lambda: self._delete_custom(lw))
        btn_row.addWidget(del_btn)
        close_btn = QPushButton("Close")
        close_btn.clicked.connect(dlg.accept)
        btn_row.addWidget(close_btn)
        layout.addLayout(btn_row)
        dlg.exec_()'''

new_mc = '''    def manage_custom(self):
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
        dlg.exec_()'''

m = m.replace(old_mc, new_mc)
print("2) manage_custom Edit button: OK")

# ===== 3) Add _edit_custom_dialog method =====
# Find the spot before _delete_custom (just after manage_custom)
# Actually, let me find where _add_custom_dialog starts and insert _edit_custom_dialog right before it

old_add_start = '    def _add_custom_dialog(self, parent_list_widget=None):'
# Insert _edit_custom_dialog right before _add_custom_dialog
new_method = '''    def _edit_custom_dialog(self, lw):
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
        _ct = "\\n".join(_cl)

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
                "Save changes to this test set?\\nThis will overwrite the current data.",
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
                _blocks = re.split(r'\\n\\s*\\n', raw)
                for _block in _blocks:
                    _block = _block.strip()
                    if not _block:
                        continue
                    _lines = _block.split("\\n")
                    _card = _lines[0].strip()
                    _card = re.sub(r"^\\d+[\\)\\.]\\s*", "", _card).strip()
                    _pr = []
                    for _l in _lines[1:]:
                        _l = _l.strip()
                        if _l and _l.lower().strip(":") != "you should say":
                            _pr.append(_l)
                    if _card:
                        _new_qs.append({"type": "P2", "cue_card": _card, "prompts": _pr})
            else:
                _pf = "P1" if "Part 1" in qt else "P3"
                for _line in raw.split("\\n"):
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

''' + old_add_start

# Find the exact location to insert
idx = m.find(old_add_start)
if idx > 0:
    m = m[:idx] + new_method + m[idx + len(old_add_start):]
    print("3) _edit_custom_dialog method: OK")
else:
    print("3) ERROR: Could not find insertion point")

with open(r"D:\EricWork\IELTS-SpeakingCoach\main.py", "w", encoding="utf-8") as f:
    f.write(m)

import py_compile
try:
    py_compile.compile(r"D:\EricWork\IELTS-SpeakingCoach\main.py", doraise=True)
    print("4) Syntax: OK")
except py_compile.PyCompileError as e:
    print(f"4) Syntax ERROR: {e}")
