from common_function import *


def isfloat(str):
    try:
        float(str)
    except ValueError:
        return False
    return True


def Is_Text_File(filename):
    return isTextFile(filename)


def Has_Left_Title(filename):
    fin = open(filename, "r")
    traits_lines = fin.readlines()
    flag = True
    for line in traits_lines:
        if "." in line.split()[0] or (line.split()[0].isdigit() and len(line.split()[0]) < 3):
            flag = False
            break
    fin.close()
    return flag


def Format_Correct(filename):
    fin = open(filename, "r")
    traits_lines = fin.readlines()
    flag = True
    for i in range(1, len(traits_lines)):
        nowline = traits_lines[i].split()
        if not isfloat(nowline[1]) and nowline[1] != "NA":
            flag = False
            break
    fin.close()
    return flag
