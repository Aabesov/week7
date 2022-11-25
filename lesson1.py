# frozenset #

# set
# set_a = [1, 2, 3, 4, "buble"]
# set_b = frozenset(set_a)
# print(type(set_b))

# zip #

# list1 = ["apple", "banana"]
# list2 = ["tomato", "potato"]
# print(dict(zip(list1, list2)))

# рекурсия #

# number = int(input("Vvedite chislo: "))
#
# def reqursion_counter(number):
#     if number == 0:
#         return number
#     else:
#         print(number)
#         return reqursion_counter(number - 1)
#
# print(reqursion_counter(number))


# number = int(input("Vvedite chislo: "))
#
# def get_factor(number):
#     if number == 1:
#         return 1
#     else:
#         return number * get_factor(number - 1)
#
# print(get_factor(number))

# num_list = [1, 2, 3, 5, 7]
#
#
# def recursion_sum(lists):
#     if lists == []:
#         return 0
#     else:
#         get_result = recursion_sum(lists[1:])
#         summ = get_result + lists[0]
#         return summ
#
#
# print(recursion_sum(num_list))

# json #

import json
with open("test.json", "r") as file:
    new_dict = json.load(file)
new_dict["name"] = "Aziz"
new_dict["age"] = 20
new_dict["is_18"] = True
with open("test.json", "w") as file:
    text_json = json.dumps(new_dict, indent=4)
    print(text_json)
    file.write(text_json)

