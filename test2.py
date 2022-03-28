"""
 * Project name(项目名称)：Python__call__方法
 * Package(包名): 
 * File(文件名): test2
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/28 
 * Time(创建时间)： 13:44
 * Version(版本): 1.0
 * Description(描述)： 
 """


class C:
    a = 1

    def __init__(self):
        self.name = "张三"
        self.sex = "男"

    def f1(self):
        print("hello")


if __name__ == '__main__':
    c = C()
    if hasattr(c, "a"):
        print(hasattr(c.a, "__call__"))
    print()
    if hasattr(c, "name"):
        print(hasattr(c.name, "__call__"))
    if hasattr(c, "sex"):
        print(hasattr(c.sex, "__call__"))
    print()
    if hasattr(c, "f1"):
        print(hasattr(c.f1, "__call__"))
