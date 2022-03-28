"""
 * Project name(项目名称)：Python__call__方法
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/28 
 * Time(创建时间)： 13:38
 * Version(版本): 1.0
 * Description(描述)： 
 """


class C:
    def __call__(self, name):
        print("调用__call__()方法", name)


if __name__ == '__main__':
    c = C()
    c("hello")
    c.__call__("hello")
