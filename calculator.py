import tkinter as tk
from tkinter import messagebox
import math
from math import factorial
messagebox.showinfo("info","Enter only operand in operand 1 for any uni operand operations")
w=tk.Tk()
w.geometry("700x300")
l1=tk.Label(w,text="Operand 1: ")
l1.grid(row=0,column=0)
t1=tk.Entry(w)
t1.grid(row=0,column=1)
l2=tk.Label(w,text="Operand 2: ")
l2.grid(row=1,column=0)
t2=tk.Entry(w)
t2.grid(row=1,column=1)
def add():
    x=int(t1.get())
    y=int(t2.get())
    messagebox.showinfo('Result',x+y)
def sub():
    x=int(t1.get())
    y=int(t2.get())
    messagebox.showinfo('Result',x-y)
def mul():
    x=int(t1.get())
    y=int(t2.get())
    messagebox.showinfo('Result',x*y)
def intdiv():
    x=int(t1.get())
    y=int(t2.get())
    messagebox.showinfo('Result',x//y)
def floatdiv():
    x=int(t1.get())
    y=int(t2.get())
    messagebox.showinfo('Result',x/y)
def power():
    x=int(t1.get())
    y=int(t2.get())
    messagebox.showinfo('Result',x**y)
def fact():
    x=int(t1.get())
    s=1
    while x!=0:
        s*=x
        x=x-1
    messagebox.showinfo('Result',s)
def permutation():
    x=int(t1.get())
    y=int(t2.get())
    k=factorial(x)//factorial(x-y)
    messagebox.showinfo('Result',k)
def combination():
    x=int(t1.get())
    y=int(t2.get())
    k=factorial(x)//(factorial(x-y)*factorial(y))
    messagebox.showinfo('Result',k)
def root():
    x=int(t1.get())
    k=math.sqrt(x)
    messagebox.showinfo('Result',k)
def sin():
    x=int(t1.get())
    k=math.sin(x)
    messagebox.showinfo('Result',k)
def cos():
    x=int(t1.get())
    k=math.sqrt(x)
    messagebox.showinfo('Result',k)
def exp():
    x=int(t1.get())
    k=math.exp(x)
    messagebox.showinfo('Result',k)
def cosh():
    x=int(t1.get())
    k=math.cosh(x)
    messagebox.showinfo('Result',k)
def sinh():
    x=int(t1.get())
    k=math.sinh(x)
    messagebox.showinfo('Result',k)
def ln():
    x=int(t1.get())
    k=math.log(x)
    messagebox.showinfo('Result',k)
def log():
    x=int(t1.get())
    k=math.log10(x)
    messagebox.showinfo('Result',k)
def tan():
    x=int(t1.get())
    k=math.tan(x)
    messagebox.showinfo('Result',k)
def tanh():
    x=int(t1.get())
    k=math.tanh(x)
    messagebox.showinfo('Result',k)
def log1p():
    x=int(t1.get())
    k=math.log1p(x)
    messagebox.showinfo('Result',k)
def gcd():
    x=int(t1.get())
    y=int(t2.get())
    k=math.gcd(x,y)
    return k
def abs():
    x=float(t1.get())
    k=math.fabs(x)
    return k
def lcm():
    x=int(t1.get())
    y=int(t2.get())
    k=math.gcd(x,y)
    p=(x*y)/k
    return p
b1=tk.Button(w,text="Addition",command=add)
b1.grid(row=3,column=0)
b2=tk.Button(w,text="Subtraction",command=sub)
b2.grid(row=3,column=1)
b3=tk.Button(w,text="Multiplication",command=mul)
b3.grid(row=3,column=2)
b4=tk.Button(w,text="IntDivision",command=intdiv)
b4.grid(row=4,column=0)
b5=tk.Button(w,text="DecimalDivision",command=floatdiv)
b5.grid(row=4,column=1)
b6=tk.Button(w,text="Power",command=power)
b6.grid(row=4,column=2)
b7=tk.Button(w,text="Factorial",command=fact)
b7.grid(row=5,column=0)
b8=tk.Button(w,text="Permutation",command=permutation)
b8.grid(row=5,column=1)
b9=tk.Button(w,text="Combination",command=combination)
b9.grid(row=5,column=2)
b10=tk.Button(w,text="Sqrt",command=root)
b10.grid(row=6,column=0)
b11=tk.Button(w,text="Sin",command=sin)
b11.grid(row=6,column=1)
b12=tk.Button(w,text="Cos",command=cos)
b12.grid(row=6,column=2)
b13=tk.Button(w,text="e^x",command=exp)
b13.grid(row=7,column=0)
b14=tk.Button(w,text="Sinh",command=sinh)
b14.grid(row=7,column=1)
b15=tk.Button(w,text="Cosh",command=cosh)
b15.grid(row=7,column=2)
b16=tk.Button(w,text="ln",command=ln)
b16.grid(row=8,column=0)
b17=tk.Button(w,text="log",command=log)
b17.grid(row=8,column=1)
b18=tk.Button(w,text="log1p",command=log1p)
b18.grid(row=8,column=2)
b19=tk.Button(w,text="tan",command=tan)
b19.grid(row=9,column=0)
b20=tk.Button(w,text="tanh",command=tanh)
b20.grid(row=9,column=1)
b21=tk.Button(w,text="abs",command=abs)
b21.grid(row=9,column=2)
b22=tk.Button(w,text="gcd",command=gcd)
b22.grid(row=10,column=0)
b23=tk.Button(w,text="lcm",command=lcm)
b23.grid(row=10,column=1)
w.mainloop()
