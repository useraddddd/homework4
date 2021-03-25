import pytest
import yaml

def division(a, b):
    try:
        a / b
    except:
        print("除数与被除数error")
    return a/b
class Test_division:
    def setup_class(self):
        print("**方法开始**")
    def teardown_class(self):
        print("**方法结束**")
    @pytest.mark.parametrize(["a","b"],yaml.safe_load(open("test_data.yaml",encoding='utf-8')))
    def test_d(self,a,b):
        a:int
        b:int
        c:float
        c = division(a,b)
        if(0<a<101 and type(a)==int and type(b)==int and 0<b<101 and type(c) == float and 0<c<101):
            assert a/b==c
        else:
            assert False