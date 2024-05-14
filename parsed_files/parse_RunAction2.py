from antlr4 import *
from JavaInterfaceLexer import JavaInterfaceLexer
from JavaInterfaceParser import JavaInterfaceParser

class JavaInterfaceListener(ParseTreeListener):
    def __init__(self):
        self.interface_name = None
        self.methods = []

    def enterInterfaceDeclaration(self, ctx:JavaInterfaceParser.InterfaceDeclarationContext):
        self.interface_name = ctx.IDENTIFIER().getText()

    def enterInterfaceMethod(self, ctx:JavaInterfaceParser.InterfaceMethodContext):
        method_name = ctx.IDENTIFIER().getText()
        self.methods.append(method_name)

def parse_java_interface(file_path):
    lexer = JavaInterfaceLexer(FileStream(file_path))
    stream = CommonTokenStream(lexer)
    parser = JavaInterfaceParser(stream)
    tree = parser.compilationUnit()

    listener = JavaInterfaceListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    return listener.interface_name, listener.methods

if __name__ == '__main__':
    java_file_path = 'C:/Users/rami dob/Downloads/pfe_application - Copy/pfe_application/Classes/RunAction2.java'  # Update with the path to your Java file
    interface_name, methods = parse_java_interface(java_file_path)
    
    print("Interface Name:", interface_name)
    print("Methods:", methods)

