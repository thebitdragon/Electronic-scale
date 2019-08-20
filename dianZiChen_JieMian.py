# ！/usr/bin/env python
# coding:utf-8
__author__ = "liyanhe"


import time
import threading
from tkinter import *
import decimal,math,string
#######################################################################################################################
'''
"""
arduino数据采集
"""
ser = serial.Serial( #下面这些参数根据情况修改
    port='COM8',
    baudrate=38400,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS)
'''
hx711 = 0.0
tare = 0.0
data1 = 0.0
def get_data():
    global scale,b
    scale = 228
    b = 1
    global hx711,tare,data1
    hx711 = ser.readline()
    data1 = float(str(hx711)[2:-5])
    x = data1
    y = x/ scale + b - tare
    data.set('%.2f'%y)
    total = float(unit) * float(y)
    totalPrice.set('%.2f'%total)
    global timer
    timer = threading.Timer(0.5,get_data)
    timer.start()
timer = threading.Timer(0.5,get_data)
timer.start()
#######################################################################################################################

root = Tk()
root.title("电子秤")

#######################################################################################################################
global cuncu, display, result, fuhao
result = fuhao = None
display = StringVar()
cuncu = []

class anjianzhi:
    global cuncu, display, result, fuhao
    def __init__(self,anjian):
        self.anjian = anjian
    def jia(self):
        cuncu.append(self.anjian)
        display.set( ''.join(cuncu))
    def clear(self):
        cuncu.clear()
        data.set('0')
        totalPrice.set('0')
        display.set('0')
        global unit,tare
        tare = 0
        unit = 0
        result = None
        fuhao = None
    def tare(self):
        cuncu.clear()
        data.set('0')
        totalPrice.set('0')
        display.set('0')
        global tare,unit,scale,b
        tare = data1/scale + b
        unit = 0
    def zhengfu(self):
        if cuncu[0]:
            if cuncu[0] == '-':
                cuncu[0] = '+'
            elif cuncu[0] == '+':
                cuncu[0] = '-'
            else:
                cuncu.insert(0, '-')
        display.set(''.join(cuncu))
    def xiaoshudian(self):
        if cuncu.count('.') >= 1:
            pass
        else:
            if cuncu == [] :
                cuncu.append('0')
            cuncu.append('.')
            display.set(''.join(cuncu))
            print(fuhao)
            print(result)
            display.set(str(result))
            cuncu.clear()
#######################################################################################################################



unit = 0
def get_entry():
   global unit
   unit = unit_price.get()

   print(unit)


########################################################################################################################
'''
容器fm1
文本显示框组件
'''
fm1 = Frame(root)
display = StringVar()
totalPrice = StringVar()
data = StringVar()
Label(fm1,text = "  重量  ").grid(row = 0,column = 0,sticky = W + E)
Label(fm1,text = "  单价  ").grid(row = 1,column = 0,sticky = W + E)
Label(fm1,text = "  总价  ").grid(row = 2,column = 0,sticky = W + E)
Label(fm1,text = "  g  ").grid(row = 0,column = 2,sticky = W + E)
Label(fm1,text = "  元/g  ").grid(row = 1,column = 2,sticky = W + E)
Label(fm1,text = "  元  ").grid(row = 2,column = 2,sticky = W + E)
weight = Entry(fm1,textvariable= data)
weight.grid(row = 0,column = 1)

unit_price = Entry(fm1,textvariable=display)
unit_price.grid(row = 1,column = 1)

total_price = Entry(fm1,textvariable = totalPrice)
total_price.grid(row = 2,column = 1)

########################################################################################################################


#######################################################################################################################
"""
容器fm2
按键组件
"""

fm2 = Frame(root)
button1 = Button(fm2,text = " 1 ",command = anjianzhi('1').jia)
button1.grid(row = 5,column = 0,sticky = N + S + W + E)

button2 = Button(fm2,text = " 2 ",command = anjianzhi('2').jia)
button2.grid(row = 5,column = 1,sticky = N + S + W + E)

button3 = Button(fm2,text = " 3 ",command = anjianzhi('3').jia)
button3.grid(row = 5,column = 2,sticky = N + S + W + E)

button4 = Button(fm2,text = " 4 ",command = anjianzhi('4').jia)
button4.grid(row = 4,column = 0,sticky = N + S + W + E)

button5 = Button(fm2,text = " 5 ",command = anjianzhi('5').jia)
button5.grid(row = 4,column = 1,sticky = N + S + W + E)

button6 = Button(fm2,text = " 6 ",command = anjianzhi('6').jia)
button6.grid(row = 4,column = 2,sticky = N + S + W + E)

button7 = Button(fm2,text = " 7 ",command = anjianzhi('7').jia)
button7.grid(row = 3,column = 0,sticky = N + S + W + E)

button8 = Button(fm2,text = " 8 ",command = anjianzhi('8').jia)
button8.grid(row = 3,column = 1,sticky = N + S + W + E)

button9 = Button(fm2,text = " 9 ",command = anjianzhi('9').jia)
button9.grid(row = 3,column = 2,sticky = N + S + W + E)

button0 = Button(fm2,text = " 0 ",command = anjianzhi('0').jia)
button0.grid(row = 6,column = 0,columnspan = 2,sticky = E + W)

buttonDot = Button(fm2,text = " . ",command = anjianzhi('.').jia)
buttonDot.grid(row = 6,column = 2,sticky = E + W)

buttonClear = Button(fm2,text = "清零",command = anjianzhi('c').clear)
buttonClear.grid(row = 3,column = 4,rowspan = 2,sticky = N + S + W + E)

buttonTare = Button(fm2,text = "去皮",command = anjianzhi('c').tare)
buttonTare.grid(row = 5,column = 4,rowspan = 2,sticky = N + S + W + E)

buttonSet = Button(fm2,text = " Enter ",command = get_entry).grid(row = 3,column = 3,rowspan = 4,sticky = N + S + W + E)


########################################################################################################################




########################################################################################################################
"""
菜单栏组件
"""
menu=Menu(root)
submenu1=Menu(menu,tearoff=0)
menu.add_cascade(label='查看',menu=submenu1)
submenu2 = Menu(menu, tearoff=0)
submenu2.add_command(label='复制')
submenu2.add_command(label='粘贴')
menu.add_cascade(label='编辑',menu=submenu2)
submenu = Menu(menu, tearoff=0)
submenu.add_command(label='查看帮助')
submenu.add_separator()
submenu.add_command(label='关于电子秤')
menu.add_cascade(label='帮助',menu=submenu)
root.config(menu=menu)
########################################################################################################################

'''
组件显示
'''
fm1.pack()
fm2.pack()

root.mainloop()

