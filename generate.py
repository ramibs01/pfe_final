import os
from test import parse_java_file, extract_classes_and_methods
from parameters_extraction import dict_item

class GenerateWidget:
    def __init__(self, directory):
        self.directory = directory

    def generate_java_file(self):
        for main_item, linked_items in dict_item.items():
            java_content = self.generate_java_content(main_item, linked_items)
            self.write_to_file(main_item, java_content)

    def generate_java_content(self, main_item, linked_items):
        processed_linked_items = [item[:-2] for item in linked_items]  # Exclude last two letters from each linked item
        linked_interfaces = ', '.join(processed_linked_items)
        
        # Check if RootAction is part of linked items
        if "RootAction" in linked_interfaces:
            import_statement = "import hudson.model.RootAction;"
        else:
            import_statement = ""
        
        # Extract methods from RootAction.java only if RootAction is part of linked items
        if "RootAction" in linked_interfaces:
            root_action_methods = self.extract_root_action_methods()
            methods_content = "\n".join(root_action_methods)
        else:
            methods_content = ""
        
        java_content = f'''
    package check_generated;

    {import_statement}

    import hudson.Extension;

    @Extension
    public class {main_item} implements {linked_interfaces} {{
        // Implement the methods of the interfaces
    {methods_content}
    }}
    '''
        return java_content



    def extract_root_action_methods(self):
        # Parse RootAction.java and extract methods
        java_file_path = "C:/Users/rami dob/Downloads/pfe_application - Copy/pfe_application/Classes/RootAction.java"
        parsed_tree = parse_java_file(java_file_path)
        classes_and_methods = extract_classes_and_methods(parsed_tree)
        
        # Find methods for RootAction interface
        root_action_methods = []
        for class_type, class_name, methods in classes_and_methods:
            if class_name == "RootAction":
                for return_type, method_name in methods:
                    root_action_methods.append(f"@Override\n    public {return_type} {method_name}() {{\n return null;    // Complete the return statement\n    }}")
        
        return root_action_methods

    def write_to_file(self, main_item, content):
        file_name = f'{main_item}.java'
        file_path = os.path.join(self.directory, file_name)
        with open(file_path, 'w') as file:
            file.write(content)

            


