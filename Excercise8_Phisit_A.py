username = input("Username :")
password = input("Password :")
if username == "newby" and password == "1234" :
    print("===== Welcome To GitHub Online Shopping =====")
    print("************** Product List *****************")
    print("1. Meat : 120 THB/Kg ")
    print("2. Milk :  20 THB/btl")
    print("3. Cake :  80 THB/pcs")
    print("-------------- Enjoy Shopping ---------------")
    amountproduct = int(input("Key amount of product you want to buy (1-3) :"))
    if amountproduct <1 or amountproduct>3 :
        print("======== ERROR =========")
        print("    We have 3 product   ")
        print("====== TRY AGAIN =======")
    elif amountproduct == 1:
        userselected = int(input("Select product in list :"))
        if userselected == 1:
            quantity = int(input("Quantity :"))
            result = 120 * quantity
            print("Meat price :", result, "THB")
            print("======= Complete ==========")
        elif userselected == 2:
            quantity = int(input("Quantity :"))
            result = 20 * quantity
            print("Milk price :", result, "THB")
            print("======= Complete ==========")
        elif userselected == 3:
            quantity = int(input("Quantity :"))
            result = 80 * quantity
            print("Cake price :", result, "THB")
            print("======= Complete ==========")
    elif amountproduct >1 and amountproduct<3 :
        userselected1 = int(input("First product :"))
        userselected2 = int(input("Second product:"))
        if userselected1 == 1 and userselected2 == 2:
            quantity1 = int(input("Meat quantity :"))
            quantity2 = int(input("Milk quantity :"))
            meatPrice = 120 * quantity1
            milkPrice = 20 * quantity2
            result2 = meatPrice + milkPrice
            print("Meat Price :", meatPrice, "THB")
            print("Milk Price :", milkPrice, "THB")
            print("Total      :", result2, "THB")
            print("========== Complete ==========")
        elif userselected1 == 1 and userselected2 == 3:
            quantity1 = int(input("Meat quantity :"))
            quantity2 = int(input("Cake quantity :"))
            meatPrice = 120 * quantity1
            cakePrice = 80 * quantity2
            result2 = meatPrice + cakePrice
            print("Meat Price :", meatPrice, "THB")
            print("Cake Price :", cakePrice, "THB")
            print("Total      :", result2, "THB")
            print("========== Complete ==========")
        elif userselected1 == 2 and userselected2 == 3:
            quantity1 = int(input("Milk quantity :"))
            quantity2 = int(input("Cake quantity :"))
            milkPrice = 20 * quantity1
            cakePrice = 80 * quantity2
            result2 = milkPrice + cakePrice
            print("Milk Price :", milkPrice, "THB")
            print("Cake Price :", cakePrice, "THB")
            print("Total      :", result2, "THB")
            print("========== Complete ==========")
        elif userselected1 == 3 and userselected2 == 2:
            quantity1 = int(input("Cake quantity :"))
            quantity2 = int(input("Milk quantity :"))
            cakePrice = 80 * quantity1
            milkPrice = 20 * quantity2
            result2 = milkPrice + cakePrice
            print("Milk Price :", milkPrice, "THB")
            print("Cake Price :", cakePrice, "THB")
            print("Total      :", result2, "THB")
            print("========== Complete ==========")
        elif userselected1 == 3 and userselected2 == 1:
            quantity1 = int(input("Cake quantity :"))
            quantity2 = int(input("Meat quantity :"))
            cakePrice = 80 * quantity1
            meatPrice = 120 * quantity2
            result2 = cakePrice + meatPrice
            print("Cake Price :", cakePrice, "THB")
            print("Meat Price :", meatPrice, "THB")
            print("Total      :", result2, "THB")
            print("========== Complete ==========")
        elif userselected1 == 2 and userselected2 == 1:
            quantity1 = int(input("Milk quantity :"))
            quantity2 = int(input("Meat quantity :"))
            milkPrice = 20 * quantity1
            meatPrice = 120 * quantity2
            result2 = milkPrice + meatPrice
            print("Milk Price :", milkPrice, "THB")
            print("Meat Price :", meatPrice, "THB")
            print("Total      :", result2, "THB")
            print("========== Complete ==========")
    elif amountproduct == 3:
        meatQuantiy = int(input("Meat quantity :"))
        milkQuantity = int(input("Milk quantity :"))
        cakeQuantiy = int(input("Cake quantity :"))
        meatPrice = 120 * meatQuantiy
        milkPrice = 20 * milkQuantity
        cakePrice = 80 * cakeQuantiy
        result3 = meatPrice + milkPrice + cakePrice
        print("Meat Price :", meatPrice, "THB")
        print("Milk Price :", milkPrice, "THB")
        print("Cake Price :", cakePrice, "THB")
        print("Total      :", result3, "THB")
        print("========== Complete ==========")

else :
    print("============= ERROR =============")
    print("Username & Password incorrect !!!")
    print("======== PLEASE TRY AGAIN =======")



