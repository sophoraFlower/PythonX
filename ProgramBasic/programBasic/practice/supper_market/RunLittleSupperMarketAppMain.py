import math

from ProgramBasic.programBasic.practice.supper_market.person.Customer_ import Customer
from ProgramBasic.programBasic.practice.supper_market.supportMarket_.LittleSuperMarket_ import LittleSuperMarket
from ProgramBasic.programBasic.practice.supper_market.supportMarket_.Merchandise_ import Merchandise
import random


def main():
    # 创建商品数据
    merchandise_list = []
    for i in range(200):
        merchandise = Merchandise("商品" + str(i), "ID00" + str(i), 200,
                                  random.random() * 200, (random.random() + 1) * 200)
        merchandise_list.append(merchandise)
    # 售出商品数据
    merchandise_sold_list = []
    # 创建超市对象
    superMaket = LittleSuperMarket("有家超市", "世纪大道666号", 200, 0, merchandise_list, merchandise_sold_list)

    print("超市开门啦！")
    print("本店叫做" + superMaket.superMarketName)
    print("本店地址" + superMaket.address)
    print("共有停车位" + str(superMaket.parkingCount) + "个")
    print("今天的营业额为" + str(superMaket.incomingSum))
    print("共有商品" + str(len(superMaket.merchandises)) + "种")

    # 创建顾客对象
    customer = Customer("顾客编号" + str(math.floor(random.random() * 10000)), (random.random()+1) * 1000,
                        random.random() > 0.5)
    # 开车的顾客
    if customer.is_drive_car:
        if superMaket.parkingCount > 0:
            print("欢迎" + customer.name + "驾车而来。本店已经为您安排了车位，停车免费哦。车位编号为" + str(superMaket.parkingCount))
            superMaket.parkingCount -= 1
        else:
            print("不好意思，本店车位已满。欢迎您下次光临")
    else:
        print("欢迎" + customer.name + "光临本店")

    # 顾客开始在超市中消费
    total_cost = 0
    print("超市营业吗？，请输入是或者否\n")
    if input() == "是":
        is_open = True
    else:
        is_open = False
    while is_open:
        print("本店提供" + str(len(superMaket.merchandises)) + "种商品，欢迎选购。请输入商品编号")
        merchandise_id = input("请输入商品编号")
        if int(merchandise_id) < 0:
            break
        if int(merchandise_id) >= len(superMaket.merchandises):
            print("本店没有这种商品，请叙述编号在0到" + str(len(superMaket.merchandises) - 1) + "之内的商品编号。")
            continue
        merchandise = merchandise_list[int(merchandise_id)]
        print("你选购的商品名： " + merchandise.name + " 该商品价格： " + str(merchandise.sold_price) + " 您的购买数量？")
        to_but_number = int(input())
        if to_but_number < 0:
            print("傻逼啊～，请输入正确的数量！！！")
            continue
        if to_but_number > merchandise.count:
            print("土豪啊～鄙店没这么多啊！！！")
            continue
        if (to_but_number * merchandise.sold_price + total_cost) > customer.money:
            print("穷逼～滚 😡")
            continue
        total_cost += to_but_number * merchandise.sold_price
        merchandise.count -= to_but_number
        merchandise_sold = Merchandise(merchandise.name, merchandise_id, to_but_number,
                                       merchandise.purchase_price, merchandise.sold_price)
        superMaket.merchandiseSold.append(merchandise_sold)

        customer.money -= total_cost
        if customer.is_drive_car:
            superMaket.parkingCount += 1
        print("顾客:" + customer.name + "的消费总额： " + str(total_cost))
        superMaket.incomingSum += total_cost

        print("还继续营业吗？")
        if input() == "是":
            is_open = True
        else:
            is_open = False
        print("超市关门了！")
        print("今天总的营业额为" + str(superMaket.incomingSum) + "。营业情况如下：")

    for i in range(len(superMaket.merchandiseSold)):
        merch = superMaket.merchandiseSold
        sold_num = merch[i].count
        if sold_num > 0:
            incomming = merch[i].sold_price * sold_num
            net_incomming = (merch[i].sold_price - merch[i].purchase_price) * sold_num
            print("该商品的价格： " + str(merch[i].purchase_price) + "和" + str(merch[i].sold_price))
            print(merch[i].name + "售出了" + str(sold_num) + "个。销售额为" + str(incomming) + "。净利润为" + str(net_incomming))


main()
