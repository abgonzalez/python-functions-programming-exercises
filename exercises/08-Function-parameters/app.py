# Your code goes here:
def render_person(name: str, dob: str, colour: str, age: str, gender: str):
    result=''
    if name:
        result += name
    if age:
        result += f' is a {age} years old '
    if gender:
        result += f'{gender} '
    if dob:
        result += f'born in {dob} '
    if colour:
        result += f'with {colour} eyes'
    return result


# Do not edit below this line
print(render_person('ax','b','c','d','e'))
print(render_person('Bob', '05/22/1983', 'green', 23, 'male'))