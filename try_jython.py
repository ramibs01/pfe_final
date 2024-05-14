from com.squareup.javapoet import JavaFile, MethodSpec, TypeSpec, TypeName
from parameters_extraction import dict_item

def generate_java_class():
    method1 = MethodSpec.methodBuilder("method1").returns(TypeName.VOID).addStatement("System.out.println('Method 1')").build()
    my_class = TypeSpec.classBuilder("MyClass").addMethod(method1).build()
    java_file = JavaFile.builder("com.example", my_class).build()
    java_code = java_file.toString()
    print(java_code)
    print(dict_item)
if __name__ == "__main__":
    generate_java_class()

