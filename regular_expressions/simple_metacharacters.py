import re

string_list = [
    "spam",
    "spum",
    "spim",
    "sram"
]

string_list1 = [
    "grey",
    "gray",
    "stingray"
]

string_pattern = "sp.m"
string_pattern1 = r"^gr.y$"


def metacharacters(list, pattern):
    for str in list:
        if re.match(pattern, str):
            print("pattern '{1}' matches\t\t'{0}'".format(str, pattern))
        else:
            print("pattern '{1}' doesn't match\t'{0}'".format(str, pattern))

metacharacters(string_list1, string_pattern1)
