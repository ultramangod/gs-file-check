# -*- coding:utf-8 -*-
# numeric文件检查模块
import common_function


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
    numeric_lines = fin.readlines()
    flag = True
    return_dict = {}
    row_num = 0
    for line in numeric_lines:
        row_num += 1
        if len(line.split()[0]) < 2:
            flag = False
            break
    fin.close()
    return_dict["result"] = flag
    return_dict["row"] = row_num
    return return_dict


def format_correct(filename):
    """
    判断文件每行数据量是否相同
    若是返回return_dict["result"]=true
    否则返回return_dict["result"]=false
    并用return_dict["row"]记录首个错误出错行号
    :param filename:文件名
    :return:return_dict
    """
    return_dict = {}
    fin = open(filename, "r")
    numeric_lines = fin.readlines()
    flag = True
    row_len = len(numeric_lines[0].split())
    row_num = 0
    for line in numeric_lines:
        row_num += 1
        if len(line.split()) != row_len:
            flag = False
            break
    fin.close()
    return_dict["result"] = flag
    return_dict["row"] = row_num
    return return_dict


def num_correct(filename):
    """
    判断数据行是否为0,1,2
    判断文件每行数据量是否相同
    若是返回return_dict["result"]=true
    否则返回return_dict["result"]=false
    并用return_dict["row"]记录首个错误出错行号
    :param filename:文件名
    :return:return_dict
    """
    fin = open(filename, "r")
    numeric_lines = fin.readlines()
    return_dict = {}
    flag = True
    row_num = 0
    for line in numeric_lines:
        row_num += 1
        column_num = 1
        now_line = line.split()
        column_num += 1
        for i in range(1, len(now_line)):
            if now_line[i] != "0" and now_line[i] != "1" and now_line[i] != "2":
                flag = False
                break
        else:
            continue
        break
    fin.close()
    return_dict["result"] = flag
    return_dict["row"] = row_num
    return_dict["column"] = column_num
    return return_dict
