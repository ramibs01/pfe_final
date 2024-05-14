import os
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QPushButton, QHBoxLayout, QDialog, QApplication, QMessageBox, QLabel, QLineEdit
from PyQt5.QtGui import QIcon

class GeneratePomWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("Generate your pom.xml")
        self.setWindowIcon(QIcon("Icons_home/Mon projet.png"))

    def init_ui(self):
        layout = QVBoxLayout(self)

        self.text_edit = QTextEdit()
        layout.addWidget(self.text_edit)

        # Create a QHBoxLayout for the buttons
        button_layout = QHBoxLayout()
        layout.addLayout(button_layout)

        # Add the "Generate New pom.xml" button
        self.generate_new_button = QPushButton("Generate New pom.xml")
        self.generate_new_button.clicked.connect(self.generate_new_pom)
        button_layout.addWidget(self.generate_new_button)

        # Add the "Save" button
        save_button = QPushButton("Save")
        save_button.clicked.connect(self.save_pom_file)
        button_layout.addWidget(save_button)

        # Add the "Cancel" button
        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.close)
        button_layout.addWidget(cancel_button)

        # Add stretch to push the buttons to the right
        button_layout.addStretch()

        # Load existing pom.xml file
        self.load_pom_file()

        add_dependency_button = QPushButton("Add Dependency")
        add_dependency_button.clicked.connect(self.add_dependency)
        button_layout.addWidget(add_dependency_button)

    def load_pom_file(self):
        pom_file_path = "C:/Users/rami dob/Downloads/pfe_application - Copy/pfe_application/check_generated/pom.xml"
        if os.path.exists(pom_file_path):
            with open(pom_file_path, "r") as file:
                pom_content = file.read()
                self.text_edit.setPlainText(pom_content)

    def generate_new_pom(self):
        pom_file_path = "C:/Users/rami dob/Downloads/pfe_application - Copy/pfe_application/check_generated/pom.xml"
        if not os.path.exists(pom_file_path):
            # Content of the new generated pom.xml
            pom_content = """<?xml version="1.0"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.jenkins-ci.plugins</groupId>
        <artifactId>plugin</artifactId>
        <version>3.5</version>
    </parent>
    <artifactId>myplugin</artifactId>
    <version>3.7-SNAPSHOT</version>
    <packaging>hpi</packaging>
    <name>Calculate the Sum</name>
    <description>Calculate the sum of two numbers</description>
    <properties>
        <jenkins.version>2.107.3</jenkins.version>
        <java.level>8</java.level>
        <findbugs.failOnError>false</findbugs.failOnError>
    </properties>
    <repositories>
        <repository>
            <id>repo.jenkins-ci.org</id>
            <url>https://repo.jenkins-ci.org/public/</url>
        </repository>
    </repositories>
    <pluginRepositories>
        <pluginRepository>
            <id>repo.jenkins-ci.org</id>
            <url>https://repo.jenkins-ci.org/public/</url>
        </pluginRepository>
    </pluginRepositories>
    <build>
        <plugins>
            <plugin>
                <groupId>org.jenkins-ci.tools</groupId>
                <artifactId>maven-hpi-plugin</artifactId>
                <extensions>true</extensions>
                <configuration>
                    <compatibleSinceVersion>3.0</compatibleSinceVersion>
                </configuration>
            </plugin>
        </plugins>
    </build>
    <dependencies>
        <dependency>
            <groupId>commons-lang</groupId>
            <artifactId>commons-lang</artifactId>
            <version>2.6</version>
        </dependency>
        <dependency>
            <groupId>org.jenkins-ci.plugins</groupId>
            <artifactId>apache-httpcomponents-client-4-api</artifactId>
            <version>4.5.3-2.0</version>
        </dependency>
        <dependency>
            <groupId>org.jenkins-ci.plugins</groupId>
            <artifactId>credentials</artifactId>
            <version>2.1.13</version>
        </dependency>
        <dependency>
            <groupId>org.jenkins-ci.plugins</groupId>
            <artifactId>cloudbees-folder</artifactId>
            <version>6.0.4</version>
        </dependency>
        <dependency>
            <groupId>com.github.tomakehurst</groupId>
            <artifactId>wiremock</artifactId>
            <version>1.58</version>
            <scope>test</scope>
        </dependency>
    </dependencies>
</project>
"""

            # Set the content to the QTextEdit
            self.text_edit.setPlainText(pom_content)

            # Save the content to the new pom.xml file
            with open(pom_file_path, "w") as file:
                file.write(pom_content)

            # Show success message
            QMessageBox.information(self, "Success", "New pom.xml file generated successfully!")

            # Disable the "Generate New pom.xml" button
            self.generate_new_button.setEnabled(False)
        else:
            # Show error message if pom.xml already exists
            QMessageBox.warning(self, "Error", "pom.xml already exists!")

    def save_pom_file(self):
        pom_file_path = "C:/Users/rami dob/Downloads/pfe_application - Copy/pfe_application/check_generated/pom.xml"
        pom_content = self.text_edit.toPlainText()
        with open(pom_file_path, "w") as file:
            file.write(pom_content)
        QMessageBox.information(self, "Success", "pom.xml file saved successfully!")

    def add_dependency(self):
        dependency_dialog = DependencyDialog(self)
        dependency_dialog.exec()

class DependencyDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Add Dependency")
        self.setGeometry(100, 100, 800, 200)

        layout = QVBoxLayout()

        self.group_id_edit = QLineEdit()
        layout.addWidget(QLabel("Group ID:"))
        layout.addWidget(self.group_id_edit)

        self.artifact_id_edit = QLineEdit()
        layout.addWidget(QLabel("Artifact ID:"))
        layout.addWidget(self.artifact_id_edit)

        self.version_edit = QLineEdit()
        layout.addWidget(QLabel("Version:"))
        layout.addWidget(self.version_edit)

        save_button = QPushButton("Save")
        save_button.clicked.connect(self.save_dependency)
        layout.addWidget(save_button)

        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.close)
        layout.addWidget(cancel_button)

        self.setLayout(layout)

    def save_dependency(self):
        group_id = self.group_id_edit.text()
        artifact_id = self.artifact_id_edit.text()
        version = self.version_edit.text()

        # Construct the XML string for the dependency
        dependency_str = f"""
    <dependency>
        <groupId>{group_id}</groupId>
        <artifactId>{artifact_id}</artifactId>
        <version>{version}</version>
    </dependency>
"""

        # Load the pom.xml content from the parent widget
        pom_widget = self.parent()
        pom_content = pom_widget.text_edit.toPlainText()

        # Find the position to insert the dependency
        dependencies_start_idx = pom_content.find("<dependencies>") + len("<dependencies>")
        dependencies_end_idx = pom_content.find("</dependencies>")
        dependencies_str = pom_content[dependencies_start_idx:dependencies_end_idx]

        # Insert the new dependency
        modified_pom_content = pom_content[:dependencies_start_idx] + dependency_str + dependencies_str + pom_content[dependencies_end_idx:]

        # Update the pom.xml content in the parent widget
        pom_widget.text_edit.setPlainText(modified_pom_content)

        self.close()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    generate_pom_widget = GeneratePomWidget()
    generate_pom_widget.show()
    sys.exit(app.exec_())
