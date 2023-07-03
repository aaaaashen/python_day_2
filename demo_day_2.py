#python输出的方式
#1.使用%输出
name = "凤凰院凶真"
number = 8
print("我是天才的疯狂科学家，%s,我们实验室有%d个labman"%(name,number))
#2.使用.format输出
print("我是天才的疯狂科学家，{},我们实验室有{}个labman".format(name,number))
#python输入的方式
#1.使用input输入
name = input("你的名字是？")
number = input("你的实验室有几个labman?")
number = int(number)#由于所有输入的input内容都默认是str，所以有时候需要转化为int
print("我是天才的疯狂科学家，%s,我们实验室有%d个labman"%(name,number))