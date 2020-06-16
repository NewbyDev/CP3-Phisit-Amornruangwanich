def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    while usernameInput != "admin" or passwordInput != "1234":
        print("== Username & Password incorrect, Please Try Again ==")
        usernameInput = input("Username : ")
        passwordInput = input("Password : ")
    showMenu()

def showMenu():
    print("Welcome To System")
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    menuSelect()

def menuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1 :
        vatCalculator()
    elif userSelected == 2 :
        priceCalculator()

def vatCalculator():
    price = int(input("Goods price (THB) :"))
    vat = 7
    result = price + (price * vat / 100)
    print("Final price :", result)
    print("======= Complete =======")
    showMenu()

def priceCalculator():
    price1 = int(input("First Product Price :"))
    price2 = int(input("Second Product Price :"))
    print("Total price :", price1 + price2)
    print("======= Complete =======")
    showMenu()

login()