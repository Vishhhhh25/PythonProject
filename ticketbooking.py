from tkinter import*
from tkinter import messagebox,ttk
import random

root=Tk()
root.title('Distance Calculator')
root.geometry('1280x1100')
bg_color='black'

city = ['Chh.Sambhajinagar', 'Chalisgaon' , 'Jalgaon' , 'Nashik' , 'Pune']

dict={ 'Chh.Sambhajinagar - Chalisgaon ':125 ,
        'Chh.Sambhajinagar - Jalgaon':100 ,
        'Chh.Sambhajinagar - Nashik':150 ,
        'Chh.Sambhajinagar - Pune':200 ,
        'Chalisgaon - Chh.Sambhajinagar':125,
        'Chalisgaon - Jalgaon ':50,
        'Chalisgaon - Nashik ' :110,
        'Chalisgaon - Pune ':250,
        'Jalgaon - Chh.Sambhajinagar ':100,
        'Jalgaon - Chalisgaon ':50 ,
        'Jalgaon - Nashik':250,
        'Jalgaon - Pune':300,
        'Nashik-Chh.Sambhajinagar':150,
        'Nashik-Chalisgaon':110,
        'Nashik-Jalgaon':250,
        'Nashik-Pune':150,
        'Pune-Chh.Sambhajinagar':200,
        'Pune-Chalisgaon':250,
        'Pune-Jalgaon':300,
        'Pune-Nashik':150
     
}
#=================variables================
person=IntVar()
c_name=StringVar()
c_phone=StringVar()
ticket_no=StringVar()
#======================================Frames=================

def varify():
    global dis
    a = combo_s.get()
    b = combo_d.get()
    p = person.get()
    d=a+'-'+b
    e=b+'-'+a
    if c_name.get() != "" or c_phone.get() != "":
        if c_phone.get().isnumeric() is not True:
            messagebox.showerror('Error','Phone number should be integer')
            return
    else:
        messagebox.showerror("Error", "Passenger detail are must")
        return
    if a!=b:
        if d in dict:
            dis= dict[d]
        elif e in dict:
            dis = dict[e]
    else:
        messagebox.showwarning('Warning ','Please select right root')
        return
    messagebox.showinfo('Varified','Successfully Vairified')

def gticket():
    try:
        welcome()
        p=person.get()
        textarea.insert(END,f"\n {55*'*'}")
        textarea.insert(END, f"\n\n From :\t\t {combo_s.get()}")
        textarea.insert(END, f"\n To :\t\t {combo_d.get()}")
        textarea.insert(END, f"\n {p} person ")
        textarea.insert(END, f"\nTotal distance :\t\t{dis}")
        textarea.insert(END, f"\n {35*'='}")
        textarea.insert(END, f"\nAmount :\t\t{2*p*dis}")
        textarea.insert(END, f"\n {35*'='}")
        textarea.insert(END, f"\n\n {55*'*'}")
        save_ticket()
    except Exception:
        messagebox.showwarning('Warrning','Pleaes varify the details first')
        clear()

def clear():
    c_name.set('')
    c_phone.set('')
    combo_s.set('select Source')
    combo_d.set('select destination')
    person.set(0)
    welcome()

def exit():
    op = messagebox.askyesno("Exit", "Do you really want to exit?")
    if op > 0:
        root.destroy()

def save_ticket():
    op=messagebox.askyesno("Save ticket","Do you want to download ticket ?")
    if op>0:
        ticket_details=textarea.get('1.0',END)
        f1=open("bills/"+str(ticket_no.get())+".txt","w")
        f1.write(ticket_details)
        f1.close()
        messagebox.showinfo("Saved",f"Ticket no, :{ticket_no.get()} Saved Successfully")
    else:
        return

def welcome():
    x = random.randint(1000, 9999)
    ticket_no.set(str(x))
    textarea.delete(1.0,END)
    textarea.insert(END,"\t\t Happy journey")
    textarea.insert(END,f"\n\nTicket Number:\t\t { ticket_no.get()}")
    textarea.insert(END,f"\nPassenger Name:\t\t { c_name.get()}")
    textarea.insert(END,f"\nPhone Number:\t\t { c_phone.get()}")
    textarea.configure(font='arial 15 bold')

title=Label(root,pady=2,text="Railway Ticket Generator",bd=12,bg=bg_color,fg='white',font=('times new roman', 25 ,'bold'),relief=GROOVE,justify=CENTER)
title.pack(fill=X)

#=================Product Frames=================
F1=LabelFrame(root,bd=10,relief=GROOVE,text='Passenger Details',font=('times new romon',15,'bold'),fg='gold',bg=bg_color)
F1.place(x=0,y=80,relwidth=1)

cname_lbl=Label(F1,text='Passenger Name',font=('times new romon',18,'bold'),bg=bg_color,fg='white').grid(row=0,column=0,padx=20,pady=5)
cname_txt=Entry(F1,width=15,textvariable=c_name,font='arial 15 bold',relief=SUNKEN,bd=7).grid(row=0,column=1,padx=10,pady=5)

cphone_lbl=Label(F1,text='Phone No. ',font=('times new romon',18,'bold'),bg=bg_color,fg='white').grid(row=0,column=2,padx=20,pady=5)
cphone_txt=Entry(F1,width=15,font='arial 15 bold',textvariable=c_phone,relief=SUNKEN,bd=7).grid(row=0,column=3,padx=10,pady=5)

F2 = LabelFrame(root, text='Root Details', font=('times new romon', 18, 'bold'), fg='gold',bg=bg_color)
F2.place(x=20, y=180,width=630,height=500)

source= Label(F2, text='Source', font=('times new roman',18, 'bold'), bg=bg_color, fg='lightgreen').grid(
row=0, column=0, padx=30, pady=20)
combo_s=ttk.Combobox(F2,font=('times new roman',18),state='readonly',value=city)
combo_s.grid(row=0,column=1,pady=10)
combo_s.set('select source')

des= Label(F2, text='Destination', font=('times new romon',18, 'bold'), bg=bg_color, fg='lightgreen').grid(
row=1, column=0, padx=30, pady=20)
combo_d=ttk.Combobox(F2,font=('times new roman',18),state='readonly',value=city)
combo_d.grid(row=1,column=1,pady=10)
combo_d.set('select destination')

n= Label(F2, text='Number of ticket', font=('times new romon',18, 'bold'), bg=bg_color, fg='lightgreen').grid(
row=2, column=0, padx=30, pady=20)
n_txt = Entry(F2, width=20,textvariable=person, font='arial 15 bold', relief=SUNKEN, bd=7).grid(row=2, column=1, padx=10,pady=20)

#========================Ticket area================
F3=Frame(root,relief=GROOVE,bd=10)
F3.place(x=700,y=180,width=500,height=500)

bill_title=Label(F3,text='Ticket',font='arial 15 bold',bd=7,relief=GROOVE).pack(fill=X)
scrol_y=Scrollbar(F3,orient=VERTICAL)
textarea=Text(F3,yscrollcommand=scrol_y)
scrol_y.pack(side=RIGHT,fill=Y)
scrol_y.config(command=textarea.yview)
textarea.pack()
welcome()
#=========================Buttons======================
btn1=Button(F2,text='Verify',font='arial 15 bold',command=varify,padx=5,pady=10,bg='lime',width=15)
btn1.grid(row=3,column=0,padx=10,pady=30)
btn2=Button(F2,text='Ticket',font='arial 15 bold',command=gticket,padx=5,pady=10,bg='lime',width=15)
btn2.grid(row=3,column=1,padx=10,pady=30)
btn3=Button(F2,text='Clear',font='arial 15 bold',padx=5,pady=10,command=clear,bg='lime',width=15)
btn3.grid(row=4,column=0,padx=10,pady=30)
btn4=Button(F2,text='Exit',font='arial 15 bold',padx=5,pady=10,command=exit,bg='lime',width=15)