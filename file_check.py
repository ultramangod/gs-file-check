# -*- coding:utf-8 -*-
import re
import json
import mdp_numeric_file_check
import mdp_traits_file_check


def read_json_file(file_name):
    """
    读配置文件
    :param file_name:文件名
    :return:所读配置文件
    """
    fin = open(file_name, "r")
    task_config_json = fin.read()
    return task_config_json


def out_json_file(json_str):
    """
    将结果输出到json文件
    :param json_str:
    :return:None
    """
    out_file_name = "./file_check_result.json"
    out_file = open(out_file_name, "w")
    out_file.write(json_str)
    out_file.close()


def numeric_data_sort(file_name, sorted_file):
    """
    将numeric文件格式规范化
    如果有标题行则删除标题行
    如果左侧为数字列则删除数字列
    任何数据包含引号则删除引号
    :param file_name:输入文件名
    :param sorted_file:格式化后的文件名
    :return:None
    """
    f_in = open(file_name, "r")
    f_out = open(sorted_file, "w")
    file_lines = f_in.readlines()
    for line in file_lines:
        output_line = ""
        now_line = re.split(r'[\s,]+', line.strip())
        if now_line[0].isdigit() and len(now_line[1]) > 1:
            if not now_line[2].isdigit():
                continue
            else:
                for i in range(1, len(now_line)):
                    if now_line[i][0] == "\"" or now_line[i][0] == "\'":
                        output_line += now_line[i][1:len(now_line[i]) - 1]
                        output_line += " "
                    else:
                        output_line += now_line[i]
                        output_line += " "
                f_out.write(output_line + "\n")
        else:
            if not now_line[1].isdigit():
                continue
            else:
                for i in range(0, len(now_line)):
                    if now_line[i][0] == "\"" or now_line[i][0] == "\'":
                        output_line += now_line[i][1:(len(now_line[i]) - 1)]
                        output_line += " "
                    else:
                        output_line += now_line[i]
                        output_line += " "
                f_out.write(output_line + "\n")
    f_in.close()
    f_out.close()


def traits_data_sort(file_name, sorted_file):
    """
    将traits文件格式规范化
    如果有标题行则删除标题行
    如果左侧为数字列则删除数字列
    任何数据包含引号则删除引号
    :param file_name:输入文件名
    :param sorted_file:格式化后的文件名
    :return:None
    """
    f_in = open(file_name, "r")
    f_out = open(sorted_file, "w")
    file_lines = f_in.readlines()
    for line in file_lines:
        output_line = ""
        now_line = re.split(r'[\s,]+', line.strip())
        if file_lines[0].split()[0].isdigit():
            for i in range(1, len(now_line)):
                if now_line[i][0] == "\"" or now_line[i][0] == "\'":
                    string = now_line[i][1:len(now_line[i]) - 1]
                    if string.upper() == "NA" or string.upper() == "NAN":
                        output_line += "NA"
                        output_line += " "
                    else:
                        output_line += string
                        output_line += " "
                else:
                    string = now_line[i]
                    if string.upper() == "NA" or string.upper() == "NAN":
                        output_line += "NA"
                        output_line += " "
                    else:
                        output_line += string
                        output_line += " "
            f_out.write(output_line + "\n")
        else:
            for i in range(0, len(now_line)):
                if now_line[i][0] == "\"" or now_line[i][0] == "\'":
                    string = now_line[i][1:len(now_line[i]) - 1]
                    if string.upper() == "NA" or string.upper() == "NAN":
                        output_line += "NA"
                        output_line += " "
                    else:
                        output_line += string
                        output_line += " "
                else:
                    string = now_line[i]
                    if string.upper() == "NA" or string.upper() == "NAN":
                        output_line += "NA"
                        output_line += " "
                    else:
                        output_line += string
                        output_line += " "
            f_out.write(output_line + "\n")
    f_in.close()
    f_out.close()


def file_march(num_file, traits_file):
    """
    numeric与trait匹配比对
    高于10%则返回true
    否则返回false
    :param num_file:numeric数据文件
    :param traits_file:traits数据文件
    :return:true or false
    """
    fin1 = open(num_file, "r")
    fin2 = open(traits_file, "r")
    num_dict = []
    traits_dict = []
    num_lines = fin1.readlines()
    traits_lines = fin2.readlines()
    count = 0
    for line in num_lines:
        num_dict.append(line.split()[0])
    for i in range(1, len(traits_lines)):
        traits_dict.append(traits_lines[i].split()[0])
    all_num = len(num_dict)
    for name in traits_dict:
        if name in num_dict:
            count += 1
    march_percent = float(count) / all_num
    if march_percent > 0.1:
        return True
    else:
        return False


def file_check(numeric_file, traits_file):
    """
    文件检查函数，查询输入的numeric文件和traits文件格式是否正确
    如遇错误则输入错误详情至file_check_result.json文件
    :param numeric_file:numeric文件
    :param traits_file:traits文件
    :return:格式正确返回true，否则返回false
    """
    output = {}
    output["result"] = False
    output["error_list"] = []
    if not mdp_numeric_file_check.is_text_file(numeric_file):
        error_dict = {
            "title": "mdp_numeric文件格式错误",
            "msg": "文件不是有效txt文件",
            "info": "计算所需文件为txt格式"
        }
        if error_dict not in output["error_list"]:
            output["error_list"].append(error_dict)
    elif not mdp_traits_file_check.is_text_file(traits_file):
        error_dict = {
            "title": "mdp_traits文件格式错误",
            "msg": "文件不是有效的txt文件",
            "info": "计算所需文件为txt格式"
        }
        if error_dict not in output["error_list"]:
            output["error_list"].append(error_dict)
    else:
        numeric_data_sort(numeric_file, "Sorted_numeric.txt")
        traits_data_sort(traits_file, "Sorted_traits.txt")
        if not mdp_numeric_file_check.has_left_title("Sorted_numeric.txt")["result"]:
            error_row = mdp_numeric_file_check.has_left_title("Sorted_numeric.txt")["row"]
            error_dict = {
                "title": "mdp_numeric文件内容格式错误",
                "msg": "数据行第%d行左侧标题不存在" % error_row,
                "info": "数据行左侧标题必须存在"
            }
            if error_dict not in output["error_list"]:
                output["error_list"].append(error_dict)
        if not mdp_numeric_file_check.format_correct("Sorted_numeric.txt")["result"]:
            error_row = mdp_numeric_file_check.format_correct("Sorted_numeric.txt")["row"]
            error_dict = {
                "title": "mdp_numeric文件数据量内容错误",
                "msg": "数据行第%d行数据量个数不同" % error_row,
                "info": "数据行所有数据行数据内容必须相同"
            }
            if error_dict not in output["error_list"]:
                output["error_list"].append(error_dict)
        if not mdp_numeric_file_check.num_correct("Sorted_numeric.txt")["result"]:
            error_row = mdp_numeric_file_check.num_correct("Sorted_numeric.txt")["row"]
            error_column = mdp_numeric_file_check.num_correct("Sorted_numeric.txt")["column"]
            error_dict = {
                "title": "mdp_numeric文件正文数据内容错误",
                "msg": "数据行第%d行%d列数据内容非0,1,2" % (error_row, error_column),
                "info": "数据行正文数据内容必须为0,1,2"
            }
            if error_dict not in output["error_list"]:
                output["error_list"].append(error_dict)
        if not mdp_traits_file_check.has_left_title("Sorted_traits.txt")["result"]:
            error_row = mdp_traits_file_check.has_left_title("Sorted_traits.txt")["row"]
            error_dict = {
                "title": "mdp_traits文件内容格式错误",
                "msg": "数据行第%d行左侧标题不存在" % error_row,
                "info": "数据行左侧标题必须存在"
            }
            if error_dict not in output["error_list"]:
                output["error_list"].append(error_dict)
        if not mdp_traits_file_check.format_correct("Sorted_traits.txt")["result"]:
            error_row=mdp_traits_file_check.format_correct("Sorted_traits.txt")["row"]
            error_dict = {
                "title": "mdp_traits文件内容格式错误",
                "msg": "数据行第%d行第2列不为数值，NAN或NA" % error_row,
                "info": "数据行第2列应为数值，NAN或NA，可以接受引号和大小写"
            }
            if error_dict not in output["error_list"]:
                output["error_list"].append(error_dict)
        if not file_march("Sorted_numeric.txt", "Sorted_traits.txt"):
            error_dict = {
                "title": "mdp_traits文件与mdp_numeric文件匹配错误",
                "msg": "双文件左侧标题匹配度低于10%",
                "info": "双文件左侧标题匹配度必须高于10%"
            }
            if error_dict not in output["error_list"]:
                output["error_list"].append(error_dict)
    if len(output["error_list"]) == 0:
        output["result"] = True
        out_json_file(json.dumps(output, ensure_ascii=False))
        return True
    else:
        out_json_file(json.dumps(output, ensure_ascii=False))
        print "error_msg in file_check_result.json"
        print json.dumps(output, ensure_ascii=False)
        return False


def main():
    """
    读配置信息，检查文件
    :return:
    """
    config_file = "task.gacfg"
    config_json = eval(read_json_file(config_file))
    numeric_file = config_json["genotype_num"]
    traits_file = config_json["phenotype_trait"]
    file_check(numeric_file, traits_file)


main()
