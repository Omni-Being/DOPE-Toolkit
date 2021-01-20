from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askdirectory
from PIL import Image as im
from PIL import ImageTk as imtk
from tkinter import messagebox as msgb
import pygame as pg
import pyqrcode as pqr
import png
from random import *
from math import *
import os
from sys import *
import time
from calendar import *
from csv import *
import cv2  
import numpy as np
import win32com.client as wincl
import webbrowser as wbb
from tkinter.colorchooser import *







class DOPE_Word_Count:



    def __init__(self,wordc_mst_wm):
        wordc_mst_wm.title("DOPE Word Count")
        wordc_mst_wm.resizable(False,False)
        wordc_mst_wm.configure(background='#e3e5e5')
        wordc_mst_wm.wm_iconbitmap('DOPE Icons\\DOPE.ico')


        Label(wordc_mst_wm,text='Enter text:-',bg="#e3e5e5").grid(row=1,column=1,padx=20,pady=20,sticky=W,columnspan=3)


        self.text_in=Text(wordc_mst_wm,height=20,width=100)
        self.text_in.grid(row=2,column=1,padx=20,pady=10,columnspan=3)


        Button(wordc_mst_wm,text="Submit",command=self.w_submit).grid(row=3,column=1,padx=20,pady=10)
        Button(wordc_mst_wm,text="Clear",command=self.w_clear).grid(row=3,column=2,padx=20,pady=10)
        Button(wordc_mst_wm,text="Quit",command=wordc_mst_wm.destroy).grid(row=3,column=3,padx=20,pady=10)
        
  
        self.getout=Label(wordc_mst_wm,text='',height=8,width=100,bg="#e3e5e5",anchor=W,justify=LEFT)
        self.getout.grid(row=4,column=1,columnspan=3,padx=20,pady=20)
        self.status13=Label(wordc_mst_wm,font=('Arial',7),text='Copyright \u00A9 and Trademarks \u2122 by DOPE Pvt. Ltd. Company.',bd=1,anchor=W,relief=SUNKEN)
        self.status13.grid(row=5,column=1,columnspan=3,pady=0,sticky='nsew')



    def w_submit(self):
        self.mytextin=self.text_in.get(1.0,END)
        self.alpha=self.digit=self.title=self.lower=self.spc=self.upper=self.space=0
        for i in self.mytextin:
            if i.isalpha()==True:
                self.alpha+=1
            elif i.isdigit()==True:
                self.digit+=1
            elif i.isspace()==True:
                self.space+=1
            else:
                self.spc+=1
            if i.islower()==True:
                self.lower+=1
            if i.isupper()==True:
                self.upper+=1
            if i.istitle()==True:
                self.title+=1
        self.getout.configure(text="Alphabets="+str(self.alpha)+"\nDigits="+str(self.digit)+"\nLowercase Letters="+str(self.lower)+"\nUppercase Letters="+str(self.upper)+"\nTitled Letters="+str(self.title)+"\nWhitespaces="+str(self.space)+"\nSpecial Characters="+str(self.spc))
                
                
    def w_clear(self):
        self.text_in.delete(1.0,END)






class DOPE_Crypto_Graphy:



    def __init__(self):
        crypt_mst_wm=Tk()
        crypt_mst_wm.title("DOPE Cryptography")
        crypt_mst_wm.resizable(False,False)
        crypt_mst_wm.configure(background='#e3e5e5')
        crypt_mst_wm.wm_iconbitmap('DOPE Icons\\DOPE.ico')

        
        Label(crypt_mst_wm,text="Enter your message:",bg='#e3e5e5').grid(row=1,column=1,padx=10,pady=10)

        self.entry_input=Entry(crypt_mst_wm,width=50)
        self.entry_input.grid(row=1,column=2,pady=20,padx=5)


        self.enc_but=Button(crypt_mst_wm,text='Encrypt',command=self.data_encode)
        self.enc_but.grid(row=2,column=1,sticky='e',pady=5,padx=0)

        self.dec_but=Button(crypt_mst_wm,text='Decrypt',command=self.data_decode)
        self.dec_but.grid(row=2,column=2,pady=20)


        Label(crypt_mst_wm,text="Required Data :",bg='#e3e5e5').grid(row=3,column=1,padx=10,pady=10)

        self.entry_output=Entry(crypt_mst_wm,width=50,state=DISABLED)
        self.entry_output.grid(row=3,column=2,pady=20,padx=5)


        self.cy_quit=Button(crypt_mst_wm,text='Quit',command=crypt_mst_wm.destroy,width=10)
        self.cy_quit.grid(row=5,column=1,pady=20,columnspan=2,padx=10)
        
        self.cy_save=Button(crypt_mst_wm,text='Save',command=self.data_save)
        self.cy_save.grid(row=4,column=1,pady=5,columnspan=1,sticky='w',padx=20)
        
        self.cy_clear=Button(crypt_mst_wm,text='Clear',command=self.data_clear)
        self.cy_clear.grid(row=4,column=1,pady=5,columnspan=2,sticky='e',padx=20)


        self.status12=Label(crypt_mst_wm,font=('Arial',7),text='Copyright \u00A9 and Trademarks \u2122 by DOPE Pvt. Ltd. Company.',bd=1,anchor=W,relief=SUNKEN)
        self.status12.grid(row=6,column=1,columnspan=2,sticky='nsew')


        
    def data_encode(self):
        msgb.showinfo(title="DOPE Encrypting....",message="Data Encryption is in progress. This will take a few seconds.")
        self.sub_data=self.entry_input.get()
        self.issue_data=''
        for letter in self.sub_data:
            if letter.isalpha():
                num = ord(letter)
                if letter.isupper():
                    base = ord('A')
                elif letter.islower():
                    base = ord('a')
                num = (num - base + 20) % 26 + base
                self.issue_data += chr(num)
            elif letter.isdigit():
                self.issue_data += letter
            else:
                self.issue_data += letter
        self.entry_output.configure(state=NORMAL)
        self.entry_output.delete(0,END)
        self.entry_output.insert(END,self.issue_data)
        self.entry_output.configure(state=DISABLED)

    
        
    def data_decode(self):
        msgb.showinfo(title="DOPE Decrypting....",message="Data Decryption is in progress. This will take a few seconds.")
        self.sub_data=self.entry_input.get()
        self.issue_data=''
        for letter in self.sub_data:
            if letter.isalpha():
                num = ord(letter)
                if letter.isupper():
                    base = ord('A')
                elif letter.islower():
                    base = ord('a')
                num = (num - base - 20) % 26 + base
                self.issue_data += chr(num)
            elif letter.isdigit():
                self.issue_data += letter
            else:
                self.issue_data += letter
        self.entry_output.configure(state=NORMAL)
        self.entry_output.delete(0,END)
        self.entry_output.insert(END,self.issue_data)
        self.entry_output.configure(state=DISABLED)



    def data_save(self):
        msgb.showinfo(title="Saving Data...",message="Data saved successfully.")
        self.sub_data1=self.entry_input.get()
        self.sub_data2=self.entry_output.get()
        self.tempfile=time.asctime(time.localtime(time.time()))
        self.templist=self.tempfile.split(':')
        self.tempfilestr='-'.join(self.templist)
        self.tempfilestr+='.txt'
        self.temp_loc=os.getcwd()
        os.chdir('Saved Data\\DOPE Cryptography\\')
        file_obj=open(self.tempfilestr,'w')
        file_obj.write(time.asctime(time.localtime(time.time())))
        file_obj.write("\n-------------------------------")
        file_obj.write("\nGiven Data:-    ")
        file_obj.write(self.sub_data1)
        file_obj.write("\nModified Data:- ")
        file_obj.write(self.sub_data2)
        file_obj.write("\n\n\n\n")
        file_obj.close()
        os.chdir(self.temp_loc)



    def data_clear(self):
        self.entry_input.delete(0,END)
        self.entry_output.configure(state=NORMAL)
        self.entry_output.delete(0,END)
        self.entry_output.configure(state=DISABLED)





class DOPE_Currency:
    def __init__(self,curr_mst_wm):
        curr_mst_wm.title("DOPE Currency")
        curr_mst_wm.resizable(0,0)
        curr_mst_wm.geometry('280x300')
        curr_mst_wm.configure(background='#e3e5e5')
        curr_mst_wm.wm_iconbitmap('DOPE Icons\\DOPE.ico')


        self.curr_inl=Label(curr_mst_wm,text="Enter currency in ",anchor=W,bg='#e3e5e5')
        self.curr_inl.grid(row=1,column=1,padx=10,pady=20)

        self.curr_var1=StringVar()
        self.curr_all=['','USA Dollar','Rupee','Euro','Yen','Dirham']
        self.curr_sel1=ttk.OptionMenu(curr_mst_wm,self.curr_var1,*self.curr_all)
        self.curr_sel1.grid(row=1,column=2,pady=20,padx=0)
        

        self.curr_in=Entry(curr_mst_wm,width=40)
        self.curr_in.grid(row=2,column=1,columnspan=2,padx=10,pady=0)


        self.conv_curr=Button(curr_mst_wm,width=20,height=3,text='Convert',command=self.curr_convert)
        self.conv_curr.grid(row=3,column=1,columnspan=2,padx=10,pady=20)


        self.curr_outl=Label(curr_mst_wm,text="Converted currency in ",anchor=W,bg='#e3e5e5')
        self.curr_outl.grid(row=4,column=1,padx=10,pady=20)

        self.curr_var2=StringVar()
        self.curr_sel2=ttk.OptionMenu(curr_mst_wm,self.curr_var2,*self.curr_all)
        self.curr_sel2.grid(row=4,column=2,pady=20,padx=0)


        self.curr_out=Entry(curr_mst_wm,width=40,state=DISABLED)
        self.curr_out.grid(row=5,column=1,columnspan=2,padx=10,pady=10)


        self.status11=Label(curr_mst_wm,font=('Arial',7),text='Copyright \u00A9 and Trademarks \u2122 by DOPE Pvt. Ltd. Company.',bd=1,anchor=W,relief=SUNKEN)
        self.status11.grid(row=6,column=1,columnspan=2,sticky='nsew')



    def curr_convert(self):
        try:
            self.curr_in_var=int(self.curr_in.get())
        except:
            self.curr_in.delete(0,END)
            msgb.showinfo(title="DOPE Currency",message="Wrong Input")
        else:
            if self.curr_var2.get()=='Select Currency' or self.curr_var1.get()=='Select Currency':
                msgb.showinfo(title="DOPE Currency",message="Please select the required currency.")
            else:
                if self.curr_var1.get()=="USA Dollar" and self.curr_var2.get()=="Rupee":
                    self.ans_curr=self.curr_in_var*68.58
                elif self.curr_var1.get()=="USA Dollar" and self.curr_var2.get()=="Euro":
                    self.ans_curr=self.curr_in_var*0.86                    
                elif self.curr_var1.get()=="USA Dollar" and self.curr_var2.get()=="Yen":
                    self.ans_curr=self.curr_in_var*110.42
                elif self.curr_var1.get()=="USA Dollar" and self.curr_var2.get()=="Dirham":
                    self.ans_curr=self.curr_in_var*3.67
                elif self.curr_var1.get()=="Rupee" and self.curr_var2.get()=="USA Dollar":
                    self.ans_curr=self.curr_in_var*0.015
                elif self.curr_var1.get()=="Rupee" and self.curr_var2.get()=="Euro":
                    self.ans_curr=self.curr_in_var*0.013
                elif self.curr_var1.get()=="Rupee" and self.curr_var2.get()=="Yen":
                    self.ans_curr=self.curr_in_var*1.61
                elif self.curr_var1.get()=="Rupee" and self.curr_var2.get()=="Dirham":
                    self.ans_curr=self.curr_in_var*0.053
                elif self.curr_var1.get()=="Euro" and self.curr_var2.get()=="USA Dollar":
                    self.ans_curr=self.curr_in_var*1.16
                elif self.curr_var1.get()=="Euro" and self.curr_var2.get()=="Rupee":
                    self.ans_curr=self.curr_in_var*79.37
                elif self.curr_var1.get()=="Euro" and self.curr_var2.get()=="Yen":
                    self.ans_curr=self.curr_in_var*127.47
                elif self.curr_var1.get()=="Euro" and self.curr_var2.get()=="Dirham":
                    self.ans_curr=self.curr_in_var*4.28
                elif self.curr_var1.get()=="Yen" and self.curr_var2.get()=="USA Dollar":
                    self.ans_curr=self.curr_in_var*0.0091
                elif self.curr_var1.get()=="Yen" and self.curr_var2.get()=="Rupee":
                    self.ans_curr=self.curr_in_var*0.63
                elif self.curr_var1.get()=="Yen" and self.curr_var2.get()=="Euro":
                    self.ans_curr=self.curr_in_var*0.0078
                elif self.curr_var1.get()=="Yen" and self.curr_var2.get()=="Dirham":
                    self.ans_curr=self.curr_in_var*0.033
                elif self.curr_var1.get()=="Dirham" and self.curr_var2.get()=="USA Dollar":
                    self.ans_curr=self.curr_in_var*0.27
                elif self.curr_var1.get()=="Dirham" and self.curr_var2.get()=="Rupee":
                    self.ans_curr=self.curr_in_var*18.77
                elif self.curr_var1.get()=="Dirham" and self.curr_var2.get()=="Euro":
                    self.ans_curr=self.curr_in_var*0.24
                elif self.curr_var1.get()=="Dirham" and self.curr_var2.get()=="Yen":
                    self.ans_curr=self.curr_in_var*30.00
                else:
                    self.curr_out.delete(0,END)
                    msgb.showinfo(title="DOPE Currency",message="Input currencies are the same.")
                self.curr_out.configure(state=NORMAL,font=("Arial",8,"bold"))
                self.curr_out.delete(0,END)
                self.curr_out.insert(END,str(self.ans_curr))
                self.curr_out.configure(state=DISABLED)





class DOPE_Browser:



    def __init__(self,brow_mst_wm):
        brow_mst_wm.title("DOPE Browser")
        brow_mst_wm.resizable(False,False)
        brow_mst_wm.configure(background='#e3e5e5')
        brow_mst_wm.wm_iconbitmap('DOPE Icons\\DOPE.ico')


        self.enter_url_l=Label(brow_mst_wm,text='Enter Url or search directly:-',bg='#e3e5e5')
        self.enter_url_l.grid(row=1,column=1,padx=80,pady=30)

        self.enter_url=Entry(brow_mst_wm,width=50,justify=LEFT)
        self.enter_url.grid(row=1,column=2,pady=30)


        self.search_but=Button(brow_mst_wm,text='Search Me',bg='#e3e5e5',width=20,height=3,font=('Arial',10,'bold'),bd=20,relief='groove',command=self.search_me)
        self.search_but.grid(row=2,column=1,columnspan=2,padx=300,pady=0)


        self.quit_search=Button(brow_mst_wm,text='Quit',command=brow_mst_wm.destroy)
        self.quit_search.grid(row=3,column=2,pady=20,sticky='e',padx=100)


        self.status9=Label(brow_mst_wm,font=('Arial',7),text='Copyright \u00A9 and Trademarks \u2122 by DOPE Pvt. Ltd. Company.',bd=1,anchor=W,relief=SUNKEN)
        self.status9.grid(row=4,column=1,columnspan=2,sticky='nsew')



    def search_me(self):
        self.url_in=str(self.enter_url.get())
        self.taburl='http://google.com/?#q='
        wbb.open(self.taburl+self.url_in,new=1)
        




class DOPE_Color_Picker:



    def __init__(self,color_mst_wm):
        color_mst_wm.title("DOPE Color Picker")
        color_mst_wm.resizable(False,False)
        color_mst_wm.configure(background='#e3e5e5')
        color_mst_wm.wm_iconbitmap('DOPE Icons\\DOPE.ico')

        
        self.color_var=Button(color_mst_wm,text="Select Color",width=10,height=2,command=self.getcolor,bd=10,relief=RIDGE)
        self.color_var.grid(row=1,column=1,padx=50,pady=20)

        self.color_out=Entry(color_mst_wm,justify=CENTER,width=40)
        self.color_out.grid(row=2,column=1,padx=20,pady=20)


        self.quit_color=Button(color_mst_wm,text='Quit',command=color_mst_wm.destroy).grid(row=3,column=1,padx=20,pady=10,sticky='w')


        self.status10=Label(color_mst_wm,font=('Arial',7),text='Copyright \u00A9 and Trademarks \u2122 by DOPE Pvt. Ltd. Company.',bd=1,anchor=W,relief=SUNKEN)
        self.status10.grid(row=4,column=1,sticky='nsew')


        
    def getcolor(self):
        self.mycolor=askcolor()
        self.color_out.delete(0,END)
        self.color_out.insert(END,self.mycolor)
        

        


class DOPE_Calendar:



    def __init__(self,calen_mst_wm):
        calen_mst_wm.title("DOPE Calendar")
        calen_mst_wm.resizable(False,False)
        calen_mst_wm.configure(background='#e3e5e5')
        calen_mst_wm.wm_iconbitmap('DOPE Icons\\DOPE.ico')


        self.enter_yearl=Label(calen_mst_wm,text='Enter Year:-',bg='#e3e5e5')
        self.enter_yearl.grid(row=1,column=1,padx=20,pady=20,sticky='e')

        self.enter_year=Entry(calen_mst_wm,width=10)
        self.enter_year.grid(row=1,column=2,padx=20,pady=20,sticky='w')


        self.enter_monthl=Label(calen_mst_wm,text='Enter Month:-',bg='#e3e5e5')
        self.enter_monthl.grid(row=2,column=1,padx=20,pady=20,sticky='e')

        self.enter_month=Entry(calen_mst_wm,width=10)
        self.enter_month.grid(row=2,column=2,padx=20,pady=20,sticky='w')


        self.button_getcal=Button(calen_mst_wm,text="Get Calendar",width=15,command=self.cal_cal)
        self.button_getcal.grid(row=3,column=1,columnspan=2,padx=20,pady=0)


        self.print_cal_area=Label(calen_mst_wm,width=100,height=35,justify=CENTER,bg='#e3e5e5')
        self.print_cal_area.grid(row=4,column=1,columnspan=2,padx=20,pady=20)


        self.status8=Label(calen_mst_wm,font=('Arial',7),text='Copyright \u00A9 and Trademarks \u2122 by DOPE Pvt. Ltd. Company.',bd=1,anchor=W,relief=SUNKEN)
        self.status8.grid(row=5,column=1,columnspan=2,sticky='nsew')



    def cal_cal(self):
        try:
            self.yer=self.enter_year.get()
            self.mon=self.enter_month.get()
            if self.yer=='' and self.mon=='':
                msgb.showinfo(title="DOPE Calendar",message="Input boxes are blank.")
            elif self.yer=='' and self.mon!='':
                self.p_cal=month(2020,int(self.mon))
            elif self.yer!='' and self.mon=='':
                self.p_cal=calendar(int(self.yer))
            elif self.yer!='' and self.mon!='':
                self.p_cal=month(int(self.yer),int(self.mon))
            self.print_cal_area.configure(text=self.p_cal)
        except:
            msgb.showinfo(title="DOPE Calendar",message="Wrong Input.")
            self.enter_year.delete(0,END)
            self.enter_month.delete(0,END)
        
      



class DOPE_Clock:



    def __init__(self,clock_mst_wm):
        self.time1=''


        clock_mst_wm.title("DOPE Clock")
        clock_mst_wm.resizable(False,False)
        clock_mst_wm.configure(background='#e3e5e5')
        clock_mst_wm.wm_iconbitmap('DOPE Icons\\DOPE.ico')


        self.myclock=Label(clock_mst_wm,font=('times','20','bold'),bg='#e3e5e5',height=3,width=30)
        self.myclock.pack(fil=BOTH,expand=1)


        self.quit_clock=Button(clock_mst_wm,text='Quit',command=clock_mst_wm.destroy).pack(pady=20)


        self.status7=Label(clock_mst_wm,font=('Arial',7),text='Copyright \u00A9 and Trademarks \u2122 by DOPE Pvt. Ltd. Company.',bd=1,anchor=W,relief=SUNKEN)
        self.status7.pack(fill=BOTH,expand=1)

        
        self.tick()



    def tick(self):
        self.time2=time.strftime('%H:%M:%S')
        if self.time2!=self.time1:
            self.time1=self.time2
            self.myclock.config(text=self.time2)
        self.myclock.after(200,self.tick)





class DOPE_QR_Code:



    def __init__(self,qr_mst_wm):
        qr_mst_wm.title("DOPE QR Code Generator")
        qr_mst_wm.resizable(False,False)
        qr_mst_wm.configure(background='#e3e5e5')
        qr_mst_wm.wm_iconbitmap('DOPE Icons\\DOPE.ico')


        self.qr_l=Label(qr_mst_wm,text='Enter text to generate QR Code:-',bg='#e3e5e5')
        self.qr_l.grid(row=1,column=1,padx=20,pady=10)
        
        self.qrtext_in=Text(qr_mst_wm,width=50,height=12,font=('Arial',10),wrap=WORD)
        self.qrtext_in.grid(row=2,column=1,padx=20,pady=0)


        self.gen_qr_but=Button(qr_mst_wm,height=2,width=15,bg="#e3e5e5",text="Generate QR Code",font=('Arial',8,'bold'),command=self.gen_qr_func)
        self.gen_qr_but.grid(row=3,column=1,padx=5,pady=20)


        self.status6=Label(qr_mst_wm,font=('Arial',7),text='Copyright \u00A9 and Trademarks \u2122 by DOPE Pvt. Ltd. Company.',bd=1,anchor=W,relief=SUNKEN)
        self.status6.grid(row=4,column=1,sticky='nsew')



    def gen_qr_func(self):
        self.a1=str(randint(1,1000))
        self.a2=str(randint(1,1000))
        self.a3=str(randint(1,1000))
        self.a4=str(randint(1,1000))
        self.a5=str(randint(1,1000))
        self.list_code=[self.a1,self.a2,self.a3,self.a4,self.a5]
        self.ren_code=''.join(self.list_code)
        self.ren_code+='.png'
        self.qrget=self.qrtext_in.get(1.0,END)
        self.qr=pqr.create(self.qrget)
        self.cur_loc=os.getcwd()
        os.chdir('Saved Data\\DOPE QR Code\\')
        self.qr.png(self.ren_code,scale=15)
        msgb.showinfo(title="DOPE QR Code Generator",message="QR Code is successfully saved to installed folder.")
        os.chdir(self.cur_loc)



        

class DOPE_Text_2_Speech:



    def __init__(self,txt2sph_mst_wm):
        txt2sph_mst_wm.title("DOPE Text 2 Speech")
        txt2sph_mst_wm.resizable(False,False)
        txt2sph_mst_wm.configure(background='#e3e5e5')
        txt2sph_mst_wm.wm_iconbitmap('DOPE Icons\\DOPE.ico')


        self.text_in_l=Label(txt2sph_mst_wm,text='Enter Text 2 Speech:-',bg='#e3e5e5')
        self.text_in_l.grid(row=1,column=1,padx=20,pady=10,sticky='w')

        self.text_in=Text(txt2sph_mst_wm,width=50,height=12,font=('Arial',10),wrap=WORD)
        self.text_in.grid(row=2,column=1,padx=20,pady=0)


        self.start_sp_but=Button(txt2sph_mst_wm,height=3,width=20,bg="#e3e5e5",text="Speech",font=('Arial',15,'bold'),command=self.listen_me)
        self.start_sp_but.grid(row=3,column=1,padx=5,pady=30)


        self.status5=Label(txt2sph_mst_wm,font=('Arial',7),text='Copyright \u00A9 and Trademarks \u2122 by DOPE Pvt. Ltd. Company.',bd=1,anchor=W,relief=SUNKEN)
        self.status5.grid(row=4,column=1,sticky='nsew')



    def listen_me(self):
        self.get_text=self.text_in.get(1.0,END)
        self.speak=wincl.Dispatch('SAPI.SpVoice')
        self.speak.Speak(self.get_text)

        



class DOPE_Web_Camera:



    def __init__(self,web_cam_mst_wm):
        web_cam_mst_wm.title("DOPE WebCam")
        web_cam_mst_wm.resizable(False,False)
        web_cam_mst_wm.configure(background='#e3e5e5')
        web_cam_mst_wm.wm_iconbitmap('DOPE Icons\\DOPE.ico')


        self.vid_in_l=Label(web_cam_mst_wm,text='Enter name of the video file to record:-',bg='#e3e5e5')
        self.vid_in_l.grid(row=1,column=1,padx=20,pady=10)
        
        self.vid_name=Entry(web_cam_mst_wm,width=30)
        self.vid_name.grid(row=2,column=1,padx=20,pady=0)


        self.start_vid_but=Button(web_cam_mst_wm,height=2,width=15,bg="#e3e5e5",text="Start Recording",font=('Arial',8,'bold'),command=self.rec_vid)
        self.start_vid_but.grid(row=3,column=1,padx=5,pady=20)


        self.vid_note=Label(web_cam_mst_wm,text='{ Note:-  Press "d" key to stop recording. }',bg='#e3e5e5')
        self.vid_note.grid(row=4,column=1,padx=10,pady=10)


        self.status4=Label(web_cam_mst_wm,font=('Arial',7),text='Copyright \u00A9 and Trademarks \u2122 by DOPE Pvt. Ltd. Company.',bd=1,anchor=W,relief=SUNKEN)
        self.status4.grid(row=5,column=1,sticky='nsew')



    def rec_vid(self):
        self.vid_name_in=self.vid_name.get()
        self.vid_name.delete(0,END)
        if self.vid_name_in=='':
            msgb.showinfo(title="DOPE WebCam",message="Please enter the media name to save.")
        else:
            self.cur_loc=os.getcwd()
            os.chdir('Saved Data\\DOPE WebCam\\')
            self.vid_name_in+='.mp4'
            self.capture_vid=cv2.VideoCapture(0)
            self.save_vid=cv2.VideoWriter_fourcc(*'MP4V')
            self.out_vid_file=cv2.VideoWriter(self.vid_name_in,self.save_vid,15.0,(640,480))
            while True:
                self.return_me,self.vid_frame=self.capture_vid.read()
                self.out_vid_file.write(self.vid_frame)
                cv2.imshow('DOPE WebCam',self.vid_frame)
                if cv2.waitKey(1) & 0xFF==ord('d'):
                    break
            self.capture_vid.release()
            self.out_vid_file.release()
            cv2.destroyAllWindows()
            msgb.showinfo(title="DOPE WebCam",message="Video is successfully saved to installed folder.")
            os.chdir(self.cur_loc)
        





class DOPE_Calculator:


    
    def __init__(self,calc_mst_wm):
        self.f2=("Calibri",10,"bold")    

        
        calc_mst_wm.title("DOPE Calculator")
        calc_mst_wm.resizable(False,False)
        calc_mst_wm.configure(background='#e3e5e5')
        calc_mst_wm.wm_iconbitmap('DOPE Icons\\DOPE.ico')


        self.m_frame=Frame(calc_mst_wm,bg='#e3e5e5')
        self.m_frame.grid(row=1,column=1)
        self.frame2=Frame(self.m_frame,bg="#e3e5e5")
        self.frame2.grid(row=2,column=1,padx=0,pady=0,sticky='nsew')
        self.frame3=Frame(self.frame2,bg="#e3e5e5")    
        self.frame3.grid(row=1,column=1,padx=0,pady=0,sticky='w')
        self.frame4=Frame(self.frame2,bg="#e3e5e5")
        self.frame4.grid(row=1,column=2,padx=0,pady=0,sticky='e')


        self.e1=Entry(self.m_frame,width=38,bg="white",font=self.f2,bd=2)
        self.e1.grid(row=1,column=1)


        self.btn1=Button(self.frame3,height=2,width=5,bg="#e3e5e5",text="7",font=self.f2,command=lambda:self.cal('7'))
        self.btn1.grid(row=1,column=1,padx=5,pady=5)

        self.btn2=Button(self.frame3,height=2,width=5,bg="#e3e5e5",text="4",font=self.f2,command=lambda:self.cal('4'))
        self.btn2.grid(row=2,column=1,padx=5,pady=5)

        self.btn3=Button(self.frame3,height=2,width=5,bg="#e3e5e5",text="1",font=self.f2,command=lambda:self.cal('1'))
        self.btn3.grid(row=3,column=1,padx=5,pady=5)
        
        self.btn5=Button(self.frame3,height=2,width=5,bg="#e3e5e5",text="8",font=self.f2,command=lambda:self.cal('8'))
        self.btn5.grid(row=1,column=2,padx=5,pady=5)

        self.btn6=Button(self.frame3,height=2,width=5,bg="#e3e5e5",text="5",font=self.f2,command=lambda:self.cal('5'))
        self.btn6.grid(row=2,column=2,padx=5,pady=5)

        self.btn7=Button(self.frame3,height=2,width=5,bg="#e3e5e5",text="2",font=self.f2,command=lambda:self.cal('2'))
        self.btn7.grid(row=3,column=2,padx=5,pady=5)

        self.btn8=Button(self.frame3,height=2,width=5,bg="#e3e5e5",text="0",font=self.f2,command=lambda:self.cal('0'))
        self.btn8.grid(row=4,column=2,padx=5,pady=5)

        self.btn9=Button(self.frame3,height=2,width=5,bg="#e3e5e5",text="9",font=self.f2,command=lambda:self.cal('9'))
        self.btn9.grid(row=1,column=3,padx=5,pady=5)

        self.btn10=Button(self.frame3,height=2,width=5,bg="#e3e5e5",text="6",font=self.f2,command=lambda:self.cal('6'))
        self.btn10.grid(row=2,column=3,padx=5,pady=5)

        self.btn11=Button(self.frame3,height=2,width=5,bg="#e3e5e5",text="3",font=self.f2,command=lambda:self.cal('3'))
        self.btn11.grid(row=3,column=3,padx=5,pady=5)


        self.btn4=Button(self.frame3,height=2,width=5,bg="#e3e5e5",text=".",font=self.f2,command=lambda:self.cal('.'))
        self.btn4.grid(row=4,column=1,padx=5,pady=5)

        self.btn12=Button(self.frame3,height=2,width=5,bg="#e3e5e5",text='=',font=self.f2,command=self.equal)
        self.btn12.grid(row=4,column=3,padx=5,pady=5)

        self.btn13=Button(self.frame4,height=2,width=5,bg="#e3e5e5",text="/",font=self.f2,command=lambda:self.cal('/'))
        self.btn13.grid(row=1,column=1,padx=5,pady=5)
    
        self.btn14=Button(self.frame4,height=2,width=5,bg="#e3e5e5",text="X",font=self.f2,command=lambda:self.cal('*'))
        self.btn14.grid(row=2,column=1,padx=5,pady=5)

        self.btn15=Button(self.frame4,height=2,width=5,bg="#e3e5e5",text="-",font=self.f2,command=lambda:self.cal('-'))
        self.btn15.grid(row=3,column=1,padx=5,pady=5)

        self.btn16=Button(self.frame4,height=2,width=5,bg="#e3e5e5",text="+",font=self.f2,command=lambda:self.cal('+'))
        self.btn16.grid(row=4,column=1,padx=5,pady=5)

        self.btn18=Button(self.frame4,height=2,width=5,bg="#e3e5e5",text="(",font=self.f2,command=lambda:self.cal('('))
        self.btn18.grid(row=2,column=2,padx=5,pady=5)
        
        self.btn19=Button(self.frame4,height=2,width=5,bg="#e3e5e5",text=")",font=self.f2,command=lambda:self.cal(')'))
        self.btn19.grid(row=3,column=2,padx=5,pady=5)


        self.btn20=Button(self.frame4,height=2,width=5,bg="#e3e5e5",text="^",font=self.f2,command=lambda:self.cal('**'))
        self.btn20.grid(row=4,column=2,padx=5,pady=5)

        self.btn17=Button(self.frame4,height=2,width=5,bg="#e3e5e5",text="DEL",font=self.f2,command=self.del_item)
        self.btn17.grid(row=1,column=2,padx=5,pady=5)


        self.status2=Label(self.frame2,font=('Arial',7),text='Copyright \u00A9 and Trademarks \u2122 by DOPE Pvt. Ltd. Company.',bd=1,anchor=W,relief=SUNKEN)
        self.status2.grid(row=2,column=1,columnspan=2,sticky='nsew')



    def equal(self):
        self.x=self.e1.get()
        try:
            self.y=eval(self.x)
        except:
            self.e1.delete(0,END)
            self.e1.insert(END,'Syntax Error')
        else:
            self.e1.delete(0,END)
            self.e1.insert(END,self.y)


            
    def del_item(self):
        self.e1.delete(0,END)



    def cal(self,var):
        self.e1.insert(END,var)





class DOPE_Music_Player:


    
    def __init__(self,music_mst_wm):
        self.list_of_songs=[]
        self.all_col=['red','blue','green','cyan','yellow','pink','gold','orange','white','grey','brown','purple','magenta','lightgreen','darkgreen','#923711','skyblue','darkblue']
        self.index=0

        
        music_mst_wm.title("DOPE Music Player")
        music_mst_wm.resizable(False,False)
        music_mst_wm.configure(background='#e3e5e5')
        music_mst_wm.wm_iconbitmap('DOPE Icons\\DOPE.ico')


        self.select_button=Button(music_mst_wm,text='Select Music Folder',command=self.select_music_list,bg='#e3e5e5')
        self.select_button.grid(row=1,column=1,pady=10,padx=10)

        self.quit_button=Button(music_mst_wm,text='Quit',command=music_mst_wm.destroy,bg='#e3e5e5')
        self.quit_button.grid(row=1,column=3,pady=10,padx=10)


        self.logo_but=Button(music_mst_wm,text='\n\tD\t\t\n\t\tO\t\n\tP\t\t\n\t\tE\t\n',anchor=W,bd=10,font=('Arial',15,'bold'),fg='black',command=self.chg_mus_col)
        self.logo_but.grid(row=2,column=1,columnspan=3,pady=10,padx=20)
        

        self.prev_button=Button(music_mst_wm,text='|\u25c0\u25c0',command=self.prev_music,bg='#e3e5e5')
        self.prev_button.grid(row=3,column=1,pady=10,padx=0)

        self.play_button=Button(music_mst_wm,text='\u25B6',command=self.music_play,bg='#e3e5e5')
        self.play_button.grid(row=3,column=2,pady=10,padx=0,sticky='w')

        self.forw_button=Button(music_mst_wm,text='\u25B6\u25B6|',command=self.next_music,bg='#e3e5e5')
        self.forw_button.grid(row=3,column=3,pady=10,padx=10,sticky='w')


        self.music_label=Label(music_mst_wm,text='Hi... Select the MUSIC folder to rock the floor.',height=3,width=30,wraplength=200,bg='#e3e5e5')
        self.music_label.grid(row=4,column=1,pady=10,padx=10,columnspan=3)


        self.status3=Label(music_mst_wm,font=('Arial',7),text='Copyright \u00A9 and Trademarks \u2122 by DOPE Pvt. Ltd. Company.',bd=1,anchor=W,relief=SUNKEN)
        self.status3.grid(row=5,column=1,columnspan=3,sticky='nsew')



    def select_music_list(self):
        self.s_m_folder=askdirectory()
        os.chdir(self.s_m_folder)
        for self.m_files in os.listdir(self.s_m_folder):
            if self.m_files.endswith(".mp3"):
                self.list_of_songs.append(self.m_files)
        self.list_of_songs.reverse()



    def chg_mus_col(self):
        self.cho_color=choice(self.all_col)
        self.logo_but.configure(bg=self.cho_color)



    def music_play(self):
        pg.mixer.init()
        pg.mixer.music.load(self.list_of_songs[self.index])
        pg.mixer.music.play()
        pg.mixer.music.set_volume(1.0)
        self.updatelabel()



    def next_music(self):
        self.index+=1
        pg.mixer.music.load(self.list_of_songs[self.index])
        pg.mixer.music.play()
        pg.mixer.music.set_volume(1.0)
        self.updatelabel()



    def prev_music(self):
        self.index-=1
        pg.mixer.music.load(self.list_of_songs[self.index])
        pg.mixer.music.play()
        pg.mixer.music.set_volume(1.0)
        self.updatelabel()



    def updatelabel(self):
        self.music_label.configure(text=self.list_of_songs[self.index])
        




class DOPE_Notes:



    def __init__(self,notes_mst_wm):
        notes_mst_wm.title("DOPE Notes")
        notes_mst_wm.resizable(False,False)
        notes_mst_wm.configure(background='#e3e5e5')
        notes_mst_wm.wm_iconbitmap('DOPE Icons\\DOPE.ico')

        
        self.note_in=Text(notes_mst_wm,width=80,height=15,font=('Arial',10),wrap=WORD)
        self.note_in.grid(row=1,column=1,columnspan=5,padx=10,pady=10)

        self.f_note_label=Label(notes_mst_wm,text='Enter name of the file to save:-',bg='#e3e5e5')
        self.f_note_label.grid(row=2,column=1,padx=10,pady=10)
        
        self.f_note_name=Entry(notes_mst_wm,width=30)
        self.f_note_name.grid(row=2,column=2,padx=10,pady=10)

        self.note_save=Button(notes_mst_wm,text="Save",command=self.nsave_me)
        self.note_save.grid(row=2,column=3,padx=10,pady=10)

        self.note_clear=Button(notes_mst_wm,text='Clear',command=self.nclear_me)
        self.note_clear.grid(row=2,column=4,padx=10,pady=10)

        self.note_quit=Button(notes_mst_wm,text='Quit',command=notes_mst_wm.destroy)
        self.note_quit.grid(row=2,column=5,padx=10,pady=10)



    def nsave_me(self):
        self.cur_loc=os.getcwd()
        os.chdir('Saved Data\\DOPE Notes\\')
        self.my_notes_save=self.note_in.get(1.0,END)
        self.file_name_in=self.f_note_name.get()
        if self.file_name_in=='':
            msgb.showinfo(title="DOPE Notes",message="Please enter the file name to save.")
        else:
            self.file_name_in+=".txt"
            self.save_note=open(self.file_name_in,'a+')
            self.save_note.write(self.my_notes_save)
            self.save_note.close()
            msgb.showinfo(title="DOPE Notes",message="Successfully saved.")
        os.chdir(self.cur_loc)
        


    def nclear_me(self):
        self.f_note_name.delete(0,END)
        self.note_in.delete(1.0,END)
        




class DOPE_Toolkit:



    def __init__(self,master_wm):
        master_wm.title("DOPE Toolkit")
        master_wm.resizable(False,False)
        master_wm.configure(background='#e3e5e5')
        master_wm.wm_iconbitmap('DOPE Icons\\DOPE.ico')


        self.wcam=PhotoImage(file='DOPE Pictures\\Webcamera.png')
        self.wcamlab=Button(master_wm,height=40,width=50,image=self.wcam,bg='#e3e5e5',command=self.go_webcamera)
        self.wcamlab.grid(row=1,column=1,padx=20,pady=20)

        self.brow=PhotoImage(file='DOPE Pictures\\Browser.png')
        self.browlab=Button(master_wm,height=40,width=50,image=self.brow,bg='#e3e5e5',command=self.go_browser)
        self.browlab.grid(row=1,column=2,padx=0,pady=20)

        self.calc=PhotoImage(file='DOPE Pictures\\Calculator.png')
        self.calclab=Button(master_wm,height=40,width=50,image=self.calc,bg='#e3e5e5',command=self.go_calculator)
        self.calclab.grid(row=1,column=3,padx=20,pady=20)

        self.calen=PhotoImage(file='DOPE Pictures\\Calendar.png')
        self.calenlab=Button(master_wm,height=40,width=50,image=self.calen,bg='#e3e5e5',command=self.go_calendar)
        self.calenlab.grid(row=1,column=4,padx=0,pady=20)

        self.cloc=PhotoImage(file='DOPE Pictures\\Clock.png')
        self.cloclab=Button(master_wm,height=40,width=50,image=self.cloc,bg='#e3e5e5',command=self.go_clock)
        self.cloclab.grid(row=1,column=5,padx=20,pady=20)


        self.wcam_l=Label(master_wm,text='WebCam',font=('Arial',8,'bold'),bg='#e3e5e5')
        self.wcam_l.grid(row=2,column=1,padx=20,pady=0)

        self.brow_l=Label(master_wm,text='Browser',font=('Arial',8,'bold'),bg='#e3e5e5')
        self.brow_l.grid(row=2,column=2,padx=0,pady=0)

        self.calc_l=Label(master_wm,text='Calculator',font=('Arial',8,'bold'),bg='#e3e5e5')
        self.calc_l.grid(row=2,column=3,padx=20,pady=0)

        self.calen_l=Label(master_wm,text='Calender',font=('Arial',8,'bold'),bg='#e3e5e5')
        self.calen_l.grid(row=2,column=4,padx=0,pady=0)

        self.cloc_l=Label(master_wm,text='Clock',font=('Arial',8,'bold'),bg='#e3e5e5')
        self.cloc_l.grid(row=2,column=5,padx=20,pady=0)


        self.CMD=PhotoImage(file='DOPE Pictures\\CMD.png')
        self.CMDlab=Button(master_wm,height=40,width=50,image=self.CMD,bg='#e3e5e5',command=self.go_command_prompt)
        self.CMDlab.grid(row=3,column=1,padx=20,pady=20)

        self.col=PhotoImage(file='DOPE Pictures\\Color.png')
        self.collab=Button(master_wm,height=40,width=50,image=self.col,bg='#e3e5e5',command=self.go_color)
        self.collab.grid(row=3,column=2,padx=0,pady=20)

        self.cryp=PhotoImage(file='DOPE Pictures\\Crypt.png')
        self.cryplab=Button(master_wm,height=40,width=50,image=self.cryp,bg='#e3e5e5',command=self.go_crypt)
        self.cryplab.grid(row=3,column=3,padx=20,pady=20)

        self.curr=PhotoImage(file='DOPE Pictures\\Currency.png')
        self.currlab=Button(master_wm,height=40,width=50,image=self.curr,bg='#e3e5e5',command=self.go_currency)
        self.currlab.grid(row=3,column=4,padx=0,pady=20)

        self.dict=PhotoImage(file='DOPE Pictures\\Dictionary.png')
        self.dictlab=Button(master_wm,height=40,width=50,image=self.dict,bg='#e3e5e5',command=self.go_dictionary)
        self.dictlab.grid(row=3,column=5,padx=20,pady=20)


        self.CMD_l=Label(master_wm,text='CMD',font=('Arial',8,'bold'),bg='#e3e5e5')
        self.CMD_l.grid(row=4,column=1,padx=20,pady=0)

        self.col_l=Label(master_wm,text='Color Picker',font=('Arial',8,'bold'),bg='#e3e5e5')
        self.col_l.grid(row=4,column=2,padx=0,pady=0)

        self.cryp_l=Label(master_wm,text='Crypt Data',font=('Arial',8,'bold'),bg='#e3e5e5')
        self.cryp_l.grid(row=4,column=3,padx=20,pady=0)

        self.curr_l=Label(master_wm,text='Currency',font=('Arial',8,'bold'),bg='#e3e5e5')
        self.curr_l.grid(row=4,column=4,padx=0,pady=0)

        self.dict_l=Label(master_wm,text='Dictionary',font=('Arial',8,'bold'),bg='#e3e5e5')
        self.dict_l.grid(row=4,column=5,padx=20,pady=0)


        self.egge=PhotoImage(file='DOPE Pictures\\Eggeater.png')
        self.eggelab=Button(master_wm,height=40,width=50,image=self.egge,bg='#e3e5e5',command=self.go_eggeater)
        self.eggelab.grid(row=5,column=1,padx=20,pady=20)

        self.wc=PhotoImage(file='DOPE Pictures\\Wordcount.png')
        self.wclab=Button(master_wm,height=40,width=50,image=self.wc,bg='#e3e5e5',command=self.go_wordcount)
        self.wclab.grid(row=5,column=2,padx=0,pady=20)

        self.stpw=PhotoImage(file='DOPE Pictures\\Stopwatch.png')
        self.stpwlab=Button(master_wm,height=40,width=50,image=self.stpw,bg='#e3e5e5',command=self.go_stopwatch)
        self.stpwlab.grid(row=5,column=3,padx=20,pady=20)
        
        self.mup=PhotoImage(file='DOPE Pictures\\Musicplayer.png')
        self.muplab=Button(master_wm,height=40,width=50,image=self.mup,bg='#e3e5e5',command=self.go_music_player)
        self.muplab.grid(row=5,column=4,padx=0,pady=20)

        self.notes=PhotoImage(file='DOPE Pictures\\Notes.png')
        self.noteslab=Button(master_wm,height=40,width=50,image=self.notes,bg='#e3e5e5',command=self.go_notes)
        self.noteslab.grid(row=5,column=5,padx=20,pady=20)


        self.egge_l=Label(master_wm,text='Eggeater',font=('Arial',8,'bold'),bg='#e3e5e5')
        self.egge_l.grid(row=6,column=1,padx=20,pady=0)

        self.wc_l=Label(master_wm,text='Wordcount',font=('Arial',8,'bold'),bg='#e3e5e5')
        self.wc_l.grid(row=6,column=2,padx=0,pady=0)

        self.stpw_l=Label(master_wm,text='Stopwatch',font=('Arial',8,'bold'),bg='#e3e5e5')
        self.stpw_l.grid(row=6,column=3,padx=20,pady=0)
        
        self.mup_l=Label(master_wm,text='Music Player',font=('Arial',8,'bold'),bg='#e3e5e5')
        self.mup_l.grid(row=6,column=4,padx=0,pady=0)

        self.notes_l=Label(master_wm,text='Notes',font=('Arial',8,'bold'),bg='#e3e5e5')
        self.notes_l.grid(row=6,column=5,padx=20,pady=0)


        self.qr=PhotoImage(file='DOPE Pictures\\Qrcode.png')
        self.qrlab=Button(master_wm,height=40,width=50,image=self.qr,bg='#e3e5e5',command=self.go_qrcode)
        self.qrlab.grid(row=7,column=1,padx=0,pady=20)

        self.ts=PhotoImage(file='DOPE Pictures\\Text2Speech.png')
        self.tslab=Button(master_wm,height=40,width=50,image=self.ts,bg='#e3e5e5',command=self.go_txt2speech)
        self.tslab.grid(row=7,column=2,padx=20,pady=20)

        self.fb=PhotoImage(file='DOPE Pictures\\Feedback.png')
        self.fblab=Button(master_wm,height=40,width=50,image=self.fb,bg='#e3e5e5',command=self.go_feedback)
        self.fblab.grid(row=7,column=3,padx=20,pady=20)


        self.qr_l=Label(master_wm,text='QR Generator',font=('Arial',8,'bold'),bg='#e3e5e5')
        self.qr_l.grid(row=8,column=1,padx=0,pady=0)

        self.ts_l=Label(master_wm,text='Text2Speech',font=('Arial',8,'bold'),bg='#e3e5e5')
        self.ts_l.grid(row=8,column=2,padx=20,pady=0)

        self.fb_l=Label(master_wm,text='Feedback',font=('Arial',8,'bold'),bg='#e3e5e5')
        self.fb_l.grid(row=8,column=3,padx=20,pady=0)


        self.ab_dev=Button(master_wm,text='About\nDeveloper',width=20,font=('Arial',12,'bold'),bg='#e3e5e5',command=self.about_dev)
        self.ab_dev.grid(row=9,column=1,columnspan=5,padx=20,pady=20)


        self.status=Label(master_wm,font=('Arial',7),text='Copyright \u00A9 and Trademarks \u2122 by DOPE Pvt. Ltd. Company.',bd=1,anchor=W,relief=SUNKEN)
        self.status.grid(row=10,column=1,columnspan=5,sticky='nsew')



    def about_dev(self):
        msgb.showinfo(title="DOPE Toolkit",message="Version:\t\t1.0\nDeveloped By:\tDOPE Pvt. Ltd. Company\nPowered By:\tHitman 47\nCopyright \u00A9 2018")



    def go_webcamera(self):
        web_cam_wm=Tk()
        WEBCAMERA=DOPE_Web_Camera(web_cam_wm)
        web_cam_wm.mainloop()



    def go_browser(self):
        brow_wm=Tk()
        BROWSER=DOPE_Browser(brow_wm)
        brow_wm.mainloop()



    def go_calendar(self):
        calen_wm=Tk()
        CALENDAR=DOPE_Calendar(calen_wm)
        calen_wm.mainloop()



    def go_calculator(self):
        calc_wm=Tk()
        CALCULATOR=DOPE_Calculator(calc_wm)
        calc_wm.mainloop()



    def go_clock(self):
        clock_wm=Tk()
        CLOCK=DOPE_Clock(clock_wm)
        clock_wm.mainloop()



    def go_eggeater(self):
        os.system('Other DOPE Apps\\DOPE Eggeater\\Eggeater.py')
        


    def go_music_player(self):
        music_wm=Tk()
        MUSICPLAYER=DOPE_Music_Player(music_wm)
        music_wm.mainloop()



    def go_notes(self):
        notes_wm=Tk()
        NOTES=DOPE_Notes(notes_wm)
        notes_wm.mainloop()



    def go_stopwatch(self):
        os.system('Other DOPE Apps\\DOPE Stopwatch\\Stopwatch.py')



    def go_wordcount(self):
        wordc_wm=Tk()
        WORDCOUNT=DOPE_Word_Count(wordc_wm)
        wordc_wm.mainloop()



    def go_feedback(self):
        os.system('Other DOPE Apps\\DOPE Feedback Form\\Feedback.py')



    def go_command_prompt(self):
        per_loc=os.getcwd()
        os.chdir("C:\\Windows\\system32\\")
        os.system('cmd.exe')
        os.chdir(per_loc)


    def go_color(self):
        color_wm=Tk()
        COLOR=DOPE_Color_Picker(color_wm)
        color_wm.mainloop()
        


    def go_crypt(self):
        CRYPTOGRAPHY=DOPE_Crypto_Graphy()



    def go_currency(self):
        curr_wm=Tk()
        CURRENCY=DOPE_Currency(curr_wm)
        curr_wm.mainloop()



    def go_dictionary(self):
        os.system('Other DOPE Apps\\DOPE Dictionary\\Oxford.pdf')
        


    def go_qrcode(self):
        qr_wm=Tk()
        QRCODE=DOPE_QR_Code(qr_wm)
        qr_wm.mainloop()



    def go_txt2speech(self):
        txt2sph_wm=Tk()
        TEXT2SPEECH=DOPE_Text_2_Speech(txt2sph_wm)
        txt2sph_wm.mainloop()





def main():
    root_wm=Tk()
    DOPE=DOPE_Toolkit(root_wm)
    root_wm.mainloop()




    
if __name__=="__main__":main()
