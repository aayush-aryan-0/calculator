import tkinter as tk
import math
class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("300x500")

        self.eqn=[]
        self.text_prev=tk.StringVar()
        self.text=tk.StringVar()

        self.create_window()
        self.mainloop()
    def create_window(self):
        #label=tk.Label(self,text="Scinctific Calculator",font=("Arial",12))
        #label.pack(padx=100, pady=20)
        
        Entry_prev=tk.Entry(self,textvariable=self.text_prev,font=("Arial",19),state="normal",justify="right",bd=0,bg="black",fg="gray", highlightthickness=0)
        Entry_prev.pack(fill="x")
        #Entry_prev.config(disabledbackground="black", disabledforeground="gray")
        Entry=tk.Entry(self,textvariable=self.text,font=("Arial",19),state="normal",justify="right",bd=0,bg="black",fg="white", highlightthickness=0)
        Entry.pack(fill="x")
        #Entry.config(disabledbackground="black", disabledforeground="gray")


        frame=tk.Frame(self)
        for i in range(6):
            frame.rowconfigure(i,weight=1)
        for j in range(4):
            frame.columnconfigure(j,weight=1)


        buttons=["sin","cos","tan","sqrt",
        "log","(",")","^",
        "AC","mod","del","/",
         "7", "8","9","x",
         "4","5","6","-",
         "1","2","3","+",
         "!","0",".","="]
        for i, labels in enumerate(buttons):
            row=i//4
            column=i%4
            btn=tk.Button(frame,text=labels,font=("Arial",18),command=lambda val=labels:self.call(val))
            btn.grid(row=row,column=column,sticky="news")
 
        frame.pack(fill='both',expand=True)

    def evaluateinfix(self,eq):
    
        return self.evaluatepostfix(self.InfixToPostfix(eq))
    def prefrence(self,op):

        if(op=='+' or op=='-'):
            return 1
        if(op=='x'or op=='/' or op=="mod"):
            return 2
        if(op=='^'):
            return 3
        if(op=="!"):
            return 4
        if(op in ["log","sqrt","sin","cos","tan"]):
            return 5
    
        return 0
    

    def InfixToPostfix(self, eq):
        op = []
        postfix = []
        num = ""
        func=""
        if eq and (eq[0] in "+-") :
            postfix.append("0")
        for i in range(len(eq)):
            if eq[i].isdigit() or eq[i]=="." :
                num += eq[i]
            else:
                if num != "":
                    postfix.append(num)
                    num = ""
                if eq[i] == "(":
                    if(eq[i-1].isdigit()):
                        op.append("x")
                    op.append(eq[i])
                elif eq[i] == ")":
                    while op and op[-1] != "(":
                        postfix.append(op.pop())
                    op.pop()
                elif eq[i] in "+-x/^":
                    while op and (self.prefrence(op[-1]) > self.prefrence(eq[i]) or (self.prefrence(op[-1]) == self.prefrence(eq[i]) and eq[i] != '^')):
                        postfix.append(op.pop())
                    op.append(eq[i])
                elif eq[i] == "!":
                    op.append("!")
                elif eq[i].isalpha():
                    func+=eq[i]
                    if(func=="log"or func=="sqrt"or func=="sin" or func =="cos" or func =="tan" or func =="mod"  ):
                        op.append(func)
                        func=""        
        if num != "":
            postfix.append(num)
    
        while op:
            postfix.append(op.pop())
        return postfix

    def evaluate(self,n1,n2,op):
         match op:
            case "+": 
                return n1+n2
            case "-":
                return n1-n2
            case "/":
                if(n2==0):
                    raise ZeroDivisionError("Disvison by Zero")             
                return n1/n2
            case "mod":
                if(n2==0):
                    raise ZeroDivisionError("Disvison by Zero")
                return n1%n2
            case "x":
                return n1*n2
            case "^": 
                return pow(n1,n2)
    def UninaryEvaluate(self,num ,op):
         match op:
            case "log": 
                return math.log10(num)
            case "sqrt":
                return math.sqrt(num)
            case "sin":           
                return math.sin(math.radians(num))
            case "cos":  
                return math.cos(math.radians(num))
            case "tan":
                return math.tan(math.radians(num))
            case "!":
                 if(num>=0 and num.is_integer()):
                    return math.factorial(int(num))
                 else:
                    raise Exception("Factorial of invalid number ")

    def evaluatepostfix(self,postfix):
        var=[]
        for i in postfix:
            try:
                var.append(float(i))
            except:
                if(i in ["log","sin","cos","sqrt","tan","!"]):
                    if var:
                        var.append(self.UninaryEvaluate(var.pop(),i))
                    else:
                        raise IndexError("Expression Error")
                else:
                    if len(var)>=2:   
                        n2=var.pop()
                        n1=var.pop()
                        var.append(self.evaluate(n1,n2,i))
                    else:
                        raise IndexError("Expression Error")

        return var.pop()




    def call(self,n):
        if(n=="="):
            exp=''.join(self.eqn)
            try:
                result=self.evaluateinfix(exp)
                self.text_prev.set(str(exp))
                self.text.set("")
                self.text.set(result)
            except Exception as e:
                self.text.set("")
                self.eqn.clear()
                self.text.set(str(e))
        elif(n=="del"):
            if self.eqn:
                self.eqn.pop()
            self.text.set("")
            self.text.set(''.join(self.eqn))
        elif(n=="AC"):
            self.text.set("")
            self.text_prev.set("")
            self.eqn.clear()
        else:
            if(n.isdigit()):
                space=""
            else:
                space=" "
            self.text.set(self.text.get()+ space + n + space)
            self.eqn.append(n)
calcu=Calculator()
