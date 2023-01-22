import re

def f1(t):
    data = re.findall(r'(\w+)\s+(is)\s+(\d+)', t)
    family_members = {name: int(age) for name, _, age in data}
    sorted_family_members = dict(sorted(family_members.items()))
    return sorted_family_members

def f2(d):
    total_age = sum(d.values())
    return total_age


print(f2(f1("Mark is 24 and Ann is 27")))
print(f2(f1("Peter is 11, Barbara is 7 and their grandfather John is 103!!")))
print(f1("Mark is 24 and Ann is 27"))
print(f1("Peter is 11, Barbara is 7 and their grandfather John is 103!!"))