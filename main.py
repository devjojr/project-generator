import sys
import os
import subprocess
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QLineEdit,
    QFileDialog,
    QComboBox,
)


class ProjectGenerationWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Project Generator")
        self.setGeometry(300, 300, 600, 400)

        layout = QVBoxLayout()

        # project name and input
        self.project_name_label = QLabel("Project Name:")
        layout.addWidget(self.project_name_label)

        self.project_name_input = QLineEdit()
        layout.addWidget(self.project_name_input)

        # choice of project type
        self.project_type_label = QLabel("Project Type:")
        layout.addWidget(self.project_type_label)

        self.project_type_list = QComboBox()
        self.project_type_list.addItems(
            ["Standard Web App", "Node.js App", "React App"]
        )
        layout.addWidget(self.project_type_list)

        # selecting a folder for the project
        self.project_folder_label = QLabel("Project Folder:")
        layout.addWidget(self.project_folder_label)

        self.project_folder_input = QLineEdit()
        self.project_folder_input.setReadOnly(True)
        layout.addWidget(self.project_folder_input)

        self.project_folder_button = QPushButton("Browse")
        self.project_folder_button.clicked.connect(self.browse_folder)
        layout.addWidget(self.project_folder_button)

        # generate project button
        self.generate_project_button = QPushButton("Generate")
        self.generate_project_button.clicked.connect(self.generate_boilerplate)
        layout.addWidget(self.generate_project_button)

        # setting widget layout
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def browse_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder:
            self.project_folder_input.setText(folder)

    def generate_boilerplate(self):
        project_name = self.project_name_input.text()
        project_folder = self.project_folder_input.text()
        project_type = self.project_type_list.currentText()

        if project_type == "Standard Web App":
            self.create_standard_web_app(project_name, project_folder)
        elif project_type == "Node.js App":
            self.create_nodejs_app(project_name, project_folder)
        elif project_type == "React App":
            self.create_react_app(project_name, project_folder)

    def create_standard_web_app(self, project_name, project_folder):
        with open(os.path.join(project_folder, "index.html"), "w") as f:
            f.write("<!DOCTYPE html>\n")
            f.write("<html lang='en'>\n")
            f.write("<head>\n")
            f.write("    <meta charset='UTF-8'>\n")
            f.write(
                "    <meta name='viewport' content='width=device-width, initial-scale=1.0'>\n"
            )
            f.write("    <title>{}</title>\n".format(project_name))
            f.write("    <link rel='stylesheet' href='styles.css'>\n")
            f.write("</head>\n")
            f.write("<body>\n")
            f.write("    <h1>Welcome to {}</h1>\n".format(project_name))
            f.write("    <script src='script.js'></script>\n")
            f.write("</body>\n")
            f.write("</html>\n")

        with open(os.path.join(project_folder, "styles.css"), "w") as f:
            f.write("/* Enter your CSS styles here */\n")

        with open(os.path.join(project_folder, "script.js"), "w") as f:
            f.write("// Enter your JavaScript code here\n")

        print(
            f"Standard Web App generated for project '{project_name}' in folder '{project_folder}'"
        )

    def create_nodejs_app(self, project_name, project_folder):
        if not os.path.exists(project_folder):
            os.makedirs(project_folder)

        os.chdir(project_folder)

        subprocess.run(["npm", "init", "-y"])
        with open(os.path.join(project_folder, "index.js"), "w") as f:
            f.write("// Enter your code here\n")

        print(
            f"Node.js app generated for project '{project_name}' in folder '{project_folder}'"
        )

    def create_react_app(self, project_name, project_folder):
        if not os.path.exists(project_folder):
            os.makedirs(project_folder)

        os.chdir(project_folder)

        subprocess.run(["npx", "create-react-app", project_name])

        print(
            f"React app generated for project '{project_name}' in folder '{project_folder}'"
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProjectGenerationWindow()
    window.show()
    sys.exit(app.exec())
