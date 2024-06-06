#商品列表
product = {"apple": 2, "pear": 3, "peach": 4, "orange": 5}
#新建空白购物车
shopping_cart = {}

#选择菜单
def menu():
    print("—" * 100, "分割线")
    print("请选择序号进行对应操作")
    print("0 退出系统")
    print("1 查看商品列表")
    print("2 加入购物车")
    print("3 查看当前购物车")
    print("4 清空购物车")
    print("5 结算购物车")
    print("6 查看余额")
    choice = int(input("请选择："))
    return choice

#选择功能
try:
    # 新建初始资金
    money = int(input("输入启动资金"))

    while True:
        choice = menu()
        #0 退出系统
        if choice == 0:
            print("已退出系统")
            break

        #1 查看商品列表
        elif choice == 1:
            print("当前商品列表：", product)

        #2 加入购物车
        elif choice == 2:
            choice_thing = input("需要加入的商品名称：")
            choice_thing_number = int(input("输入该商品数量："))
            if choice_thing in product:
                if choice_thing not in shopping_cart:
                    shopping_cart[choice_thing] = product[choice_thing]
                    shopping_cart[choice_thing] = choice_thing_number
                    print("已成功")
                else:
                    price = choice_thing_number * product[choice_thing] + shopping_cart[choice_thing]
                    choice_thing_number = choice_thing_number + shopping_cart[choice_thing]
                    shopping_cart[choice_thing] = choice_thing_number
            else:
                print("不存在该商品，请联系管理员添加")

        #3 查看当前购物车
        elif choice == 3:
            print("当前购物车:{}，".format(shopping_cart))

        #4 清空购物车
        elif choice == 4:
            del shopping_cart
            print("已清理完毕，当前购物车空空如也，快去挑选喜欢的商品吧")

        #5 结算购物车
        elif choice == 5:
            list1 = []
            for key11 in shopping_cart:
                price1 = shopping_cart[key11] * product[key11]
                list1.append(price1)
                total = int(sum(list1))
            print("总计", total, "元")

        #6 查看余额
        elif choice == 6:
            balance = money - total
            if balance < 0:
                print("余额不足，请充值")
                break
            else:
                print("当前余额", balance, "元")

        else:
            print("违规输入，已重置")

except:
    print("输入有问题，请重新")

#文件保存
with open("C:/Users/ABCDE/PycharmProjects/Project1/商品信息管理系统.txt", "w", encoding="UTF-8") as file:
    file.write(str(shopping_cart))
