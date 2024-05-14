import os
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QPushButton, QFileDialog, QHBoxLayout, QLabel, QLineEdit, QDialog, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap

class BasicJellyFormatDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Basic .jelly Format")
        self.setGeometry(100, 100, 600, 400)
        self.setWindowIcon(QIcon("Icons_home/jelly-removebg-preview.png"))

        layout = QVBoxLayout(self)

        basic_jelly_text = """
        <j:jelly xmlns:j="jelly:core" xmlns:l="/lib/layout" xmlns:st="jelly:stapler">
            <l:layout title="">
                <l:side-panel> 
                </l:side-panel>
                <l:main-panel>
                </l:main-panel>
            </l:layout>
            <script>
            </script>
        </j:jelly>
        """

        text_edit = QTextEdit()
        text_edit.setPlainText(basic_jelly_text)
        text_edit.setReadOnly(True)

        layout.addWidget(text_edit)

class AboutDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.setWindowTitle("About")
        self.setGeometry(100, 100, 400, 300)
        self.setWindowIcon(QIcon("Icons_home/jelly-removebg-preview.png"))

    def init_ui(self):
        layout = QVBoxLayout(self)

        image_label = QLabel(self)
        pixmap = QPixmap("Icons_home/jenkins3.png")
        image_label.setPixmap(pixmap)
        layout.addWidget(image_label)

class GenerateJellyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("Generate your index.jelly")
        self.setWindowIcon(QIcon("Icons_home/jelly-removebg-preview.png"))

    def init_ui(self):
        layout = QVBoxLayout(self)

        # Create a QHBoxLayout to contain the buttons and the QTextEdit
        buttons_textedit_layout = QHBoxLayout()

        # Create a QVBoxLayout for the buttons
        buttons_layout = QVBoxLayout()

        # Add buttons for each XML tag
        button_info = {"<j:jelly>": "Add jelly tag", "<l:layout>": "Add layout tag",
                       "<l:side-panel>": "Add side-panel tag", "<l:main-panel>": "Add main-panel tag",
                       "<script>": "Add script tag"}
        for text, action in button_info.items():
            button = QPushButton(action)
            button.clicked.connect(lambda checked, text=text: self.insert_tag(text))
            buttons_layout.addWidget(button)

        # Add stretch to push the buttons to the top of the layout
        buttons_layout.addStretch()

        # Add the buttons layout to the buttons_textedit_layout
        buttons_textedit_layout.addLayout(buttons_layout)

        # Create the QTextEdit
        self.text_edit = QTextEdit()
        buttons_textedit_layout.addWidget(self.text_edit)

        # Add the buttons_textedit_layout to the main layout
        layout.addLayout(buttons_textedit_layout)

        # Load existing jelly file
        self.load_jelly_file()

        # Create button layout for Save and Cancel buttons
        button_layout = QHBoxLayout()
        layout.addLayout(button_layout)

        save_button = QPushButton("Save")
        save_button.clicked.connect(self.save_jelly_file)
        button_layout.addWidget(save_button)

        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.close)
        button_layout.addWidget(cancel_button)

        # Add "Basic .jelly format" button
        basic_jelly_button = QPushButton("Basic .jelly format")
        basic_jelly_button.clicked.connect(self.show_basic_jelly_format)
        layout.addWidget(basic_jelly_button)

        # Add "About" button
        about_button = QPushButton("About")
        about_button.clicked.connect(self.show_about_dialog)
        layout.addWidget(about_button)

        # Add "Generate Empty index.jelly" button
        generate_empty_button = QPushButton("Generate Empty index.jelly")
        generate_empty_button.clicked.connect(self.generate_empty_jelly)
        layout.addWidget(generate_empty_button)

        # Disable all buttons initially
        #self.disable_buttons()

    def load_jelly_file(self):
        # Load existing jelly file if it exists
        pom_file_path = "C:/Users/rami dob/Downloads/pfe_application - Copy/pfe_application/check_generated/index.jelly"
        if os.path.exists(pom_file_path):
            with open(pom_file_path, "r") as file:
                pom_content = file.read()
                self.text_edit.setPlainText(pom_content)

    def save_jelly_file(self):
        pom_file_path = "C:/Users/rami dob/Downloads/pfe_application - Copy/pfe_application/check_generated/index.jelly"
        pom_content = self.text_edit.toPlainText()
        with open(pom_file_path, "w") as file:
            file.write(pom_content)
        self.close()

    def insert_tag(self, tag):
        cursor = self.text_edit.textCursor()
        if tag == "<j:jelly>":
            cursor.insertText(tag + "\n\n</j:jelly>")
        elif tag.startswith("<l:"):
            closing_tag = "</" + tag[1:]
            cursor.insertText(tag + "\n\n" + closing_tag)
        elif tag == "<script>":
            cursor.insertText(tag + "\n\n</script>")
        else:
            cursor.insertText(tag)

    def show_basic_jelly_format(self):
        dialog = BasicJellyFormatDialog()
        dialog.exec_()

    def show_about_dialog(self):
        dialog = AboutDialog()
        dialog.exec_()

    def generate_empty_jelly(self):
        # Generate an empty index.jelly file
        pom_file_path = "C:/Users/rami dob/Downloads/pfe_application - Copy/pfe_application/check_generated/index.jelly"
        if not os.path.exists(pom_file_path):
            # Create an empty file
            open(pom_file_path, 'a').close()
            QMessageBox.information(self, "Success", "Empty index.jelly file generated successfully!")
            # Enable all buttons after generating the file
            self.enable_buttons()
        else:
            QMessageBox.warning(self, "Error", "index.jelly already exists!")

    def disable_buttons(self):
        # Disable all buttons except "Generate Empty index.jelly"
        for button in self.findChildren(QPushButton):
            if button.text() != "Generate Empty index.jelly":
                button.setEnabled(False)

    def enable_buttons(self):
        # Enable all buttons
        for button in self.findChildren(QPushButton):
            button.setEnabled(True)
