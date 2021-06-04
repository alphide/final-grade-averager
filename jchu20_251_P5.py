# Name: Jonathan Chu
# Project 5
# Due Date: 4/25/2021
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.

def grades_to_str(grades):
    temp = ''
    # iterates through tuple pairs of grades
    for i, v in grades.items():
        # adds on the key and the value to temp
        temp += i + ': ' + str(v) + '\n'

    return temp


def projects_weighted_avg(grades):
    new_list = []

    for i in sorted(grades['Projects']):
        new_list.append(i)

    temp = []
    # multiplies lowest grades by half of the weight and adds it to temp list
    for i in new_list[0:2]:
        x = i * 0.2
        temp.append(x)
    # multiplies the rest of the grades accordingly
    for i in new_list[2:]:
        y = i * 0.4
        temp.append(y)

    return sum(temp) / (0.2 * len(new_list[0:2]) + 0.4 * len(new_list[2:]))


def homeworks_weighted_avg(grades):
    new_list = []

    for i in sorted(grades['Homeworks']):
        new_list.append(i)
    # removes the lowest grade from sorted list
    new_list.remove(new_list[0])

    return sum(new_list) / len(new_list)


def zybooks_weighted_avg(grades):

    new_list = []

    for i in sorted(grades['zyBooks']):
        new_list.append(i)
    # removes lowest two grades from sorted list
    del new_list[0:2]

    return sum(new_list) / len(new_list)


def quiz_weighted_avg(grades):
    new_list = []

    for i in sorted(grades['Quizzes']):
        new_list.append(i)
    # removes lowest two grades from sorted list
    del new_list[0:2]

    return sum(new_list) / len(new_list)


def compute_final_grade(grades):
    # creates new list and computes the weight of grades
    new_list = [0.4 * projects_weighted_avg(grades), 0.07 * homeworks_weighted_avg(grades),
                0.05 * zybooks_weighted_avg(grades), 0.1 * quiz_weighted_avg(grades),
                0.13 * max(grades['Midterm'], grades['Final']), 0.25 * grades['Final']
                ]

    overall_grade = 0
    # iterates through the list and adds the values to overall_grade
    for i in new_list:
        overall_grade += i

    return overall_grade


def convert_string_to_float(lists):
    # new function to convert string to float
    new_list = []

    for i in lists:
        new_list.append(float(i))

    return new_list


def read_grades_file(filename):

    # dict that initializes list
    dict = {'Name': None,
            'Projects': [],
            'Homeworks': [],
            'zyBooks': [],
            'Quizzes': [],
            'Midterm': [],
            'Final': []
            }

    with open(filename, 'r') as grades_file:
        lines = grades_file.readlines()
        # sets dict keys to file lines
        dict['Name'] = lines[0].strip()
        dict['Projects'] = convert_string_to_float(lines[1].split())
        dict['Homeworks'] = convert_string_to_float(lines[2].split())
        dict['zyBooks'] = convert_string_to_float(lines[3].split())
        dict['Quizzes'] = convert_string_to_float(lines[4].split())
        dict['Midterm'] = float(lines[5])
        dict['Final'] = float(lines[6])

    return dict


def write_grades_file(filename, grades):

    with open(filename, 'w') as f:
        # writes the dict values to a file
        f.write(grades['Name'] + '\n')
        f.write(' '.join([str(i) for i in grades['Projects']]) + ' \n')
        f.write(' '.join([str(i) for i in grades['Homeworks']]) + ' \n')
        f.write(' '.join([str(i) for i in grades['zyBooks']]) + ' \n')
        f.write(' '.join([str(i) for i in grades['Quizzes']]) + ' \n')
        f.write(str(grades['Midterm']) + '\n')
        f.write(str(grades['Final']))

