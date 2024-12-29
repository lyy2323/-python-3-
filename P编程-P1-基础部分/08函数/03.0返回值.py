def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name("jake", "hendrix")
print(musician)

def get_formatted_name(first_name, last_name, middle_name=""):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name("jake", "hendrix")
print(musician)

def build_person(first_name, last_name, age=None):
    person = {"first": first_name, "last": last_name}
    if age:
        person["age"] = age
    return person
musician = build_person("jimi", "hendrix")
print(musician)
musician = build_person("jake", "henry", age=27)
print(musician)


