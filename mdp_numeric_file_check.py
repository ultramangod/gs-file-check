from common_function import *

def Is_Text_File(filename):
    isTextFile(filename)

def Has_Left_Title(filename):
    fin = open(filename, "r")
    numeric_lines = fin.readlines()
    flag = True
    for line in numeric_lines:
        if len(line.split()[0]) < 2:
            flag = False
            break
    fin.close()
    return flag

def Format_Correct(filename):
    fin = open(filename, "r")
    numeric_lines = fin.readlines()
    flag = True
    rowlen= len(numeric_lines[0].split())
    for line in numeric_lines:
        if len(line.split()) != rowlen:
            flag = False
            break
    fin.close()
    return flag

def Num_Correct(filename):
    fin = open(filename, "r")
    numeric_lines = fin.readlines()
    flag = True
    for line in numeric_lines:
        nowline=line.split()
        for i in range(1, len(nowline)):
            if nowline[i] != "0" and nowline[i] != "1" and nowline[i] != "2":
                flag=False
                break
    return flag



