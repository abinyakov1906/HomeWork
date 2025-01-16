def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])
print_list = ([1, 2, 3], True, "Привет")
print_params(*print_list)
print_dict= {}
print_params(**print_dict)
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)