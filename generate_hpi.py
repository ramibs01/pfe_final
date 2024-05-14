import sys
import os
import shutil
import subprocess
from PyQt5.QtWidgets import QApplication, QFileDialog, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget, QMessageBox
from PyQt5.QtGui import QIcon

class GenerateHPIWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("Generate your HPI file")
        self.setWindowIcon(QIcon("Icons_home/hpi-removebg-preview.png"))

    def init_ui(self):
        layout = QVBoxLayout(self)

        # Create a label to indicate the purpose of the widget
        label = QLabel("Choose a location to save your HPI file")
        layout.addWidget(label)

        # Create a label to display the chosen location
        self.location_label = QLabel("")
        layout.addWidget(self.location_label)

        # Create a horizontal layout for the buttons
        button_layout = QHBoxLayout()

        # Add stretch to move the buttons to the bottom
        button_layout.addStretch()

        # Create a button to open the file dialog
        self.choose_button = QPushButton("Choose Location")
        self.choose_button.clicked.connect(self.choose_location)
        button_layout.addWidget(self.choose_button)

        # Create a button to generate the file
        self.generate_button = QPushButton("Generate")
        self.generate_button.clicked.connect(self.generate_file)
        self.generate_button.setEnabled(False)  # Disable initially
        button_layout.addWidget(self.generate_button)

        # Add the button layout to the main layout
        layout.addLayout(button_layout)

    def choose_location(self):
        options = QFileDialog.Options()
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder to Save HPI Files", options=options)
        if folder_path:
            self.location_label.setText(f"Chosen Location: {folder_path}")
            self.generate_button.setEnabled(True)  # Enable the generate button

    def generate_file(self):
        folder_path = self.location_label.text().replace("Chosen Location: ", "")

        # Create src/main/java/org/jenkins/ci/plugins/jobimport directory
        java_dir = os.path.join(folder_path, "src", "main", "java", "org", "jenkins", "ci", "plugins", "jobimport")
        os.makedirs(java_dir, exist_ok=True)

        # Create src/main/resources/org/jenkins/ci/plugins/jobimport/Class_1 directory
        resources_dir = os.path.join(folder_path, "src", "main", "resources", "org", "jenkins", "ci", "plugins", "jobimport", "MyPlugin")
        os.makedirs(resources_dir, exist_ok=True)

        # Copy Java file
        java_src = "check_generated/MyPlugin.java"
        java_dest = os.path.join(java_dir, "MyPlugin.java")
        shutil.copy(java_src, java_dest)

        # Copy Jelly files
        jelly_src = "check_generated/index.jelly"
        jelly_dest = os.path.join(resources_dir, "index.jelly")
        shutil.copy(jelly_src, jelly_dest)

        # Copy pom.xml
        pom_src = "check_generated/pom.xml"
        pom_dest = os.path.join(folder_path, "pom.xml")
        shutil.copy(pom_src, pom_dest)

        #os.startfile("C:/Users/rami dob/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/System Tools/Command Prompt.lnk")
        batch_file_path = os.path.join(os.environ["TEMP"], "cd_to_folder.bat")
        with open(batch_file_path, "w") as batch_file:
            batch_file.write(f'@echo off\n')
            batch_file.write(f'cd /d "{folder_path}"\n')
            batch_file.write(f'mvn package install -DskipTests\n')
        # Open a command prompt window and execute the batch file
        subprocess.Popen(["cmd", "/K", batch_file_path])
        #QMessageBox.information(self, "Success", "HPI file generated and Maven command executed successfully!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    generate_hpi_widget = GenerateHPIWidget()
    generate_hpi_widget.show()
    sys.exit(app.exec_())
