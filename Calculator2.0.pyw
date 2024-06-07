from customtkinter import *
from PIL import Image as img
from tkinter import *
try:
    import sympy
except Exception:
    pass
from math import *

Buttonfont = ("Lucida Handwriting", 20)
midfont = ("Lucida Handwriting", 14)
midfont2 = ("Lucida Handwriting", 11)
smallfont = ("Lucida Handwriting", 9)
KeyFrame_fg_color = "#242424"
fgcolor = "#242422"
Menu_color = "#382929"
operators = ["+", "-", "*", "/", "%"]
digit = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', "."]
mapping = {"/":"\u00F7", "*":"\u00D7"}
btns = {
    "2ⁿᵈ": (0, 0), "\u03C0": (0, 1), "e": (0, 2), "AC": (0, 3), "C": (0, 4),
    "x\u00B2": (1, 0), "\u221Ax": (1, 1), "xʸ": (1, 2), "10ˣ": (1, 3), "ln": (1, 4),
    "1/x": (2, 0), "(": (2, 1), ")": (2, 2), "n!": (2, 3), "/": (2, 4),
    "|x|": (3, 0), "7": (3, 1), "8": (3, 2), "9": (3, 3), "*": (3, 4),
    "exp": (4, 0), "4": (4, 1), "5": (4, 2), "6": (4, 3), "-": (4, 4),
    "log": (5, 0), "1": (5, 1), "2": (5, 2), "3": (5, 3), "+": (5, 4),
    "mod": (6, 0), "+/-": (6, 1), "0": (6, 2), ".": (6, 3), "=": (6, 4)
}
special = {
    "2ᴺᴰ": (0, 0), "x³": (1, 0), "\u221Bx": (2, 0), "ʸ\u221Ax": (3, 0), "2ˣ": (4, 0), "logᵧx": (5, 0), "eˣ":(6, 0)
}
tri = {
    "sin": (1, 1), "cos": (1, 2), "tan": (1, 3), "Inv": (1, 4),
    "cot": (2, 1), "sec": (2, 2), "csc": (2, 3), 
    }
inverse = {
    "sin⁻¹": (1, 1), "cos⁻¹": (1, 2), "tan⁻¹": (1, 3), "hyp": (1, 4),
    "cot⁻¹": (2, 1), "sec⁻¹": (2, 2), "csc⁻¹": (2, 3), 
    
}
hyp = {
    "sinh": (1, 1), "cosh": (1, 2), "tanh": (1, 3), "tri": (1, 4),
    "coth": (2, 1), "sech": (2, 2), "csch": (2, 3), 
    
}

class Calculator():
    Val = "0"
    exp = ""
    
    def __init__(self):
        self.win = CTk()
        self.win.geometry(f"{320}x{480}")
        self.win.iconbitmap("calculator2.ico")
        self.win.resizable(0, 0)
        self.win.title("Calculator")

        self.f1 = CTkFrame(self.win, corner_radius=0, fg_color=KeyFrame_fg_color, height=40, width=460)
        self.Mbutton = CTkButton(self.f1, text="", hover_color=KeyFrame_fg_color, image=CTkImage(img.open("menu.png"), size=(30, 30)), fg_color=KeyFrame_fg_color, width=40, font=Buttonfont, command=self.Menu)
        self.Mbutton.place(x=0, y=0)

        CTkLabel(self.f1, text="Standard Calculator", font=Buttonfont).place(x=50, y=5)
        self.f1.pack(pady=5)

        self.expLabel = CTkLabel(self.win, text=self.exp, font=Buttonfont)
        self.expLabel.pack(anchor=NE, padx=20)
        
        self.TextFrame = CTkFrame(self.win, corner_radius=5, height=100, width=460)
        self.TextFrame.pack(padx=4)

        self.KeyFrame = CTkFrame(self.win, corner_radius=5, height=330, width=460, fg_color=KeyFrame_fg_color)
        self.KeyFrame.pack(fill=BOTH, side=BOTTOM, pady=7)

        self.inp = StringVar()
        self.ent = CTkEntry(self.TextFrame, justify="right", height=100, width=460, fg_color=KeyFrame_fg_color, border_color="white", border_width=2, font=("Times New Roman", 60), textvariable=self.inp, state=DISABLED)
        self.inp.set(self.Val)
        self.ent.pack()

        self.buttons= {
            "AC": (1, 0), "C": (1, 1), "%": (1, 2), "/": (1, 3),
            "7": (2, 0), "8": (2, 1), "9": (2, 2), "*": (2, 3),
            "4": (3, 0), "5": (3, 1), "6": (3, 2), "-": (3, 3),
            "1": (4, 0), "2": (4, 1), "3": (4, 2), "+": (4, 3),
            "0": (5, 0), ".": (5, 2), "=": (5, 3)
        }
        self.specialBtn = {
            "\u221Ax": (0, 0), "\u221Bx": (0, 1), "x\u00B2": (0, 2), "+/-": (0, 3)
        }

        for key, gridValue in self.specialBtn.items():
            self.createSpecialBtn(key, gridValue)
        self.binding()

        for pair in self.buttons.items():
            self.createButton(pair[0], pair[1])
        self.rad  = True

    def createButton(self, key, gridValue):
        CTkButton(self.KeyFrame, command=lambda: self.click(key), width=80 if key !="0" else 140, height=48, hover_color=Menu_color, font=Buttonfont, fg_color=KeyFrame_fg_color, border_spacing=3, corner_radius=50, border_color="white", border_width=2, text=key if key not in ["/", "*"] else mapping.get(key)).grid(row=gridValue[0], column=gridValue[1], columnspan=1 if key != "0" else 2, pady=1)

    def createSpecialBtn(self, key, gridValue):
        CTkButton(self.KeyFrame, command=lambda: self.click(key.replace("x", "")), width=70, height=30, hover_color=Menu_color, font=Buttonfont, fg_color=KeyFrame_fg_color, border_spacing=3, corner_radius=50, border_color="white", border_width=2, text=key).grid(row=gridValue[0], column=gridValue[1], pady=2)

    def  click(self, text):
        if text in digit:
            if self.Val == "0" and text != ".":
                self.Val = ""
            self.Val += text
            self.inp.set(self.Val)
        elif text in operators:
            if len(self.exp) != 0 and self.exp[-1] in operators and self.Val == "0":
                self.exp = self.exp[:-1] + self.Val[:-1] + text
            else:
                if self.Val == "0" and self.Val[-1] == ".": self.Val += "0"
                self.exp = self.exp + self.Val + text
            if text in ["/", "*"]:
                self.exp= self.exp.replace("*", "\u00D7")
                self.exp= self.exp.replace("/", "\u00F7")
            self.expLabel.configure(text=self.exp)
            self.Val = "0"
        elif text == "AC":
            self.exp = ""
            self.Val = "0"
            self.expLabel.configure(text=self.exp)
            self.inp.set(self.Val)
        elif text == "C":
            self.Val = self.Val[:-1]
            if self.Val == "":
                self.Val += "0"
            self.inp.set(self.Val)
        elif text == "\u221A":
            self.exp += "\u221A" + self.Val
            self.expLabel.configure(text=self.exp)
            try:
                self.Val = str(eval(self.Val + "**.5"))
            except Exception:
                self.inp.set("Error")
            self.inp.set(self.Val)
            self.exp = ""
        elif text == "\u221B":
            self.exp += "\u221B" + self.Val
            self.expLabel.configure(text=self.exp)
            try:
                self.Val = str(cbrt(float(self.Val)))
            except Exception:
                self.inp.set("Error")
            self.inp.set(self.Val)
            self.exp = ""
        elif text == "\u00B2":
            self.exp += self.Val + "\u00B2"
            self.expLabel.configure(text=self.exp)
            try:
                self.Val = str(eval(self.Val + "**2"))
            except Exception:
                self.inp.set("Error")
            self.inp.set(self.Val)
            self.exp = ""
        elif text == "+/-":
            if self.Val[0] != "-":
                self.Val = "-" + self.Val
            else:
                self.Val = self.Val[1:]
            self.inp.set(self.Val)
        elif text == "=":
            if self.exp[:2] == "ʸ\u221A":
                txt = self.exp[2:]
                try:
                    self.exp = self.exp[2:] + "**(1/" + self.Val + ")"
                    self.inp.set(str(eval(str(self.exp))))
                except Exception: self.inp.set("Error")
                self.expLabel.configure(text = self.Val + "ʸ\u221A" + txt)
                self.Val = "0"
                return
            elif self.exp[-4:] == "base":
                try:
                    self.inp.set(log(float(self.exp[:self.exp.find("log")-1]), float(self.Val)))
                except Exception: self.inp.set("Error")
                self.expLabel.configure(text = self.exp + self.Val)
                self.Val = "0"
                return

            try:
                self.exp += self.Val
                self.exp=self.changeBtnText("^", "**")
                self.exp=self.changeBtnText("mod", "%")
                if self.exp.find("\u00D7") == -1 or self.exp.find("\u00F7") == -1:
                    self.exp=self.changeBtnText("\u00D7", "*")
                    self.exp=self.changeBtnText("\u00F7", "/")
                    self.Val = str(eval(self.exp))
                    self.exp= self.changeBtnText("/", "\u00F7")
                    self.exp= self.changeBtnText("**", "^")
                    self.exp= self.changeBtnText("%", "mod")
                    self.exp= self.changeBtnText("*", "\u00D7")
                else:
                    self.Val = str(eval(self.exp))
                self.expLabel.configure(text=self.exp)
                self.inp.set(self.Val)
                self.exp = ""
                # self.Val = "0"
            except ZeroDivisionError as error:
                self.inp.set("Math Error")
            except Exception as error:
                self.exp = ""
                self.Val = "0"
                self.inp.set("Error")
        
    def changeBtnText(self, x, y):
        return self.exp.replace(x, y)
    def updateOperator(self, text, change):
        ind = self.exp.find(text)
        self.exp = self.exp[:ind] + change + self.exp[ind +1:]

    def binding(self):
        self.win.bind()
        self.win.bind("<Return>", lambda event, key="=": self.click(key))
        self.win.bind("<Escape>", lambda event, key="AC": self.click(key))
        self.win.bind("<BackSpace>", lambda event, key="C": self.click(key))
        for key in ["%",  "/",  "7",  "8",  "9",  "*",  "4",  "5",  "6",  "-",  "1",  "2",  "3",  "+",  "0",  "."]:
            self.win.bind(str(key), lambda event, key=str(key): self.click(key))

    def Menu(self):
        self.frame = CTkFrame(self.win, width=240, height=435)
        self.createMenuButton("Standard", 2, self.Standard, CTkImage(img.open("Cal.png"), size=(20, 20)), fgcolor, Menu_color)
        self.createMenuButton("Scientific", 30, self.scientific, CTkImage(img.open("sciCalc.png"), size=(20, 20)), Menu_color, KeyFrame_fg_color)
        self.frame.place(x=0, y=45)
        def collapse():
            self.frame.destroy()
            self.Mbutton.configure(command=self.Menu)
        self.Mbutton.configure(command=collapse)


    def createMenuButton(self, text, y, cmd, Img, hvcolor, fgcolor):
        CTkButton(self.frame, width=240, image=Img, hover_color=hvcolor, font=midfont, fg_color=fgcolor, command=cmd, text=text, anchor=W).place(x=0, y=y)
    
    def Standard(self):
        for widget in self.KeyFrame.winfo_children():
            widget.grid_remove()
        try:
            self.radBtn.place_forget()
        except Exception:
            pass
        self.KeyFrame.pack(fill=BOTH, side=BOTTOM, pady=7)
        for key, gridValue in self.specialBtn.items():
            self.createSpecialBtn(key, gridValue)
        self.binding()

        for pair in self.buttons.items():
            self.createButton(pair[0], pair[1])
        self.frame.place_forget()

    def scientific(self):
        for widget in self.KeyFrame.winfo_children():
            widget.grid_remove()
        
        for key, gridValue in btns.items():
            self.createSciBtn(key, gridValue[0], gridValue[1])

        self.radBtn = CTkButton(self.TextFrame, command=self.UpdateRad, width=50, height=20, hover_color=Menu_color, font=smallfont, bg_color=KeyFrame_fg_color, fg_color=KeyFrame_fg_color, border_color="white", border_width=0, text="Rad")
        self.radBtn.place(x=5, y=5)
        self.frame.place_forget()

    def UpdateRad(self):
        self.radBtn.configure(text="Deg", hover_color=KeyFrame_fg_color, bg_color=Menu_color, fg_color=Menu_color, command=self.UpdateDeg)
        self.rad = False

    def UpdateDeg(self):
        self.radBtn.configure(text="Rad", hover_color=Menu_color, bg_color=KeyFrame_fg_color, fg_color=KeyFrame_fg_color, command=self.UpdateRad)
        self.rad = True

    def createSciBtn(self, text, r, c, font=midfont):
        if text in ["\u221Ax", "\u221Bx", "x\u00B2", "+/-", "\u00D7", "\u00F7", "AC", "C", "="] + digit + operators:
            CTkButton(self.KeyFrame, command=lambda: self.click(text.replace("x", "")), fg_color=KeyFrame_fg_color, height=35, hover_color=Menu_color, font=font, border_color="white", border_width=2, text=text, corner_radius=50, width=35).grid(row=r, column=c, pady=2, sticky=NSEW)
        else:
            CTkButton(self.KeyFrame, command=lambda: self.evaluate(text), fg_color=KeyFrame_fg_color, height=35, hover_color=Menu_color, font=font, border_color="white", border_width=2, text=text, corner_radius=50, width=35).grid(row=r, column=c, pady=2, sticky=NSEW)

    def evaluate(self, text):
        if text == "1/x":
            self.exp = "1/" + self.Val
            self.expLabel.configure(text=self.exp)
            try:
                self .Val = str(eval(self.exp))
                self.inp.set(self.Val)
            except Exception:
                self.inp.set("Error")
            self.exp = ""
        elif text == "(":
            self.exp += "("
            self.expLabel.configure(text=self.exp)
        elif text == ")":
            self.exp += ")"
            self.expLabel.configure(text=self.exp)
        elif text == "xʸ":
            self.exp = self.Val + "^"
            self.expLabel.configure(text=self.exp)
            self.Val = "0"
        elif text == "10ˣ":
            self.exp = "10^"+self.Val
            self.expLabel.configure(text=self.exp)
            self.Val=""
        elif text == "ln":
            self.exp = "ln(" + self.Val + ")"
            self.expLabel.configure(text=self.exp)
            try:
                self.Val = str(log(float(self.Val)))
                self.inp.set(self.Val)
            except Exception:
                self.inp.set("Error")
            self.exp = ""
        elif text == "log":
            self.exp = "log(" + self.Val + ")"
            self.expLabel.configure(text=self.exp)
            try:
                self.Val = str(log10(float(self.Val)))
                self.inp.set(self.Val)
            except Exception:
                self.inp.set("Error")
            self.exp = ""
        elif text == "|x|":
            self.exp = f"|{self.Val}|"
            self.expLabel.configure(text = self.exp)
            try:
                self.Val = abs(float(self.Val))
                self.inp.set(self.Val)
            except Exception:
                self.inp.set("Error")
            self.exp =""
        elif text == "exp":
            self.exp = f"exp({self.Val})"
            self.expLabel.configure(text = self.exp)
            try:
                self.inp.set(self.Val)
                self.Val = abs(float(self.Val))
            except Exception:
                self.inp.set("Error")
            self.exp = ""
        elif text == "mod":
            self.exp = self.Val + "mod"
            self.expLabel.configure(text=self.exp)
            self.Val = ""
        elif text == "\u03C0":
            self.inp.set(str(pi))
        elif text == "e":
            self.inp.set(str(e))
        elif text == "2ⁿᵈ":
            for key, gValue in tri.items():
                self.createSciBtn(key, gValue[0], gValue[1], midfont2)
            for key, gValue in special.items():
                self.createSciBtn(key, gValue[0], gValue[1], midfont2)

        elif text == "Inv":
            for key, gValue in inverse.items():
                self.createSciBtn(key, gValue[0], gValue[1], smallfont)
        elif text == "sin":
            self.triFun("sin", str(sin(float(self.Val))) if self.rad else str(sin(radians(float(self.Val)))))
        elif text == "cos":
            self.triFun("cos", str(cos(float(self.Val))) if self.rad else str(cos(radians(float(self.Val)))))
        elif text == "tan":
            self.triFun("tan", str(tan(float(self.Val))) if self.rad else str(tan(radians(float(self.Val)))))
        elif text == "cot":
            self.triFun("cot", str(sympy.cot(float(self.Val))) if self.rad else str(sympy.cot(radians(float(self.Val)))))
        elif text == "sec":
            self.triFun("sec", str(sympy.sec(float(self.Val))) if self.rad else str(sympy.sec(radians(float(self.Val)))))
        elif text == "csc":
            self.triFun("cosec", str(sympy.csc(float(self.Val))) if self.rad else str(sympy.csc(radians(float(self.Val)))))
        elif text == "sin⁻¹":
            try:
                self.triFun("sin⁻¹", str(asin(float(self.Val))) if self.rad else str(asin(radians(float(self.Val)))))
            except Exception:
                self.inp.set("Error")
        elif text == "cos⁻¹":
            try:
                self.triFun("cos⁻¹", str(acos(float(self.Val))) if self.rad else str(acos(radians(float(self.Val)))))
            except Exception:
                self.inp.set("Error")
        elif text == "tan⁻¹":
            try:
                self.triFun("tan⁻¹", str(atan(float(self.Val))) if self.rad else str(atan(radians(float(self.Val)))))
            except Exception:
                self.inp.set("Error")
        elif text == "csc⁻¹":
            try:
                self.triFun("cosec⁻¹", str(asin(1 / float(self.Val))) if self.rad else str(asin(radians(1 / float(self.Val)))))
            except Exception:
                self.inp.set("Error")
        elif text == "sec⁻¹":
            try:
                self.triFun("sec⁻¹", str(acos(1 / float(self.Val))) if self.rad else str(acos(radians(1 / float(self.Val)))))
            except Exception:
                self.inp.set("Error")
        elif text == "cot⁻¹":
            try:
                self.triFun("cot⁻¹", str(atan(1 / float(self.Val))) if self.rad else str(atan(radians(1 / float(self.Val)))))
            except Exception:
                self.inp.set("Error")
        elif text == "hyp":
            for key, gValue in hyp.items():
                self.createSciBtn(key, gValue[0], gValue[1], smallfont)
        elif text == "tri":
            for widget in self.KeyFrame.winfo_children():
                if str(widget)[-2:] in ["30", "31", "32", "35", "36", "37"]:
                    widget.grid_remove()
            for key, gValue in tri.items():
                self.createSciBtn(key, gValue[0], gValue[1], smallfont)
        elif text == "sinh":
            self.triFun("sinh", str(sinh(float(self.Val))) if self.rad else str(sinh(radians(float(self.Val)))))
        elif text == "cosh":
            self.triFun("cosh", str(cosh(float(self.Val))) if self.rad else str(cosh(radians(float(self.Val)))))
        elif text == "tanh":
            self.triFun("tanh", str(tanh(float(self.Val))) if self.rad else str(tanh(radians(float(self.Val)))))
        elif text == "coth":
            self.triFun("coth", str(sympy.coth(float(self.Val))) if self.rad else str(sympy.coth(radians(float(self.Val)))))
        elif text == "sech":
            self.triFun("sech", str(sympy.sech(float(self.Val))) if self.rad else str(sympy.sech(radians(float(self.Val)))))
        elif text == "csch":
            self.triFun("cosech", str(sympy.csch(float(self.Val))) if self.rad else str(sympy.csch(radians(float(self.Val)))))
        elif text == "n!":
            self.exp = f"fact({self.Val})"
            self.Val = factorial(int(self.Val))
            self.inp.set(self.Val)
            self.expLabel.configure(text=self.exp)
        elif text == "x³":
            self.exp = f"{self.Val}³"
            self.Val = str(float(self.Val) ** 3)
            self.inp.set(self.Val)
            self.expLabel.configure(text=self.exp)
        elif text == "ʸ\u221Ax":
            self.exp = f"ʸ\u221A{self.Val}"
            self.expLabel.configure(text=self.exp)
            self.Val = "0"
        elif text == "2ˣ":
            self.exp = f"2^{self.Val}³"
            self.Val = str(2 ** float(self.Val))
            self.inp.set(self.Val)
            self.expLabel.configure(text=self.exp)
        elif text == "logᵧx":
            self.exp = f"{self.Val} log base"
            self.expLabel.configure(text=self.exp)
            self.Val = "0"
        elif text == "eˣ":
            self.exp = f"e^{self.Val}³"
            self.Val = str(exp(float(self.Val)))
            self.inp.set(self.Val)
            self.expLabel.configure(text=self.exp)
        elif text == "2ᴺᴰ":
            # for widget in self.KeyFrame.winfo_children():
            #     widget.grid_remove()                
            for key, gValue in btns.items():
                self.createSciBtn(key, gValue[0], gValue[1], smallfont)


    def triFun(self, text, fun):
            self.exp = f"{text}({self.Val})"
            try:
                self.Val = fun
            except Exception:
                self.exp = "Error"
            self.inp.set(self.Val)
            self.expLabel.configure(text = self.exp)
            self.exp = ""

    def run(self):
        self.win.mainloop()

if __name__ == "__main__":
    Calc = Calculator()
    Calc.run()