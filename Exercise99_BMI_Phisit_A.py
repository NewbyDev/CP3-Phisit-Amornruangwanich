from tkinter import *
import math

def leftClickButton(event):
    BMI_Index = float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)
    print("BMI Index : ",BMI_Index)
    if BMI_Index >= 30.0 :
        labelResult.configure(text = "อ้วนมาก เสี่ยงต่อโรค คุมอาหารและออกกำลังกาย")
    elif BMI_Index >= 25.0 :
        labelResult.configure(text = "เริ่มอ้วน คุมอาหารและออกกำลังกาย")
    elif BMI_Index >= 23.0 :
        labelResult.configure(text = "น้ำหนักเกิน ลดน้ำหนักเพื่อสุขภาพที่ดี")
    elif BMI_Index >= 18.6 :
        labelResult.configure(text = "น้ำหนักปกติ เหมาะสม")
    elif BMI_Index <=18.5 :
        labelResult.configure(text = "ผอมเกินไป ควรทานอาหารให้เพียงพอ" )

MainWindow = Tk()
#ทำ lebel กับ box ของ ส่วนสูง
labelHeight = Label(MainWindow,text = "ส่วนสูง (cm.)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)
#ทำ lebel กับ box ของ น้ำหนัก
labelWeight = Label(MainWindow,text = "น้ำหนัก (Kg.)")
labelWeight.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
#ทำ lebel กับ box ของการคำนวน
calculateButton = Button(MainWindow,text = "คำนวน")
calculateButton.bind('<Button-1>',leftClickButton)
calculateButton.grid(row=2)
labelResult = Label(MainWindow,text = "ผลลัพธ์")
labelResult.grid(row=2,column=1)
MainWindow.mainloop()