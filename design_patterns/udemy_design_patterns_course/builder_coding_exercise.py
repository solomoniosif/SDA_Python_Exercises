# Implement the Builder design pattern for rendering simple chunks of code.

# Sample use of the builder you are asked to creeate:
# cb = CodeBuilder('Person').add_field('name', '""').add_field('age', '0')
# print(cb)
#
# Expected output:
# class Person:
#     def __init__(self):
#         self.name = ""
#         self.age = 0


class CodeProperty:
    indent_size = 4

    def __init__(self, field_name="", field_value=None):
        self.name = None
        self.field_name = field_name
        self.field_value = field_value
        self.properties = []

    def __str__(self):
        result = f"class {self.name}:\n"
        result += " " * self.indent_size + f"def __init__(self):\n"
        for p in self.properties:
            result += f"{' ' * self.indent_size * 2}self.{p.field_name} = {p.field_value}\n"
        return result


class CodeBuilder:
    __root = CodeProperty()

    def __init__(self, root_name):
        self.root_name = root_name
        self.__root.name = root_name

    def add_field(self, field_name, field_value):
        self.__root.properties.append(CodeProperty(field_name, field_value))
        return self

    def __str__(self):
        return str(self.__root)


cb = CodeBuilder('Person').add_field('name', '""').add_field('age', '0')
print(cb)
