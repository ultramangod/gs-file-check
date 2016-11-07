# -*- coding:utf-8 -*-
import re
import json
import mdp_numeric_file_check
import mdp_traits_file_check


def read_json_file(file_name):
    fin = open(file_name, "r")
    task_config_json = fin.read()
    return task_config_json


def out_json_file(json_str):
    out_file_name = "./file_check_result.json"
    out_file = open(out_file_name, "w")
    out_file.write(json_str)
    out_file.close()


def numericData_Sort(file, sortedfile):
    fin = open(file, "r")
    fout = open(sortedfile, "w")
    filelines = fin.readlines()
    for line in filelines:
        outputline = ""
        nowline = re.split(r'[\s\,]+', line.strip())
        if nowline[0].isdigit() and len(nowline[1]) > 1:
            if not nowline[2].isdigit():
                continue
            else:
                for i in range(1, len(nowline)):
                    if nowline[i][0] == "\"" or nowline[i][0] == "\'":
                        outputline += nowline[i][1:len(nowline[i]) - 1]
                        outputline += " "
                    else:
                        outputline += nowline[i]
                        outputline += " "
                fout.write(outputline + "\n")
        else:
            if not nowline[1].isdigit():
                continue
            else:
                for i in range(0, len(nowline)):
                    if nowline[i][0] == "\"" or nowline[i][0] == "\'":
                        outputline += nowline[i][1:(len(nowline[i]) - 1)]
                        outputline += " "
                    else:
                        outputline += nowline[i]
                        outputline += " "
                fout.write(outputline + "\n")
    fin.close()
    fout.close()


def traitsData_Sort(file, sortedfile):
    fin = open(file, "r")
    fout = open(sortedfile, "w")
    filelines = fin.readlines()
    for line in filelines:
        outputline = ""
        nowline = re.split(r'[\s\,]+', line.strip())
        if filelines[0].split()[0].isdigit():
            for i in range(1, len(nowline)):
                if nowline[i][0] == "\"" or nowline[i][0] == "\'":
                    str = nowline[i][1:len(nowline[i]) - 1]
                    if str.upper() == "NA" or str.upper() == "NAN":
                        outputline += "NA"
                        outputline += " "
                    else:
                        outputline += str
                        outputline += " "
                else:
                    str = nowline[i]
                    if str.upper() == "NA" or str.upper() == "NAN":
                        outputline += "NA"
                        outputline += " "
                    else:
                        outputline += str
                        outputline += " "
            fout.write(outputline + "\n")
        else:
            for i in range(0, len(nowline)):
                if nowline[i][0] == "\"" or nowline[i][0] == "\'":
                    str = nowline[i][1:len(nowline[i]) - 1]
                    if str.upper() == "NA" or str.upper() == "NAN":
                        outputline += "NA"
                        outputline += " "
                    else:
                        outputline += str
                        outputline += " "
                else:
                    str = nowline[i]
                    if str.upper() == "NA" or str.upper() == "NAN":
                        outputline += "NA"
                        outputline += " "
                    else:
                        outputline += str
                        outputline += " "
            fout.write(outputline + "\n")
    fin.close()
    fout.close()


def file_march(numfile, traitsfile):
    fin1 = open(numfile, "r")
    fin2 = open(traitsfile, "r")
    numdict = []
    traitsdict = []
    numlines = fin1.readlines()
    traitslines = fin2.readlines()
    count = 0
    for line in numlines:
        numdict.append(line.split()[0])
    for i in range(1, len(traitslines)):
        traitsdict.append(traitslines[i].split()[0])
    All = len(numdict)
    for name in traitsdict:
        if (name in numdict):
            count = count + 1
    march_percent = float(count) / All
    if march_percent > 0.1:
        return True
    else:
        return False


def check_error_case():
    numeric_file = "mdp_numeric.txt"
    traits_file = "mdp_traits.txt"
    numeric_list = ["file_type_01.7z", "firstrow_01.txt", "left_columnnum_01.txt", "miss_lefttitle_01.txt",
                    "mismatch_data_01.txt", "wrong_data_01.txt"]
    traits_list = ["file_type_02.7z", "left_columnnum_02.txt", "miss_lefttitle_02.txt", "wrong_data_02.txt",
                   "under_10_percent_01.txt"]
    output = {}
    output["result"] = False
    output["error_list"] = []
    for numeric in numeric_list:
        if not mdp_numeric_file_check.isTextFile(numeric):
            errordict = {
                "title": "mdp_numeric文件格式错误",
                "msg": "文件不是有效txt文件",
                "info": "计算所需文件为txt格式"
            }
            if errordict not in output["error_list"]:
                output["error_list"].append(errordict)
            continue
        numericData_Sort(numeric, "Sorted_numeric.txt")
        traitsData_Sort(traits_file, "Sorted_traits.txt")
        if not mdp_numeric_file_check.Has_Left_Title("Sorted_numeric.txt"):
            errordict = {
                "title": "mdp_numeric文件内容格式错误",
                "msg": "左侧标题不存在",
                "info": "左侧标题必须存在"
            }
            if errordict not in output["error_list"]:
                output["error_list"].append(errordict)
        if not mdp_numeric_file_check.Format_Correct("Sorted_numeric.txt"):
            errordict = {
                "title": "mdp_numeric文件数据量内容错误",
                "msg": "数据行数据量个数不同",
                "info": "所有数据行数据内容必须相同"
            }
            if errordict not in output["error_list"]:
                output["error_list"].append(errordict)
        if not mdp_numeric_file_check.Num_Correct("Sorted_numeric.txt"):
            errordict = {
                "title": "mdp_numeric文件正文数据内容错误",
                "msg": "正文数据内容非0,1,2",
                "info": "正文数据内容必须为0,1,2"
            }
            if errordict not in output["error_list"]:
                output["error_list"].append(errordict)
        if not mdp_traits_file_check.Has_Left_Title("Sorted_traits.txt"):
            errordict = {
                "title": "mdp_traits文件内容格式错误",
                "msg": "左侧标题不存在",
                "info": "左侧标题必须存在"
            }
            if errordict not in output["error_list"]:
                output["error_list"].append(errordict)
        if not mdp_traits_file_check.Format_Correct("Sorted_traits.txt"):
            errordict = {
                "title": "mdp_traits文件内容格式错误",
                "msg": "第二行不为数值，NAN或NA",
                "info": "第二行应为数值，NAN或NA，可以接受引号和大小写"
            }
            if errordict not in output["error_list"]:
                output["error_list"].append(errordict)
        if not file_march("Sorted_numeric.txt", "Sorted_traits.txt"):
            errordict = {
                "title": "mdp_traits文件与mdp_numeric文件匹配错误",
                "msg": "双文件左侧标题匹配度低于10%",
                "info": "双文件左侧标题匹配度必须高于10%"
            }
            if errordict not in output["error_list"]:
                output["error_list"].append(errordict)
    for traits in traits_list:
        if not mdp_traits_file_check.Is_Text_File(traits):
            errordict = {
                "title": "mdp_traits文件格式错误",
                "msg": "文件不是有效的txt文件",
                "info": "计算所需文件为txt格式"
            }
            if errordict not in output["error_list"]:
                output["error_list"].append(errordict)
            continue
        numericData_Sort(numeric_file, "Sorted_numeric.txt")
        traitsData_Sort(traits, "Sorted_traits.txt")
        if not mdp_numeric_file_check.Has_Left_Title("Sorted_numeric.txt"):
            errordict = {
                "title": "mdp_numeric文件内容格式错误",
                "msg": "左侧标题不存在",
                "info": "左侧标题必须存在"
            }
            if errordict not in output["error_list"]:
                output["error_list"].append(errordict)
        if not mdp_numeric_file_check.Format_Correct("Sorted_numeric.txt"):
            errordict = {
                "title": "mdp_numeric文件数据量内容错误",
                "msg": "数据行数据量个数不同",
                "info": "所有数据行数据内容必须相同"
            }
            if errordict not in output["error_list"]:
                output["error_list"].append(errordict)
        if not mdp_numeric_file_check.Num_Correct("Sorted_numeric.txt"):
            errordict = {
                "title": "mdp_numeric文件正文数据内容错误",
                "msg": "正文数据内容非0,1,2",
                "info": "正文数据内容必须为0,1,2"
            }
            if errordict not in output["error_list"]:
                output["error_list"].append(errordict)
        if not mdp_traits_file_check.Has_Left_Title("Sorted_traits.txt"):
            errordict = {
                "title": "mdp_traits文件内容格式错误",
                "msg": "左侧标题不存在",
                "info": "左侧标题必须存在"
            }
            if errordict not in output["error_list"]:
                output["error_list"].append(errordict)
        if not mdp_traits_file_check.Format_Correct("Sorted_traits.txt"):
            errordict = {
                "title": "mdp_traits文件内容格式错误",
                "msg": "第二行不为数值，NAN或NA",
                "info": "第二行应为数值，NAN或NA，可以接受引号和大小写"
            }
            if errordict not in output["error_list"]:
                output["error_list"].append(errordict)
        if not file_march("Sorted_numeric.txt", "Sorted_traits.txt"):
            errordict = {
                "title": "mdp_traits文件与mdp_numeric文件匹配错误",
                "msg": "双文件左侧标题匹配度低于10%",
                "info": "双文件左侧标题匹配度必须高于10%"
            }
            if errordict not in output["error_list"]:
                output["error_list"].append(errordict)
    out_json_file(json.dumps(output, ensure_ascii=False))


def file_check(numericfile, traitsfile):
    output = {}
    output["result"] = False
    output["error_list"] = []
    if not mdp_numeric_file_check.isTextFile(numericfile):
        errordict = {
            "title": "mdp_numeric文件格式错误",
            "msg": "文件不是有效txt文件",
            "info": "计算所需文件为txt格式"
        }
        if errordict not in output["error_list"]:
            output["error_list"].append(errordict)
    elif not mdp_traits_file_check.Is_Text_File(traitsfile):
        errordict = {
            "title": "mdp_traits文件格式错误",
            "msg": "文件不是有效的txt文件",
            "info": "计算所需文件为txt格式"
        }
        if errordict not in output["error_list"]:
            output["error_list"].append(errordict)
    else:
        numericData_Sort(numericfile, "Sorted_numeric.txt")
        traitsData_Sort(traitsfile, "Sorted_traits.txt")
        if not mdp_numeric_file_check.Has_Left_Title("Sorted_numeric.txt"):
            errordict = {
                "title": "mdp_numeric文件内容格式错误",
                "msg": "左侧标题不存在",
                "info": "左侧标题必须存在"
            }
            if errordict not in output["error_list"]:
                output["error_list"].append(errordict)
        if not mdp_numeric_file_check.Format_Correct("Sorted_numeric.txt"):
            errordict = {
                "title": "mdp_numeric文件数据量内容错误",
                "msg": "数据行数据量个数不同",
                "info": "所有数据行数据内容必须相同"
            }
            if errordict not in output["error_list"]:
                output["error_list"].append(errordict)
        if not mdp_numeric_file_check.Num_Correct("Sorted_numeric.txt"):
            errordict = {
                "title": "mdp_numeric文件正文数据内容错误",
                "msg": "正文数据内容非0,1,2",
                "info": "正文数据内容必须为0,1,2"
            }
            if errordict not in output["error_list"]:
                output["error_list"].append(errordict)
        if not mdp_traits_file_check.Has_Left_Title("Sorted_traits.txt"):
            errordict = {
                "title": "mdp_traits文件内容格式错误",
                "msg": "左侧标题不存在",
                "info": "左侧标题必须存在"
            }
            if errordict not in output["error_list"]:
                output["error_list"].append(errordict)
        if not mdp_traits_file_check.Format_Correct("Sorted_traits.txt"):
            errordict = {
                "title": "mdp_traits文件内容格式错误",
                "msg": "第二行不为数值，NAN或NA",
                "info": "第二行应为数值，NAN或NA，可以接受引号和大小写"
            }
            if errordict not in output["error_list"]:
                output["error_list"].append(errordict)
        if not file_march("Sorted_numeric.txt", "Sorted_traits.txt"):
            errordict = {
                "title": "mdp_traits文件与mdp_numeric文件匹配错误",
                "msg": "双文件左侧标题匹配度低于10%",
                "info": "双文件左侧标题匹配度必须高于10%"
            }
            if errordict not in output["error_list"]:
                output["error_list"].append(errordict)
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
    config_file = "task.gacfg"
    config_json = eval(read_json_file(config_file))
    numeric_file = config_json["genotype_num"]
    traits_file = config_json["phenotype_trait"]
    file_check(numeric_file, traits_file)


check_error_case()
