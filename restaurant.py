# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 16:04:52 2019

@author: Oluwafemi Samuel
@Company: SOLMA AND FEMTECH
"""
from tkinter import*
import time
import random
#Name the Application
myApp = Tk()

#set the geometry/size
myApp.geometry('1400x800+0+0')
#Application title
myApp.title('Restaurant Transaction Manager')

#Set the time
currentTime = time.asctime(time.localtime(time.time()))
#variables
var = StringVar()
operator = ''


#Top of App
up = Frame(myApp, width = 1600, height = 10,bg = 'skyblue', relief = RAISED)
#Info that goes into the top banner
label1_up = Label(up,font=('arial',30,'bold'), text = 'Restaurant Transaction Manager', fg = 'orange', anchor ='w', bd = 10)
label1_up.grid(column = 0, row = 0)
label2_up = Label(up,font = ('arial', 14,'bold'),text =currentTime,fg = 'orange', anchor ='w', bd = 10)
label2_up.grid(row = 1, column = 0 )
#Pack all info in the top
up.pack(side = TOP)

#Left side part of the app
side1 = Frame(myApp, width = 800, height = 700,relief = RIDGE)

#Pack info in side one
side1.pack(side = LEFT)

#Right side part of the app
side2 = Frame(myApp, width = 300, height =700,relief = RAISED)

#Pack info in the right side
side2.pack(side = RIGHT)

#Calcuator

#function definitions
def Clickbutton(x):
    global operator
    operator = operator + str(x)
    var.set(operator)
#
def clearDisplay():
    global operator
    operator = ''
    var.set(operator)
    
    
def Equals():
    global operator
    process = str(eval(operator))
    var.set(process)
    operator = ''
    
    

displayText = Entry(side2, font =('arial', 20,'bold'),
                    textvariable = var,bd = 30, insertwidth =4,bg = 'skyblue',
                    justify = 'right' )
displayText.grid(columnspan = 4)
#set calculator buttons
#Row2 Buttons
button7 = Button(side2,padx =16, pady =16, bd = 8, fg = 'black', font =('arial', 20,'bold'), text = '7',
                 bg = 'skyblue', command = lambda: Clickbutton(7)).grid(row=2,column=0)
button8 = Button(side2,padx =16, pady =16, bd = 8, fg = 'black', font =('arial', 20,'bold'), text = '8',
                 bg = 'skyblue', command = lambda: Clickbutton(8)).grid(row=2,column=1)

button9 = Button(side2,padx =16, pady =16, bd = 8, fg = 'black', font =('arial', 20,'bold'), text = '9',
                 bg = 'skyblue', command = lambda: Clickbutton(9)).grid(row=2,column=2)
minus= Button(side2,padx =16, pady =16, bd = 8, fg = 'black', font =('arial', 20,'bold'), text = '-',
                 bg = 'skyblue', command = lambda: Clickbutton('-')).grid(row=2,column=3)
#row3 buttons

button4 = Button(side2,padx =16, pady =16, bd = 8, fg = 'black', font =('arial', 20,'bold'), text = '4',
                 bg = 'skyblue', command = lambda: Clickbutton(4)).grid(row=3,column=0)
button5 = Button(side2,padx =16, pady =16, bd = 8, fg = 'black', font =('arial', 20,'bold'), text = '5',
                 bg = 'skyblue', command = lambda: Clickbutton(5)).grid(row=3,column=1)

button6 = Button(side2,padx =16, pady =16, bd = 8, fg = 'black', font =('arial', 20,'bold'), text = '6',
                 bg = 'skyblue', command = lambda: Clickbutton(6)).grid(row=3,column=2)
add = Button(side2,padx =16, pady =16, bd = 8, fg = 'black', font =('arial', 20,'bold'), text = '+',
                 bg = 'skyblue', command = lambda: Clickbutton('+')).grid(row=3,column=3)

#row4 buttons

button1 = Button(side2,padx =16, pady =16, bd = 8, fg = 'black', font =('arial', 20,'bold'), text = '1',
                 bg = 'skyblue', command = lambda: Clickbutton(1)).grid(row=4,column=0)
button2 = Button(side2,padx =16, pady =16, bd = 8, fg = 'black', font =('arial', 20,'bold'), text = '2',
                 bg = 'skyblue', command = lambda: Clickbutton(2)).grid(row=4,column=1)

button3 = Button(side2,padx =16, pady =16, bd = 8, fg = 'black', font =('arial', 20,'bold'), text = '3',
                 bg = 'skyblue', command = lambda: Clickbutton(3)).grid(row=4,column=2)
multiply= Button(side2,padx =16, pady =16, bd = 8, fg = 'black', font =('arial', 20,'bold'), text = '*',
                 bg = 'skyblue', command = lambda: Clickbutton('*')).grid(row=4,column=3)
#row5 buttons

button0 = Button(side2,padx =16, pady =16, bd = 8, fg = 'black', font =('arial', 20,'bold'), text = '0',
                 bg = 'skyblue', command = lambda: Clickbutton(0)).grid(row=5,column=0)
clear = Button(side2,padx =16, pady =16, bd = 8, fg = 'black', font =('arial', 20,'bold'), text = 'C',
                 bg = 'skyblue', command = clearDisplay).grid(row=5,column=1)

equals = Button(side2,padx =16, pady =16, bd = 8, fg = 'black', font =('arial', 20,'bold'), text = '=',
                 bg = 'skyblue', command = Equals).grid(row=5,column=2)
divide= Button(side2,padx =16, pady =16, bd = 8, fg = 'black', font =('arial', 20,'bold'), text = '/',
                 bg = 'skyblue', command = lambda: Clickbutton('/')).grid(row=5,column=3)


#side 1 info
#=========================Info about restaurant=====================================
#Variable declaration
Ref = StringVar()
Fries  = StringVar()
Burger = StringVar()
Fillet  = StringVar()
subTotal = StringVar()
Total  = StringVar()
serviceCharge = StringVar()
Drinks  = StringVar()
Tax = StringVar()
Cost  = StringVar()
chickenBurger = StringVar()
cheeseBurger = StringVar()
#==========================1ST ITEM===========================================
label4Ref = Label(side1, font = ('arial', 16,'bold'), text = 'Txn Reference', 
                    bd =16,anchor ='w')
label4Ref.grid(row =0, column =0)
RefText = Entry(side1,font =('arial', 16,'bold'),
                    textvariable = Ref,bd = 10, insertwidth =4,bg = 'skyblue',
                    justify = 'right')
RefText.grid(row =0, column =1)

#===========================2ND ITEM==========================================
label4Fries = Label(side1, font = ('arial', 16,'bold'), text = 'French Fries', 
                    bd =16,anchor ='w')
label4Fries.grid(row =1, column =0)

FriesText = Entry(side1,font =('arial', 16,'bold'),
                    textvariable = Fries, bd = 10, insertwidth =4,bg = 'skyblue',
                    justify = 'right')
FriesText.grid(row =1, column =1)


#==========================3RD ITEM===========================================
label4Burger = Label(side1, font = ('arial', 16,'bold'), text = 'Burger Meal', 
                    bd =16,anchor ='w')
label4Burger.grid(row =2, column =0)
BurgerText = Entry(side1,font =('arial', 16,'bold'),
                    textvariable = Burger,bd = 10, insertwidth =4,bg = 'skyblue',
                    justify = 'right')
BurgerText.grid(row =2, column =1)

#===========================4TH ITEM==========================================
label4Fillet = Label(side1, font = ('arial', 16,'bold'), text = 'Fillet Oat Meal', 
                    bd =16,anchor ='w')
label4Fillet.grid(row =3, column =0)

FilletText = Entry(side1,font =('arial', 16,'bold'),
                    textvariable = Fillet, bd = 10, insertwidth =4,bg = 'skyblue',
                    justify = 'right')
FilletText.grid(row =3, column =1)

#==========================5TH ITEM===========================================
label4chickenBurger = Label(side1, font = ('arial', 16,'bold'), text = 'Chicken Combo', 
                    bd =16,anchor ='w')
label4chickenBurger.grid(row =4, column =0)
chickenBurgerText = Entry(side1,font =('arial', 16,'bold'),
                    textvariable = chickenBurger,bd = 10, insertwidth =4,bg = 'skyblue',
                    justify = 'right')
chickenBurgerText.grid(row =4, column =1)

#===========================6TH ITEM==========================================
label4cheeseBurger = Label(side1, font = ('arial', 16,'bold'), text = 'Mac and Cheese', 
                    bd =16,anchor ='w')
label4cheeseBurger.grid(row =5, column =0)
cheeseBurgerText = Entry(side1,font =('arial', 16,'bold'),
                    textvariable = cheeseBurger,bd = 10, insertwidth =4,bg = 'skyblue',
                    justify = 'right')
cheeseBurgerText.grid(row =5, column =1)

#=========================More Info about restaurant=====================================
#==========================1ST ITEM===========================================
labelDrinks = Label(side1, font = ('arial', 16,'bold'), text = 'Drinks', 
                    bd =16,anchor ='w')
labelDrinks.grid(row =0, column =2)
DrinksText = Entry(side1,font =('arial', 16,'bold'),
                    textvariable = Drinks,bd = 10, insertwidth =4,
                    justify = 'right')
DrinksText.grid(row =0, column =3)

#===========================2ND ITEM==========================================
label4Cost = Label(side1, font = ('arial', 16,'bold'), text = 'Meal Cost', 
                    bd =16,anchor ='w')
label4Cost.grid(row =1, column =2)

CostText = Entry(side1,font =('arial', 16,'bold'),
                    textvariable = Cost, bd = 10, insertwidth =4,
                    justify = 'right', state = 'disabled')
CostText.grid(row =1, column =3)


#==========================3RD ITEM===========================================
label4serviceCharge = Label(side1, font = ('arial', 16,'bold'), text = 'Service charge', 
                    bd =16,anchor ='w')
label4serviceCharge.grid(row =2, column =2)
serviceChargeText = Entry(side1,font =('arial', 16,'bold'),
                    textvariable = serviceCharge,bd = 10, insertwidth =4,
                    justify = 'right', state = 'disabled')
serviceChargeText.grid(row =2, column =3)

#===========================4TH ITEM==========================================
label4Tax = Label(side1, font = ('arial', 16,'bold'), text = 'Sales Tax', 
                    bd =16,anchor ='w')
label4Tax.grid(row =3, column =2)

TaxText = Entry(side1,font =('arial', 16,'bold'),
                    textvariable = Tax, bd = 10, insertwidth =4,
                    justify = 'right', state = 'disabled')
TaxText.grid(row =3, column =3)

#==========================5TH ITEM===========================================
label4subTotal = Label(side1, font = ('arial', 16,'bold'), text = 'Sub Total', 
                    bd =16,anchor ='w')
label4subTotal.grid(row =4, column =2)
subTotalText = Entry(side1,font =('arial', 16,'bold'),
                    textvariable = subTotal,bd = 10, insertwidth =4,
                    justify = 'right', state = 'disabled')
subTotalText.grid(row =4, column =3)

#===========================6TH ITEM==========================================
label4Total = Label(side1, font = ('arial', 16,'bold'), text = 'Total', 
                    bd =16,anchor ='w')
label4Total.grid(row =5, column =2)
TotalText = Entry(side1,font =('arial', 16,'bold'),
                    textvariable = Total,bd = 10, insertwidth =4,
                    justify = 'right', state = 'disabled')
TotalText.grid(row =5, column =3)
#============================Button Functions===========================
def GenRef(): #This function will also process the calculations
    x = random.randint(12900, 80921)
    x = str(x)
    Ref.set(x)
    #Get the number of items customer wants first
    fries_cost  = float(Fries.get())
    burger_cost = float(Burger.get())
    fillet_cost  = float(Fillet.get())
    drinks_cost  = float(Drinks.get()) 
    chickenBurger_cost = float(chickenBurger.get())
    cheeseBurger_cost = float(cheeseBurger.get())
    
    #Set the default price of each food item or drink
    updated_fries_cost  = fries_cost * 10.99
    updated_burger_cost = burger_cost * 11
    updated_fillet_cost  = fillet_cost * 8.99
    updated_drinks_cost  = drinks_cost * 4.99 
    updated_chickenBurger_cost = chickenBurger_cost * 12.99
    updated_cheeseBurger_cost = cheeseBurger_cost * 7.99
    
    updated_Cost  = '$' + (str('%.2f' %(updated_fries_cost+updated_burger_cost+
                                     updated_fillet_cost+updated_drinks_cost+
                                     updated_chickenBurger_cost+updated_cheeseBurger_cost)))
    applicableTax = (0.32 * (updated_fries_cost+updated_burger_cost+
                                     updated_fillet_cost+updated_drinks_cost+
                                     updated_chickenBurger_cost+updated_cheeseBurger_cost))
    
    formated_applicableTax = '$' + (str('%.2f' %(applicableTax)))
    
    cal_serviceCharge = ((updated_fries_cost+updated_burger_cost+
                                     updated_fillet_cost+updated_drinks_cost+
                                     updated_chickenBurger_cost+updated_cheeseBurger_cost)/99)
    
    formated_cal_serviceCharge = '$' + (str('%.2f' %(cal_serviceCharge)))
    
    cal_subTotal = (updated_fries_cost+updated_burger_cost+
                                     updated_fillet_cost+updated_drinks_cost+
                                     updated_chickenBurger_cost+updated_cheeseBurger_cost)
    
    formated_cal_subTotal = '$' + (str('%.2f' %(cal_subTotal)))
    
    cal_Total = (cal_serviceCharge + applicableTax + cal_subTotal)
    formated_cal_Total = '$' + (str('%.2f' %(cal_Total)))
    Cost.set(updated_Cost)
    Tax.set(formated_applicableTax)
    serviceCharge.set(formated_cal_serviceCharge)
    subTotal.set(formated_cal_subTotal)
    Total.set(formated_cal_Total)
    '''
    subTotal = 
    Total  = '''
    
    
    
    
def queueExit():
    myApp.destroy()

def Reset():
    Ref.set('')
    Fries.set('')
    Burger.set('')
    Fillet.set('')
    subTotal.set('')
    Total.set('')
    serviceCharge.set('')
    Drinks.set('')
    Tax.set('')
    Cost.set('')
    chickenBurger.set('')
    cheeseBurger.set('')
    
    
#==================Buttons==============================================
totalButton = Button(side1, padx =16, pady = 8, bd = 16, fg = 'black',font = ('arial', 16,'bold'),
                     width = 10, text = 'Total', bg = 'skyblue', command = GenRef )
totalButton.grid(row = 7, column = 1 )

resetButton = Button(side1, padx =16, pady = 8, bd = 16, fg = 'black',font = ('arial', 16,'bold'),
                     width = 10, text = 'Reset', bg = 'skyblue', command = Reset )
resetButton.grid(row = 7, column = 2 )

exitButton = Button(side1, padx =16, pady = 8, bd = 16, fg = 'black',font = ('arial', 16,'bold'),
                     width = 10, text = 'Exit', bg = 'skyblue', command = queueExit )
exitButton.grid(row = 7, column = 3 )
#Run the loop
myApp.mainloop()

