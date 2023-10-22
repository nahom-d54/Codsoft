import tkinter as tk
import tkinter.ttk  as ttk


class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        self.title("TODO LIST")
        self.geometry("600x400")
        self.resizable(False,False)
        h1 = tk.Label(self, text="GET THINGS DONE", font=("Arial", 20))
        h1.pack()

        tsk = tk.Frame(self)
        self.taskin = tk.Entry(tsk,bd=1,width=41,font=("Arial",13))
        addtask = tk.Button(tsk,text="Add Task",command=self.addTodo,font=("Arial",13))
        self.taskin.pack(ipadx=5, ipady=3,side='left')
        addtask.pack(side='right')
        tsk.pack()
        deletetask = tk.Button(self,text="Remove Task",command=self.delTodo,font=("Arial",13))

        container = tk.Frame(self)
        container.pack()
        scrollbar = tk.Scrollbar(container)
        scrollbar.pack(side=tk.RIGHT,fill='y')

        self.lb = tk.Listbox(container,width=50,height=12,font=("Arial",13),yscrollcommand=scrollbar.set)
        self.lb.pack(pady=5,side=tk.LEFT,fill=tk.BOTH)
        deletetask.pack()

    def addTodo(self):
        if self.taskin.get():
            self.lb.insert(tk.END,self.taskin.get())
        self.taskin.delete(0,tk.END)
    def delTodo(self):
        for i in self.lb.curselection():
            self.lb.delete(i)
            
        


        



if __name__ == '__main__':
    app = App()
    app.mainloop()
    