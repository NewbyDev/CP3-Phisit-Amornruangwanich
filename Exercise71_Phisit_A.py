menuList = []
priceList = []

def showฺBill():
    print("---- My Food ----")
    for number in range(len(menuList)):
        print(menuList[number],priceList[number])

def totalPrice():
    total = 0
    for number in range(len(priceList)) :
        total += priceList[number]
    print("Total :", total)



while True:
    menuName = input("Please Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = int(input("Price :"))
        menuList.append(menuName)
        priceList.append(menuPrice)

showฺBill()
totalPrice()



