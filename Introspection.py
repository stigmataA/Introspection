def introspection_info(obj):
    obj_type = type(obj).__name__ # определение типа объекта
    attributes = dir(obj) # получение списка атрибутов объекта
    methods = [method for method in attributes if callable(getattr(obj, method))] # получение методов объекта
    module = obj.__class__.__module__ # получение имени модуля объекта
    info = {'type': obj_type, 'attributes': attributes, 'methods': methods, 'module': module} # создание словаря с информацией о объекте

    return info


number_info = introspection_info(42) # получение информации о числе
print(number_info)
string_info = introspection_info('Hello World') # получение информации о строке
print(string_info)
list_info = introspection_info([1, 10, 5.0, 'hello']) # получение информации о списке
print(list_info)
