systemMenu = {"KFC":250,"MK":655,"BURGER":150,"SIZZLER":655}
orderList = []

def showฺBill():
    print(" THAI-CHANA FoodCenter ".center(30,"="))
    print("==== VAT Included ====".center(30, " "))
    print("== ORDER LIST ==".center(30, " "))
    for number in range(len(orderList)):
        print(orderList[number][0],orderList[number][1])
    print("=".center(30,"="))

def totalPrice():
    total = 0
    for i in range(len(orderList)):
        total += orderList[i][1]
    print("Amount :",len(orderList),"orders")
    print("Total :",total)
    userMoney = int(input("Cash :"))
    print("Change :",userMoney - total)
    print(" THANK YOU ".center(30,"="))

while True:
    orderName = input("Please Select Order :").upper()
    if(orderName.lower() == "exit"):
        break
    else:
        orderList.append([orderName,systemMenu[orderName]])

showฺBill()
totalPrice()
