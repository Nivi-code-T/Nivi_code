import tkinter as tk

class Application(tk.Frame):
   def __init__(self,master=None):
     super().__init__(master)
     self.pack()
     self.create_widgets()

   def create_widgets(self):
     self.firstNumberEntry = tk.Entry()
     self.plusSign=tk.Label(text="+")
     self.secondNumberEntry = tk.Entry()
     self.equalSign = tk.Label(text="=")
     self.resultLabel=tk.Label(text="Result...",bg="Orange",fg="white")
     self.calculateButton =tk.Button(text="Calculate",command=self.calculate_sum)

    #Palce widgets
     self.firstNumberEntry.pack(side="left")
     self.plusSign.pack(side="left")
     self.secondNumberEntry.pack(side="left")
     self.equalSign.pack(side="left")
     self.resultLabel.pack(side="left")
     self.calculateButton.pack(side="left")


   def calculate_sum(self):
     try:
        num1 = float(self.firstNumberEntry.get())
        num2 = float(self.secondNumberEntry.get())
        result = num1 + num2
        self.resultLabel.config(text=str(result))
     except ValueError:
        self.resultLabel.config(text="Invalid input")

#Create the Application
app = Application()
app.master.title("Summator")
app.master.minsize(width=300, height=50)
app.mainloop()



