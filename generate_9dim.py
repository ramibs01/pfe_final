import os

class GenerateWidget:
    def __init__(self, dropped_items, directory):
        self.dropped_items = dropped_items
        self.directory = directory

    def generate_java_file(self):
        # Check if RootAction and RunAction2 are present in the dropped items
        if "RootAction" in self.dropped_items and "RunAction2" in self.dropped_items:
            # Define the package name and imports
            java_code = "package org.jenkins.ci.plugins.jobimport;\n\n"
            java_code += "import hudson.Extension;\n"
            java_code += "import hudson.model.RootAction;\n"
            java_code += "import hudson.model.Run;\n"
            java_code += "import jenkins.model.RunAction2;\n\n"
            
            # Define the class with the required annotations and methods
            java_code += "@Extension\n"
            java_code += "public class MyPlugin implements RootAction, RunAction2 {\n\n"
            java_code += "\tprivate transient Run run;\n\n"
            java_code += "\t@Override\n"
            java_code += "\tpublic void onAttached(Run<?, ?> run) {\n"
            java_code += "\t\tthis.run = run;\n"
            java_code += "\t}\n\n"
            java_code += "\t@Override\n"
            java_code += "\tpublic void onLoad(Run<?, ?> run) {\n"
            java_code += "\t\tthis.run = run;\n"
            java_code += "\t}\n\n"
            java_code += "\tpublic Run getRun() {\n"
            java_code += "\t\treturn run;\n"
            java_code += "\t}\n\n"
            java_code += "\t@Override\n"
            java_code += "\tpublic String getIconFileName() {\n"
            java_code += "\t\treturn \"headshot.png\";\n"
            java_code += "\t}\n\n"
            java_code += "\t@Override\n"
            java_code += "\tpublic String getUrlName() {\n"
            java_code += "\t\treturn \"myplugin\";\n"
            java_code += "\t}\n\n"
            java_code += "\t@Override\n"
            java_code += "\tpublic String getDisplayName() {\n"
            java_code += "\t\treturn \"My Plugin\";\n"
            java_code += "\t}\n\n"
            java_code += "}\n"

            # Write the generated Java code to a file
            file_path = os.path.join(self.directory, "MyPlugin.java")
            with open(file_path, "w") as java_file:
                java_file.write(java_code)
            
            print(f"Java file '{file_path}' generated successfully.")
        else:
            print("Required items not found in the dropped items.")
