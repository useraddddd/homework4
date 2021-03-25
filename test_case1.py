import pytest
import yaml

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    try:a/b
    except:print("error")
    return a/b
#加减乘除用同一组数据，至少有一个用例可通过，或多个
class Test_d:
    def setup_class(self):
        print("计算开始")
    def teardown_class(self):
        print("计算结束")
    def setup(self):
        print("计算开始")
    def teardown(self):
        print("计算结束")

    @pytest.mark.parametrize(["a","b","c"],yaml.safe_load(open("test_data1.yaml")))
    def test_add(self,a,b,c):
        assert add(a,b)==c

    @pytest.mark.parametrize(["a", "b", "c"], yaml.safe_load(open("test_data1.yaml")))
    def test_sub(self,a,b,c):
        assert sub(a,b)==c

    @pytest.mark.parametrize(["a", "b", "c"], yaml.safe_load(open("test_data1.yaml")))
    def test_mul(self,a,b,c):
        assert mul(a,b)==c

    @pytest.mark.parametrize(["a", "b", "c"], yaml.safe_load(open("test_data1.yaml")))
    def test_div(self,a,b,c):
        assert div(a,b)==c