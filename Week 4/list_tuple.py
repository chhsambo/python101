classes_list = [
    "Python Sat-Sun",
    "C/C++ Mon-Fri",
    "C# Weekend"
]
study_hours = (
    "7:00 - 9:00",
    "9:00 - 11:00",
    "13:00 - 15:00",
    "15:00 - 17:00",
    "18:00 - 20:00"
)

classes_list.append("ML with C#")
classes_list[2] = "C# Weekend"

new_classes = {
    classes_list[3]: {
        "day": "Sat-Sun",
        "hour": study_hours[1]
    },
    classes_list[1]: {
        "day": "Mon-Fri",
        "hour": study_hours[3]
    },
}
print(new_classes)

# for _class in new_classes:
#     print(_class)