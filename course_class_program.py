import course_class as cc

class1 = cc.Course("Advanced Python", 125468, 25, "MIS4322")

class2 = cc.Course("Database Development", 985474, 40, "MIS4340")


# Create a dictionary with CRN as key and capacity

course_dict = {}


def add_to_dict(Course_obj):
    course_dict[Course_obj.get_CRN] = Course_obj.get_capacity


print(course_dict)


# I'm not sure if this works but i hope so!!!
