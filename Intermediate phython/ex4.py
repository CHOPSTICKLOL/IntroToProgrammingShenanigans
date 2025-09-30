from getopt import gnu_getopt


def value_changer(gg):
    for key,value in gg.items():
        if value>=90:
            gg[key]="A"
        elif value>=70:
            gg[key]="B"
        elif value>=50:
            gg[key]="C"
        elif value>=30:
            gg[key]="D"
        else:
            gg[key]="horrible"
    return gg
students = {"Alice": 92,"Bob": 78,"Charlie": 55,"David": 89,"Ed": 42,"Frank": 1,}
print(value_changer(students))
