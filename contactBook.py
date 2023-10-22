import tkinter as tk
from contactdb import ContactBook
import tkinter.ttk  as ttk





class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Contact Book")
        self.resizable(False,False)
        self.contact = ContactBook()
        #lb = tk.Listbox(self)
        self.geometry("800x400")
        #search button and event
        header = tk.Frame(self)
        header.pack(side=tk.TOP,fill='x')
        L1 = tk.Label(header, text="Search: ")
        L1.pack( side = tk.LEFT)
        self.E1 = tk.Entry(header, bd =5)
        self.E1.pack(side = tk.RIGHT, expand=True,fill='x')
        self.E1.bind("<Return>", self.handle_search_query)

        container = tk.Frame(self)
        container.pack(side=tk.BOTTOM)
        w = tk.Scrollbar(container ,orient=tk.VERTICAL)
        w.pack(side=tk.RIGHT,fill='y')

        columns = ("phone", "email","address")
        self.tree= ttk.Treeview(container, columns=columns ,height = 15,yscrollcommand=w.set)
        self.tree.pack(padx = 5, pady = 5)
        self.tree.heading('#0', text='Name')
        self.tree.heading('phone', text='Phone')
        self.tree.heading('email', text='Email')
        self.tree.heading('address', text='Address')
        self.handle_search_query()
            
        
        w.config(command=self.tree.yview)
        footer = tk.Frame(self)
        footer.pack(side=tk.BOTTOM)
        updatebtn = tk.Button(footer,text="Update",width=6, height=1,font=("Arial", 10),command=self.update_contact)
        deletebtn = tk.Button(footer,text="Delete",width=6, height=1,font=("Arial", 10),command=self.delete_contact)
        addbtn = tk.Button(footer,text="AddNew",width=6, height=1,font=("Arial", 10),command=self.add_contact)

        addbtn.pack(side="left",padx=5)
        updatebtn.pack(side="left",padx=5)
        deletebtn.pack(side="left",padx=5)
        

    def handle_search_query(self):
        self.tree.delete(*self.tree.get_children())
        for c in self.contact.searchContact((self.E1.get())):
            self.tree.insert('', tk.END, iid = c.id,
            text = c.name, values = [c.phone_no,c.email,c.address])
            #lb.insert(index, c.name)
            #lb.grid(row=index,column=0)

    def delete_contact(self):
        selected_item = self.tree.selection()
        if selected_item:
            #print(selected_item)
            self.contact.deleteContact(selected_item[0])
            self.handle_search_query()

    def _entry_create(self,lable,fr,width=8,height=2):
        btfr = tk.Frame(fr)
        btnlbl = tk.Label(btfr,text=lable,width=width,height=height,font=("Areal",10),pady=3)
        btnent = tk.Entry(btfr, bd =5,font=("Areal",12))
        btnlbl.pack(side='left')
        btnent.pack(side='right')

        return btfr,btnlbl,btnent
    def add_contact(self):
        dialog = tk.Toplevel(self)
        dialog.title("Add Contact")
        dialog.geometry("350x250")
        add = tk.Frame(dialog)
        nfr,nlbl,nent = self._entry_create("Name: ",add)
        pfr,plbl,pent = self._entry_create("Phone: ",add)
        efr,elbl,eent = self._entry_create("Email: ",add)
        afr,albl,aent = self._entry_create("Address: ",add)

        def submit():
            self.contact.addContact(nent.get(),pent.get(),eent.get(),aent.get())
            self.handle_search_query()
            dialog.destroy()
            

        addbtn = tk.Button(add,text="Submit",width=5, height=1,font=("Arial", 11),command=submit)



        nfr.pack()
        pfr.pack()
        efr.pack()
        afr.pack()
        add.pack()
        addbtn.pack()
    
    def update_contact(self):
        selected_item = self.tree.selection()
        if not selected_item:
            return
        dialog = tk.Toplevel(self)
        dialog.title("Update Contact")
        dialog.geometry("350x250")
        edit = tk.Frame(dialog)

        nfr,nlbl,nent = self._entry_create("Name: ",edit)
        pfr,plbl,pent = self._entry_create("Phone: ",edit)
        efr,elbl,eent = self._entry_create("Email: ",edit)
        afr,albl,aent = self._entry_create("Address: ",edit)


        
        sel_item = self.contact.getContact(selected_item[0])
        
        nent.insert(0,sel_item[1])
        pent.insert(0,sel_item[2])
        eent.insert(0,sel_item[3])
        aent.insert(0,sel_item[4])

        def submit():
            self.contact.updateContact(selected_item[0],name=nent.get(),phone_no=pent.get(),email=eent.get(),address=aent.get())
            self.handle_search_query()
            dialog.destroy()
            

        addbtn = tk.Button(edit,text="Submit",width=5, height=1,font=("Arial", 11),command=submit)



        nfr.pack()
        pfr.pack()
        efr.pack()
        afr.pack()
        edit.pack()
        addbtn.pack()
        
    

        
        


if __name__ == '__main__':
    app = App()
    app.mainloop()
    

