#!/usr/bin/python
import Tkinter as tk
import ttk

import db
def getmenuchoices():
    names=[i[0] for i in db.getmealnames()]
    numbers=[i[1] for i in db.getmealnames()]
    return (names,numbers)

def getlogtext():
    return db.getLogText()
    
class App(object):
    def __init__(self):
        self.root=tk.Tk()
        self.root.resizable(width=tk.FALSE, height=tk.TRUE)
        self.mainloop=tk.mainloop
        self.root.rowconfigure(0,weight=1)
        self.root.columnconfigure(0,weight=0)

        self.topframe=tk.Frame(self.root)
        self.topframe.grid(column=0,row=0,sticky="NSEW")
        self.topframe.rowconfigure(0,weight=0)
        self.topframe.rowconfigure(1,weight=1)
        self.topframe.columnconfigure(0,weight=1)

        self.e=Entry(self.topframe,self.updatelog)
        self.e.grid(column=0,row=0,sticky="NSEW")
        self.l=Log(self.topframe)
        self.l.grid(column=0,row=1,sticky="NSEW")
        
    def updatelog(self):
        self.l.updatelog()

class Entry(ttk.LabelFrame):
    def __init__(self, parent,cmd):
        self.cmd=cmd
        ttk.LabelFrame.__init__(self,parent,text="Entry",width=300,height=140)
        self.rowconfigure(0,weight=1)
        self.columnconfigure(5,weight=1)

        self.rbut=ttk.Button(self,text="Reload",command=self.relfunc)
        self.rbut.grid(column=1,row=4,sticky="NESW",padx=3)
                
        self.val=tk.StringVar()
        self.cbb=ttk.Combobox(self,textvariable=self.val,state="readonly")
        self.cbb.grid(column=5,row=4,sticky="NSEW")
        (self.names,self.numbers)=getmenuchoices()
        self.cbb['values']=self.names
        self.cbb.bind('<<ComboboxSelected>>', self.selfunction)

        self.mval = tk.StringVar()
        self.mval.set("1.0")
        self.s = tk.Spinbox(self, from_=0.0, to=9.0, format="%2.1f", increment=0.1,textvariable=self.mval)
        self.s.grid(column=10,row=4,sticky="NSEW",padx=3)

        self.but=ttk.Button(self,text="Eat",command=self.butfunc)
        self.but.grid(column=15,row=4,sticky="NSEW",padx=4)
        
    def selfunction(self,arg):
        self.cbb.selection_clear()
    def butfunc(self):
        val=self.cbb.current()
        if val==-1 : return
        db.logmeal(self.numbers[val], float(self.mval.get()))
        self.cmd()
    def relfunc(self):
        self.cmd()
    
class Log(ttk.LabelFrame):
    def __init__(self, parent):
        ttk.LabelFrame.__init__(self,parent,text="Day Log",width=100,height=50)
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)

        self.txt=tk.Text(self,width=114,height=12,state="normal")
        s = ttk.Scrollbar(self,orient=tk.VERTICAL,command=self.txt.yview)
        s.grid(column=1,row=0,sticky="NS")
        self.txt.configure(yscrollcommand=s.set)
        self.txt.grid(column=0,row=0,sticky="NSEW")
        text=getlogtext()
        self.txt.insert("1.0",text)
        self.txt['state']="disabled"
    def updatelog(self):
        text=getlogtext()
        self.txt['state']="normal"
        self.txt.delete("1.0",index2="end")
        self.txt.insert("1.0",text)
        self.txt['state']="disabled"
        
        
db=db.db()
a=App()
a.mainloop()
