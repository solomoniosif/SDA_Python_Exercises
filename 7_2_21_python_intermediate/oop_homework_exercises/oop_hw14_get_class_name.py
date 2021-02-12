
# TODO: Write a Python program to get the class name of an instance in Python.


class GetClassName:
    def __call__(self, instance):
        return self.get_class_name(instance)

    @staticmethod
    def get_class_name(instance):
        return instance.__class__.__name__


if __name__ =='__main__':
    get_class_name = GetClassName()

    print(get_class_name('abc'))
    print(get_class_name(get_class_name))
    print(get_class_name(24))
    print(get_class_name([]))