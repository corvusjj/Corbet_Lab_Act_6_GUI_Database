from PyQt6.QtWidgets import QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QMessageBox, QTableWidgetItem, QTableWidget, QHeaderView, QWidget

from .model import Student
from .service import StudentServices

class StudentView(QWidget):
    def __init__(self, service: StudentServices):
        super(). __init__()
        self.service = service
        self.setWindowTitle("Student Management")
        self.resize(600, 400)
        self.build_ui()
        

    def build_ui(self)-> None:
        layout = QVBoxLayout(self)

        form = QFormLayout()
        self.name_input = QLineEdit()
        self.email_input = QLineEdit()
        form.addRow("Name", self.name_input)
        form.addRow("Email", self.email_input)
        layout.addLayout(form)

        add_Button = QPushButton("Add Student")
        add_Button.clicked.connect(self.add_Student)
        layout.addWidget(add_Button)

        self.table = QTableWidget(0, 3)
        self.table.setHorizontalHeaderLabels(["ID", "Name", "Email"])
        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )
        layout.addWidget(self.table)

    def add_Student(self) -> None:
        try:
            student = Student(self.name_input.text(), self.email_input.text())
            self.service.add_student(student)
        except ValueError as error:
            QMessageBox.warning(self,"Invalid Student", str(error))
            return

        self.name_input.clear()
        self.email_input.clear()
        self.refresh()

    def refresh(self) -> None:
        students = self.service.get_students()
        self.table.setRowCount(len(students))

        for row, student in enumerate(students):

            self.table.setItem(
                row, 0,
                QTableWidgetItem(str(student.id))
                )

            self.table.setItem(
                row, 1,
                QTableWidgetItem(student.name)
                )

            self.table.setItem(
                row, 2,
                QTableWidgetItem(student.email)
                )
