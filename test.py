import javalang

def parse_java_file(file_path):
    with open(file_path, 'r') as file:
        java_code = file.read()
        #print("Java code read successfully:")
        #print(java_code)
    try:
        tree = javalang.parse.parse(java_code)
        #print("Java code parsed successfully.")
    except Exception as e:
        print("Error occurred while parsing Java code:", e)
        tree = None
    return tree

def extract_classes_and_methods(tree):
    classes = []
    if tree is None:
        return classes
    for path, node in tree:
        if isinstance(node, javalang.tree.ClassDeclaration):  # Check for class declaration
            class_name = node.name
            methods = [(method.return_type.name, method.name) for method in node.methods]  # Include return type
            classes.append(("class", class_name, methods))
        elif isinstance(node, javalang.tree.InterfaceDeclaration):  # Check for interface declaration
            interface_name = node.name
            methods = [(method.return_type.name, method.name) for method in node.methods]  # Include return type
            classes.append(("interface", interface_name, methods))
    return classes

if __name__ == "__main__":
    java_file_path = "C:/Users/rami dob/Downloads/pfe_application - Copy/pfe_application/Classes/RootAction.java"
    parsed_tree = parse_java_file(java_file_path)
    classes_and_methods = extract_classes_and_methods(parsed_tree)
    if classes_and_methods:
        for class_type, class_name, methods in classes_and_methods:
            print(f"{class_type.capitalize()}: {class_name}")
            for return_type, method_name in methods:
                print(f"Method: {method_name}, Return Type: {return_type}")
    else:
        print("No classes and methods found.")
