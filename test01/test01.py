# 快速排序算法
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]  # 选择中间元素作为基准
        left = [x for x in arr if x < pivot]  # 小于基准的元素
        middle = [x for x in arr if x == pivot]  # 等于基准的元素
        right = [x for x in arr if x > pivot]  # 大于基准的元素
        return quick_sort(left) + middle + quick_sort(right)

# 单词翻转
def reverse_words(input):
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    input_words = input.split(" ")

    # 翻转字符串
    # 假设列表 list = [1,2,3,4],
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    input_words = input_words[-1::-1]

    # 重新组合字符串
    output = ' '.join(input_words)

    return output


# 示例使用
if __name__ == "__main__":
    unsorted_array = [3, 6, 8, 10, 1, 2, 1]
    sorted_array = quick_sort(unsorted_array)
    print("排序前的数组:", unsorted_array)
    print("排序后的数组:", sorted_array)

    input = 'I like runoob'
    rw = reverse_words(input)
    print(rw)

    input_words = input.split(" ")
    print(input_words)
    input_words = input_words[-1::-1]

    num_str = '123456789'


    print(num_str)  # 输出字符串
    print(num_str[0:-1])  # 输出第一个到倒数第二个的所有字符
    print(num_str[0])  # 输出字符串第一个字符
    print(num_str[2:5])  # 输出从第三个开始到第六个的字符（不包含）
    print(num_str[2:])  # 输出从第三个开始后的所有字符
    print(num_str[1:5:2])  # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
    print(num_str * 2)  # 输出字符串两次
    print(num_str + '你好')  # 连接字符串

    print('------------------------------')

    print('hello\nrunoob')  # 使用反斜杠(\)+n转义特殊字符
    print(r'hello\nrunoob')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义
    # 不换行输出
    print('hello', end=" ")
    print('runoob')

    print('-')

    import sys

    print('================Python import mode==========================')
    print('命令行参数为:')
    for i in sys.argv:
        print(i)
    print('\n python 路径为', sys.path)


    print('==========================================')
    x = b"hello"
    y = x[1:3]  # 切片操作，得到 b"el"
    z = x + b"world"  # 拼接操作，得到 b"helloworld"
    print(x)
    print(y)
    print(z)






