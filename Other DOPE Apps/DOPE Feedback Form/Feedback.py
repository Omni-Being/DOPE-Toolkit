from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os

class FeedBack:
    def __init__(self,master):
        
        master.title("DOPE Feedback Form")
        master.resizable(False,False)
        master.configure(background='black')
        master.wm_iconbitmap('..\\..\\DOPE Icons\\DOPE.ico')

        self.style=ttk.Style()
        self.style.configure('TFrame',background='black')
        self.style.configure('TButton',background='black')
        self.style.configure('TLabel',background='black',font=('Arial',11))
        self.style.configure('Header.TLabel',foreground='green',font=('Forte',18,'bold')) 

        self.frame_header=ttk.Frame(master)
        self.frame_header.pack()

        ttk.Label(self.frame_header,style='Header.TLabel',text="Thanks For Your Views. It's what We gain....").grid(row=0,column=1,pady=20)
        ttk.Label(self.frame_header,wraplength=400,font=("Comic Sans MS",8,'bold'),foreground='gold',text='We are glad to know that We are the priceless things to all of you.').grid(row=1,column=1,pady=30)
        
        self.frame_content=ttk.Frame(master)
        self.frame_content.pack()

        ttk.Label(self.frame_content,foreground='white',text="Name:").grid(row=0,column=0,padx=10,sticky='e')
        ttk.Label(self.frame_content,foreground='white',text="Email:").grid(row=0,column=2,padx=10,sticky='sw')
        ttk.Label(self.frame_content,foreground='white',text="Comments:").grid(row=3,column=0,padx=10,sticky='sw')

        self.name=StringVar()
        self.email=StringVar()
        self.entry_name=ttk.Entry(self.frame_content,textvariable=self.name,width=24,font=('Arial',10))
        self.entry_email=ttk.Entry(self.frame_content,textvariable=self.email,width=24,font=('Arial',10))
        self.text_comments=Text(self.frame_content,width=50,height=10,font=('Arial',10),wrap=WORD)

        self.entry_name.grid(row=0,column=1,padx=5)
        self.entry_email.grid(row=0,column=3,padx=5)
        self.text_comments.grid(row=4,column=0,columnspan=4,padx=5)

        ttk.Button(self.frame_content,text='Submit',command=self.data_submit).grid(row=5,column=1,sticky='e',pady=5,padx=10)
        ttk.Button(self.frame_content,text='Clear',command=self.data_clear).grid(row=5,column=2,sticky='w',pady=5,padx=10)
        ttk.Button(self.frame_content,text='Quit',command=master.destroy).grid(row=5,column=3,sticky='w',pady=5,padx=10)

        self.status=Label(master,font=('Arial',8),text='Copyright \u00A9 and Trademarks \u2122 by DOPE Pvt. Ltd. Comapany',bd=1,anchor=W,relief=SUNKEN)
        self.status.pack(side=BOTTOM,fill=X)
        
    def data_submit(self):
        self.sub_name=self.name.get()
        self.sub_email=self.email.get()
        self.sub_comments=self.text_comments.get(1.0,'end')
        os.chdir('..\\..\\Saved Data\\DOPE Feedback\\')
        self.sub_name2=self.sub_name+'.docx'
        self.save_me=open(self.sub_name2,'a+')
        self.save_me.write("Name:\t")
        self.save_me.write(self.sub_name)
        self.save_me.write("\n-----\n")
        self.save_me.write("Email:\t")
        self.save_me.write(self.sub_email)
        self.save_me.write("\n------\n")
        self.save_me.write("Comments:")
        self.save_me.write("\n---------\n")
        self.save_me.write(self.sub_comments)
        self.save_me.write("\n\n")
        self.save_me.close()
        messagebox.showinfo(title="DOPE Feedback Form",message="Successfully submitted.")
        

    def data_clear(self):
        self.entry_name.delete(0,'end')
        self.entry_email.delete(0,'end')
        self.text_comments.delete(1.0,'end')
        
def main():
    root=Tk()
    feedback=FeedBack(root)
    root.mainloop()
    
if __name__=="__main__":main()
