# employees = [
#     {"name": "name_0", "city": "city_0", "employee id": "EMP ID 0"},
#     {"name": "name_1", "city": "city_1", "employee id": "EMP ID 1"},
#     {"name": "name_2", "city": "city_2", "employee id": "EMP ID 2"},
#     {"name": "name_3", "city": "city_3", "employee id": "EMP ID 3"},
#     {"name": "name_4", "city": "city_4", "employee id": "EMP ID 4"},
# ]
#
#
# class Employee(object):
#     def __init__(self, employee) -> None:
#         self._employee = employee
#
#     # This function will make class iterable
#     # and on every iteration we will return name of employee
#     # solution to line 39-43
#     def __getitem__(self, index):
#         if isinstance(index, int):
#             return self._employee[index]["name"]
#         else:
#             for x in self._employee:
#                 if index in x.values():
#                     return x
#             raise IndexError
#
#     # This function will return class attribute
#     # if class attribute not found it will return employee detail
#     # solution to line number 45
#     def __getattr__(self, attribute_name):
#         try:
#             super().__getattr__(attribute_name)
#         except AttributeError:
#             return self[attribute_name]
#
#
# obj = Employee(employees)
#
# print("\n\n")
# for employee in obj:
#     print(employee)  # name_0, name_1 .... name_4
#
# print("\n\n")
# print(obj["name_0"])  # {"name": "name_0", "city": "city_0", "employee id": "EMP ID 0"}
#
# print("\n\n")
# print(obj.name_0["city"])  # city_0
#
# print("\n\n")


for i in range(2, 6):
    num = 1
    for j in range(0, i):
        num = num * i
    print(num)










