# -*- coding:utf-8 -*-
import common_function


def isfloat(number):
    try:
        float(number)
    except ValueError:
        return False
    return True


def is_text_file(filename):
    """
    判断是否为txt文件
    是返回true，否则返回false
    :param filename:文件名
    :return:True or False
    """
    return common_function.is_text_file(filename)


def has_left_title(filename):
    """
    判断左侧标题是否存在
    若是返回return_dict["result"]=true
    否则返回return_dict["result"]=false
    并用return_dict["row"]记录首个错误出错行号
    :param filename:文件名
    :return:return_dict
    """
    fin = open(filename, "r")
    traits_lines = fin.readlines()
    flag = True
    return_dict = {}
    row_num = 0
    for line in traits_lines:
        row_num += 1
        if "." in line.split()[0] or (line.split()[0].isdigit() and len(line.split()[0]) < 3):
            flag = False
            break
    fin.close()
    return_dict["result"] = flag
    return_dict["row"] = row_num
    return return_dict


def format_correct(filename):
    """
    判断数据行第二列是否为数值或NA
    若是返回return_dict["result"]=true
    否则返回return_dict["result"]=false
    并用return_dict["row"]记录首个错误出错行号
    :param filename:文件名
    :return:return_dict
    """
    fin = open(filename, "r")
    traits_lines = fin.readlines()
    flag = True
    return_dict = {}
    row_num = 0
    for i in range(1, len(traits_lines)):
        row_num += 1
        now_line = traits_lines[i].split()
        if not isfloat(now_line[1]) and now_line[1] != "NA":
            flag = False
            break
    fin.close()
    return_dict["result"] = flag
    return_dict["row"] = row_num
    return return_dict
