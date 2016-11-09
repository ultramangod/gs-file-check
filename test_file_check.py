# -*- coding:utf-8 -*-
# 测试文件，逐个测试filecheck对于不同测试用例返回结果
from file_check import *
import pytest


class TestFile:
    def test_numeric_file_type(self):
        assert file_check("file_type_01.7z", "mdp_traits.txt") is False

    def test_first_row(self):
        assert file_check("firstrow_01.txt", "mdp_traits.txt") is True

    def test_numeric_left_column(self):
        assert file_check("left_columnnum_01.txt", "mdp_traits.txt") is True

    def test_numeric_miss_left_title(self):
        assert file_check("miss_lefttitle_01.txt", "mdp_traits.txt") is False

    def test_numeric_mismatch(self):
        assert file_check("mismatch_data_01.txt", "mdp_traits.txt") is False

    def test_numeric_wrong_data(self):
        assert file_check("wrong_data_01.txt", "mdp_traits.txt") is False

    def test_traits_file_type(self):
        assert file_check("mdp_numeric.txt", "file_type_02.7z") is False

    def test_traits_left_column(self):
        assert file_check("mdp_numeric.txt", "left_columnnum_02.txt") is True

    def test_traits_miss_left_title(self):
        assert file_check("mdp_numeric.txt", "miss_lefttitle_02.txt") is False

    def test_traits_wrong_data(self):
        assert file_check("mdp_numeric.txt", "wrong_data_02.txt") is False

    def test_under_percent(self):
        assert file_check("mdp_numeric.txt", "under_10_percent_01.txt") is False

    def test_normal(self):
        assert file_check("mdp_numeric.txt", "mdp_traits.txt") is True


if __name__ == '__main__':
    checklist=["test_file_check.py"]
    pytest.main(checklist)
