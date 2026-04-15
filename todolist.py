import sys
import json
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QLineEdit, QListWidget, QListWidgetItem, QMessageBox
)
from PyQt5.QtCore import Qt


class TodoApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("To-Do List App")
        self.setGeometry(200, 300, 350, 450)

        layout = QVBoxLayout()

        # Input
        self.input = QLineEdit()
        self.input.setPlaceholderText("Enter your task...")

        # Buttons
        self.add_btn = QPushButton("Add Task")
        self.delete_btn = QPushButton("Delete Selected ❌")
        self.complete_btn = QPushButton("Mark Complete ✅")

        # List
        self.list_widget = QListWidget()

        # Add to layout
        layout.addWidget(self.input)
        layout.addWidget(self.add_btn)
        layout.addWidget(self.delete_btn)
        layout.addWidget(self.complete_btn)
        layout.addWidget(self.list_widget)

        self.setLayout(layout)

        # Connect buttons
        self.add_btn.clicked.connect(self.add_task)
        self.delete_btn.clicked.connect(self.delete_task)
        self.complete_btn.clicked.connect(self.mark_complete)

        # Load saved tasks
        self.load_tasks()

    # ➕ Add Task
    def add_task(self):
        task = self.input.text()

        if task != "":
            item = QListWidgetItem(task)
            self.list_widget.addItem(item)
            self.input.clear()
            self.save_tasks()

    # ❌ Delete Task
    def delete_task(self):
        selected = self.list_widget.currentRow()

        if selected >= 0:
            self.list_widget.takeItem(selected)
            self.save_tasks()
        else:
            QMessageBox.warning(self, "Warning", "Please select a task!")

    def mark_complete(self):
        item = self.list_widget.currentItem()

        if item:
            font = item.font()
            font.setStrikeOut(not font.strikeOut())  
            item.setFont(font)
            self.save_tasks()
        else:
            QMessageBox.warning(self, "Warning", "Select a task first!")

    def save_tasks(self):
        tasks = []

        for i in range(self.list_widget.count()):
            item = self.list_widget.item(i)
            tasks.append({
                "text": item.text(),
                "completed": item.font().strikeOut()
            })

        with open("tasks.json", "w") as f:
            json.dump(tasks, f)

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as f:
                tasks = json.load(f)

                for task in tasks:
                    item = QListWidgetItem(task["text"])

                    if task["completed"]:
                        font = item.font()
                        font.setStrikeOut(True)
                        item.setFont(font)

                    self.list_widget.addItem(item)
        except:
            pass


app = QApplication(sys.argv)
window = TodoApp()
window.show()
sys.exit(app.exec_())