from file_check import *
import pytest
class TestFile:
    def test_numericfiletype(self):
        assert file_check("file_type_01.7z", "mdp_traits.txt") == False

    def test_firstrow(self):
        assert file_check("firstrow_01.txt", "mdp_traits.txt") == True

    def test_numericleftcolumn(self):
        assert file_check("left_columnnum_01.txt", "mdp_traits.txt") == True

    def test_numericmisslefttitle(self):
        assert file_check("miss_lefttitle_01.txt", "mdp_traits.txt") == False

    def test_numericmismatch(self):
        assert file_check("mismatch_data_01.txt", "mdp_traits.txt") == False

    def test_numericwrongdata(self):
        assert file_check("wrong_data_01.txt", "mdp_traits.txt") == False

    def test_traitsfiletype(self):
        assert file_check("mdp_numeric.txt", "file_type_02.7z") == False

    def test_traitsleftcolumn(self):
        assert file_check("mdp_numeric.txt", "left_columnnum_02.txt") == True

    def test_traitsmisslefttitle(self):
        assert file_check("mdp_numeric.txt", "miss_lefttitle_02.txt") == False

    def test_traitswrongdata(self):
        assert file_check("mdp_numeric.txt", "wrong_data_02.txt") == False

    def test_underpercent(self):
        assert file_check("mdp_numeric.txt", "under_10_percent_01.txt") == False

    def test_normal(self):
        assert file_check("mdp_numeric.txt", "mdp_traits.txt") == True


if __name__ == '__main__':
    checklist=["test_file_check.py"]
    pytest.main(checklist)