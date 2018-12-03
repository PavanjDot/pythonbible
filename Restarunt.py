from tkinter import*
import random
import time;

root = Tk()
root.geometry("1600x800+0+0")
root.title ("Resturant manegment system")

text_Input = StringVar ()
operator = " "


Tops = Frame(root, width = 1600, height = 50, bg="powder blue", relief = SUNKEN)
Tops.pack(side = TOP)

f1= Frame(root, width = 800, height = 700,  bg="powder blue", relief = SUNKEN)
f1.pack(side = LEFT)

f2 = Frame(root, width = 300, height = 700,  bg="powder blue", relief = SUNKEN)
f2.pack(side = RIGHT)

#=====================Time==========================================
localtime=time.asctime (time.localtime(time.time()))

#=====================Info=====================================================================
lblInfo = Label (Tops, font=('arial', 50, 'bold'), text = "Restaurant Manegment System", fg="Steel Blue", bd=10, anchor='w')
lblInfo.grid(row=0,column=0)
lblInfo = Label (Tops, font=('arial', 20, 'bold'), text = localtime, fg="Steel Blue", bd=10, anchor='w')
lblInfo.grid(row=1,column=0)

#===================calculator================================================
def btnClick(numbers):
    global operator
    operator= operator + str(numbers)
    text_Input.set(operator)


def btnClearDisplay():
     global operator
     operator = " "
     text_Input.set(" ")


def btnEqualsInput ():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator=" "
    
         
txtDisplay = Entry(f2, font=('arial', 20, 'bold'), textvariable = text_Input, bd=30, insertwidth=4,
                               bg="powder blue", justify='right')

txtDisplay.grid(columnspan=4)

btn7=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
                       text="7" , bg="powder blue", command = lambda: btnClick(7)).grid(row=2, column=0)

btn8=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
                       text="8" , bg="powder blue", command = lambda: btnClick(8)).grid(row=2, column=1)

btn9=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
                       text="9" , bg="powder blue", command = lambda: btnClick(9)).grid(row=2, column=2)


Addition=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
                       text="+" , bg="powder blue", command = lambda: btnClick("+")).grid(row=2, column=3)
#===================================================================================
btn4=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
                       text="4" , bg="powder blue", command = lambda: btnClick(4)).grid(row=3, column=0)
btn5=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
                       text="5" , bg="powder blue", command = lambda: btnClick(5)).grid(row=3, column=1)
btn6=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
                       text="6" , bg="powder blue", command = lambda: btnClick(6)).grid(row=3, column=2)
Substraction=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
                       text="-" , bg="powder blue", command = lambda: btnClick("-")).grid(row=3, column=3)
#==================================================================================
btn1=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
                       text="1" , bg="powder blue", command = lambda: btnClick(1)).grid(row=4, column=0)
btn2=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
                       text="2" , bg="powder blue", command = lambda: btnClick(2)).grid(row=4, column=1)
btn3=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
                       text="3" , bg="powder blue", command = lambda: btnClick(3)).grid(row=4, column=2)
Multiplication=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
                       text=" * " , bg="powder blue", command = lambda: btnClick(" * ")).grid(row=4, column=3)
#==================================================================================
btn0=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
                       text="0" , bg="powder blue", command = lambda: btnClick(0)).grid(row=5, column=0)
btnClear=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
                       text="c" , bg="powder blue", command=lambda:btnClearDisplay()).grid(row=5, column=1)
btnEquals=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
                       text="=" , bg="powder blue", command=btnEqualsInput).grid(row=5, column=2)
Multiplication=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
                       text=" / " , bg="powder blue", command = lambda: btnClick(" * ")).grid(row=5, column=3)
#=================================================================================
rand = StringVar()
Alubhat = StringVar()
Idli=StringVar()
Puri=StringVar()
Susla = StringVar()
Vada = StringVar()
SubTotal = StringVar()
WaterBotal=StringVar()
Tax = StringVar()
Cost=StringVar()



lblReference = Label(f1,font=('arial',16,'bold'), text="Reference", bd=16, anchor='w')
lblReference.grid(row=0,column=0)
txtReference=Entry(f1,font=('arial',16,'bold'), textvariable=rand, bd=10, insertwidth=4,
                                bg = "powder blue", justify = 'right')
txtReference.grid(row=0,column=1)


lblIdli = Label(f1,font=('arial',16,'bold'), text="Idli", bd=16, anchor='w')
lblIdli.grid(row=1,column=0)
txtIdli=Entry(f1,font=('arial',16,'bold'), textvariable=Idli , bd=10, insertwidth=4,
                              bg = "powder blue", justify = 'right')
txtIdli.grid(row=1,column=1)

lblPuri = Label(f1,font=('arial',16,'bold'), text="Puri ", bd=16, anchor='w')
lblPuri.grid(row=2,column=0)
txtPuri =Entry(f1,font=('arial',16,'bold'), textvariable=Puri , bd=10, insertwidth=4,
                              bg = "powder blue", justify = 'right')
txtPuri.grid(row=2,column=1)

lblSusla = Label(f1,font=('arial',16,'bold'), text="Susla  ", bd=16, anchor='w')
lblSusla.grid(row=3,column=0)
txtSusla  =Entry(f1,font=('arial',16,'bold'), textvariable=Susla  , bd=10, insertwidth=4,
                              bg = "powder blue", justify = 'right')
txtSusla.grid(row=3,column=1)

lblVada= Label(f1,font=('arial',16,'bold'), text="Vada ", bd=16, anchor='w')
lblVada.grid(row=4,column=0)
txtVada =Entry(f1,font=('arial',16,'bold'), textvariable=Vada , bd=10, insertwidth=4,
                              bg = "powder blue", justify = 'right')
txtVada.grid(row=4,column=1)

lblWaterBotal = Label(f1,font=('arial',16,'bold'), text="WaterBotal ", bd=16, anchor='w')
lblWaterBotal.grid(row=5,column=0)
txtWaterBotal =Entry(f1,font=('arial',16,'bold'), textvariable=WaterBotal , bd=10, insertwidth=4,
                              bg = "powder blue", justify = 'right')
txtWaterBotal.grid(row=5,column=1)

root.mainloop()




