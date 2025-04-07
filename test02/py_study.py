

if __name__ == '__main__':

#     a, b = 0,1
#     while a < 1000:
#         print(a,end=' ')
#         a, b = b, a+b
#
#     words = ['cat', 'window', 'defenestrate']
#     for w in words:
#         print(w, len(w))
#
#
# # 创建示例多项集
# users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# # 策略：迭代一个副本
# for user, status in users.copy().items():
#     print(users)
#     print(user, status)
#     if status == 'inactive':
#         del users[user]
#
# # 策略：创建一个新多项集
# active_users = {}
# for user, status in users.items():
#     if status == 'active':
#         active_users[user] = status
#

    # for n in range(2,10):
    #     for x in range(2,n):
    #         if n % x == 0:
    #             print(n, 'equals', x, '*', n//x)
    #             break
    #     else:
    #         # loop fell through without finding a factor
    #         print(n, 'is a prime number')

    # 斐波拉契数列
    def fib(n):
        a, b = 0, 1
        while a < n:
            print(a, end=' ')
            a, b = b, a+b
        print()

    fib(2000)

    def ask_ok(prompt, retries=4, reminder='Please try again!'):
        while True:
            reply = input(prompt)
            if reply in {'y', 'ye', 'yes'}:
                return True
            if reply in {'n', 'no', 'nop', 'nope'}:
                return False
            retries = retries - 1
            if retries < 0:
                raise ValueError('超过次数限制了，大哥！！！！')
            print(reminder)


    # ask_ok('Do you really want to quit?')
    ask_ok('OK to overwrite the file?')