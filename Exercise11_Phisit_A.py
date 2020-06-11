userInput = int(input("Input number :"))
for i in range(userInput) :
    for x in range(userInput-i):
        print(" ",end="")
    for y in range(i*2+1) :
        print("*",end="")
    print()