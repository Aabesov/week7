# regex #
# регулярные выражения #

import re

# match #

# text = "I love arsen@mail.ru BISKEK! love"

# x = re.match("I", text)
# print(x.group(0))

# search #

# x = re.search("love", text)
# print(x.group(0))

# x = re.search(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", text)
# print(x.group())

# x = re.findall("w", text)
# print(x)

# спящий, бичи

# with open("pushkin.txt", "r") as file:
#     x = re.findall("спящий",  file.read())
#     print(x)

# text = "I love arsen@mail.ru BISKEK! love"

# split() #
# x = re.split("lo", text, maxsplit=1)
# print(x)

# x = re.sub("lo | ve", "hh", text)
# print(x)


# with open("pushkin.txt", 'r') as file:
#     x = re.findall(r"\+996\(5{2}[0-9]\)[-]+[0-9]{3}-+[0-9]{3}", file.read())
#     s = re.sub("-", " ", ", ".join(x))
#     nums = open("number.txt", 'w')
#     nums.write(s)
#     nums.close()



