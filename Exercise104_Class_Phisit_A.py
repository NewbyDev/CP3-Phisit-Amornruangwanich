class customer:
    cusName = ""
    cusLastname = ""
    cusAge = 0

    def addCart(self):
        print("Added product to",self.cusName,self.cusLastname,"'s cart")

customer1 = customer()
customer1.cusName = "Phisit"
customer1.cusLastname = "Amornruangwanich"
customer1.cusAge = 27
customer1.addCart()

customer2 = customer()
customer2.cusName = "Nobita"
customer2.cusLastname = "Nobi"
customer2.cusAge = 15
customer2.addCart()

customer3 = customer()
customer3.cusName = "Doraemon"
customer3.cusLastname = "Dora"
customer3.cusAge = 17
customer3.addCart()

customer4 = customer()
customer4.cusName = "Naruto"
customer4.cusLastname = "Usumaki"
customer4.cusAge = 23
customer4.addCart()
