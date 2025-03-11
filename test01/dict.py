if __name__ == "__main__":
    # create a dictionary
    my_dict = {'apple': 1, 'banana': 2, 'orange': 3}
    # print the dictionary
    print(my_dict)

    # 使用大括号 {} 来创建空字典
    emptyDict = {}

    # 打印字典
    print(emptyDict)

    # 查看字典的数量
    print("Length:", len(emptyDict))

    # 查看类型
    print(type(emptyDict))

    # 向字典中添加元素
    emptyDict['one'] = 1
    emptyDict['two'] = 2
    emptyDict['three'] = 3

    # 打印字典
    print(emptyDict)

    # 访问字典中的元素
    print("Value of 'one':", emptyDict['one'])
    print("Value of 'two':", emptyDict['two'])
    print("Value of 'three':", emptyDict['three'])

    # 修改字典中的元素
    emptyDict['one'] = 100
    emptyDict['two'] = 200
    emptyDict['three'] = 300

    # 打印修改后的字典
    print(emptyDict)

    # 删除字典中的元素
    del emptyDict['one']
    del emptyDict['two']
    del emptyDict['three']

    # 打印删除后的字典
    print(emptyDict)


    age = int(input("请输入你家狗狗的年龄: "))
    print("")
    if age <= 0:
        print("你是在逗我吧!")
    elif age == 1:
        print("相当于 14 岁的人。")
    elif age == 2:
        print("相当于 22 岁的人。")
    elif age > 2:
        human = 22 + (age - 2) * 5
        print("对应人类年龄: ", human)

    ### 退出提示
    input("点击 enter 键退出")
