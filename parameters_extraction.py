import os
import xml.etree.ElementTree as ET
import re
DIR_NAME = os.path.dirname(__file__)


tree = ET.parse(os.path.join(DIR_NAME, 'JavaClasses.xml'))
root = tree.getroot()


def list_of_parameter_snipped_code(code):
    return re.findall(r'##\w+##', code)


def justify_xml_file(xml_file):
    tree_xml = ET.parse(xml_file)
    root_xml = tree_xml.getroot()
    xml_string = ET.tostring(root_xml, encoding="utf-8", method="xml").decode()
    lines = xml_string.split('\n')
    lines_without_empty = [line for line in lines if line.strip() != '']
    new_xml_string = '\n'.join(lines_without_empty)

    with open(xml_file, 'w') as file:
        file.write(new_xml_string)
        file.close()


def parameter_xml_file():
    parameters_dict = {}
    
    for class_elem in root.findall("Java/Class"):
        module_name = class_elem.find("ClassName").text
        parameters_dict[module_name] = []
    for class_elem in root.findall("Java/Parent"):
        module_name = class_elem.find("ParentName").text
        parameters_dict[module_name] = []
        
    return parameters_dict





def number_of_parameters():
    modules = list(parameter_xml_file().keys())
    list_modules = []

    for i in range(len(modules)):
        list_modules.append(i)

    return list_modules


def dict_module_name_number():
    module_name_number = {}
    for i in range(len(number_of_parameters())):
        module_name_number[list(parameter_xml_file().keys())[i]] = i
    return module_name_number


def dict_module_name_number_0():
    module_name_number = {}
    for i in range(len(number_of_parameters())):
        module_name_number[list(parameter_xml_file().keys())[i]] = 0
    return module_name_number


def dict_module_name_number_1():
    module_name_number = {}
    for i in range(len(number_of_parameters())):
        module_name_number[list(parameter_xml_file().keys())[i]] = 0
    return module_name_number


dict_add = dict_module_name_number_0()
dict_add_for_more = dict_module_name_number_1()



def dict_module_name_number_add(module_name):
    for j, i in dict_add.items():
        if module_name == j:
            i = i + 1
            dict_add[j] = i
    return dict_add


def dict_module_name_number_add_for_more(module_name):
    for j, i in dict_add_for_more.items():
        if module_name == j:
            i = i + 1
            dict_add_for_more[j] = i
    return dict_add_for_more



list_of_item = []
dict_item = {}


def appending_item_in_list(first_item, end_item):
    list_of_item.append(first_item)
    list_of_item.append(end_item)
    return list_of_item


def appending_item_in_dict(input_list):
    output_dict = {}
    for i in range(0, len(input_list), 2):
        key = input_list[i]
        value = input_list[i + 1]
        if key not in output_dict:
            output_dict[key] = []
            dict_item[key] = []
        output_dict[key].append(value)
        dict_item[key].append(value)
    return output_dict






