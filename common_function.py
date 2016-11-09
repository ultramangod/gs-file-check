#!/bin/env python
# coding=UTF-8

import string


def is_text_file(fq_file):
    """
    判断是否为文本文件
    :param fq_file:输入文件名
    :return:
    """
    text_characters = "".join(map(chr, range(32, 127)) + list("\n\r\t\b"))
    _null_trans = string.maketrans("", "")

    input_fq = open(fq_file)
    content = input_fq.read(1024)

    if "\0" in content:
        return False

    if not content:
        return True

    t = content.translate(_null_trans, text_characters)
    if float(len(t))/len(content) > 0.30:
        return False

    input_fq.close()
    return True

