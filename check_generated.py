import os
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QPushButton, QFileDialog, QHBoxLayout, QLabel, QLineEdit, QDialog, QSplitter, QScrollArea
from PyQt5.QtGui import QIcon

class CheckGeneratedWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("Check your generated files")
        self.setWindowIcon(QIcon("Icons_home/preview-removebg-preview.png"))

    def init_ui(self):
        layout = QVBoxLayout(self)

        # Create a splitter to divide the window into two sections
        splitter = QSplitter(self)
        layout.addWidget(splitter)

        # Left section for file buttons
        files_widget = QWidget()
        files_layout = QVBoxLayout(files_widget)

        # Create a scroll area to contain the buttons
        scroll_area = QScrollArea()
        files_layout.addWidget(scroll_area)

        # Create a widget to hold the buttons
        buttons_widget = QWidget()
        scroll_area.setWidget(buttons_widget)
        scroll_area.setWidgetResizable(True)  # Allow resizing of the widget inside the scroll area

        # Create a layout for the buttons
        buttons_layout = QVBoxLayout(buttons_widget)

        # Get the list of files in the specified directory
        directory = "C:/Users/rami dob/Downloads/pfe_application - Copy/pfe_application/check_generated"
        files = os.listdir(directory)

        # Check if the directory is empty
        if not files:
            # Display a message saying "No file generated yet"
            no_files_label = QLabel("No files generated yet")
            buttons_layout.addWidget(no_files_label)
        else:
            # Create a button for each file in the directory
            for file_name in files:
                file_path = os.path.join(directory, file_name)
                button = QPushButton(file_name)
                button.clicked.connect(lambda checked, file_path=file_path: self.display_file_content(file_path))
                buttons_layout.addWidget(button)

        splitter.addWidget(files_widget)

        # Right section for QTextEdit
        self.text_edit = QTextEdit()
        self.text_edit.textChanged.connect(self.enable_save_button)  # Connect textChanged signal to enable_save_button slot
        splitter.addWidget(self.text_edit)

        # Set sizes for the sections
        sizes = [self.height() // 3, 2 * (self.height() // 3)]
        splitter.setSizes(sizes)

        # Create button layout for Save Changes and Cancel buttons
        button_layout = QHBoxLayout()
        layout.addLayout(button_layout)

        self.save_button = QPushButton("Save Changes")
        self.save_button.setEnabled(False)  # Initially disabled until changes are made
        self.save_button.clicked.connect(self.save_changes)
        button_layout.addWidget(self.save_button)

        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.close)
        button_layout.addWidget(cancel_button)

    def display_file_content(self, file_path):
        # Read the content of the file
        with open(file_path, "r") as file:
            file_content = file.read()
        
        # Display the content in the QTextEdit
        self.text_edit.setPlainText(file_content)
        self.current_file_path = file_path  # Store the current file path

    def enable_save_button(self):
        # Enable the Save Changes button when text is changed
        self.save_button.setEnabled(True)

    def save_changes(self):
        # Save changes back to the original file
        if hasattr(self, 'current_file_path'):  # Check if a file is currently opened
            file_content = self.text_edit.toPlainText()
            with open(self.current_file_path, "w") as file:
                file.write(file_content)
            self.save_button.setEnabled(False)  # Disable the Save Changes button after saving

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    generate_pom_widget = CheckGeneratedWidget()
    generate_pom_widget.show()
    sys.exit(app.exec_())
