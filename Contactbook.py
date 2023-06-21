from tkinter import*
from tkinter import messagebox
import datetime
import sqlite3


con = sqlite3.connect("contacts1.db")
cur = con.cursor()

# cur.execute("""create table contacts1(
#     id integer primary key autoincrement,
#     f_name text,
#     l_name text,
#     phone_no integer,
#     email text,
#     address text
# )""")
#con.commit()


class contacts(object):

    def __init__(self,master):
        self.master = master
        #frames on root window

        self.top = Frame(master, height=100, bg="white")
        self.top.pack(fill=X)
        self.bottom = Frame(master, height=350, bg="blue")
        self.bottom.pack(fill=X)

        #label and date 
        #label title
        h1 = Label(self.top, text="Contactbook", font="mosarrate 18 bold", fg="blue", bg="white")
        h1.place(x=235, y=30)
        #for date
        d = datetime.datetime.now().date()
        dl = Label(self.top, text=d, font="mosarrate 9 bold", fg="blue", bg="white")
        dl.place(x=315, y=75)

        #for bottom frame
        #listbox and scroll bar
        
        lb = Listbox(self.bottom, width=30, height=16, font="mosarrate 11")
        sb = Scrollbar(self.bottom, orient=VERTICAL, width=10)
        sb.config(command=lb.yview)
        lb.config(yscrollcommand=sb.set)
        lb.grid(row=0, column=0, padx=(3,0), pady=(2,2))
        person = cur.execute("select * from 'contacts1'").fetchall()
        i=0
        j=1
        for p in person:
            lb.insert(i,str(j)+". "+p[1]+" "+p[2])
            i+=1
            j+=1
        sb.grid(row=0, column=1, sticky=N+S)

        
        #buttons for functions
        #addcontacts
        def addwind():
            addc_detail = Toplevel()
            addc_detail.geometry("400x400+660+160")
            addc_detail.title("ContactBook")
            addc_detail.resizable(0,0)

            #frames
            topc = Frame(addc_detail, height=100, bg="white")
            topc.pack(fill=X)
            bts = Frame(addc_detail, height=350, bg="royalblue")
            bts.pack(fill=X)

            #topc frame detail
            addcontact = Label(topc, text="Add Contact", font="mosarrate 18 bold", fg="royalblue", bg="white")
            addcontact.place(x=235, y=30)

            #bottomc frame detail
            cl = "royalblue"
            fl = Label(bts, text="First Name", font="mosarrate 13 bold", fg="white", bg=cl )
            fl.place(x=15, y=30)
            fe = Entry(bts, width=30, font="mosarrate 13")
            fe.place(x=110, y=30)
            
            ll = Label(bts, text="Last Name", font="mosarrate 13 bold", fg="white", bg=cl )
            ll.place(x=15, y=60)
            le = Entry(bts, width=30, font="mosarrate 13")
            le.place(x=110, y=60)

            pl = Label(bts, text="Phone", font="mosarrate 13 bold", fg="white", bg=cl )
            pl.place(x=15, y=90)
            pe = Entry(bts, width=30, font="mosarrate 13")
            pe.place(x=110, y=90)

            el = Label(bts, text="email", font="mosarrate 13 bold", fg="white", bg=cl )
            el.place(x=15, y=120)
            ee = Entry(bts, width=30, font="mosarrate 13")
            ee.place(x=110, y=120)

            al = Label(bts, text="Adress", font="mosarrate 13 bold", fg="white", bg=cl )
            al.place(x=15, y=150)
            ae = Text(bts, width=30, height=5, font="mosarrate 13")
            ae.place(x=110, y=150)

            #for data base
            def database():
                fname= fe.get()
                lname = le.get()
                phone = pe.get()
                email = ee.get()
                address = ae.get(1.0,'end-1c')
                if (fname and phone !=""):
                    try:
                        quary = "insert into 'contacts1'(f_name, l_name, phone_no, email, address) values(?,?,?,?,?)"
                        con.execute(quary,(fname,lname,phone,email,address))
                        con.commit()
                        addc_detail.destroy()
                        messagebox.showinfo("Done", "Contact Added")
                    except:
                        None            
                else:
                    addc_detail.destroy()
                    messagebox.showwarning("Failed","Please Add Name and Number")

            btna = Button(bts, text="Save", font="mosarrate 11 bold", fg="white", bg="green", width=9, command=database)
            btna.place(x=115, y=260)

        bt1= Button(self.bottom, text="Add", font="mosarrate 11 bold", fg="white", bg="gray", width=7, command=addwind)
        bt1.grid(row=0, column=2, sticky=N, padx=(30,0), pady=(15,0))

        #---------------for display detail of contact-----------------
        def con_detail():
            try:
                select = lb.curselection()
                pr_id = lb.get(select).split(".")[0]
                query = (f"select * from contacts1 where id={pr_id}")
                res = cur.execute(query).fetchone()
                
                #fatching the data
                fname = res[1]
                lname = res[2]
                phone = res[3]
                email = res[4]
                address = res[5]
                
                ec_wind = Toplevel()
                ec_wind.geometry("400x400+660+160")
                ec_wind.title("Contact Detail")
                ec_wind.resizable(0,0)

                #frame of ec_wind
                #topframe
                bcl = "royalblue"
                top = Frame(ec_wind, height=100, bg="white")
                top.pack(fill=X)
                bts = Frame(ec_wind, height=350, bg=bcl)
                bts.pack(fill=X)

                heading = Label(top, text="Contact Detail",font="mosarrate 18 bold", fg=bcl, bg="white")
                heading.place(x=226, y=30)
                #labels entry and textbox
                fl = Label(bts, text="First Name",font="mosarrate 13 bold", fg="white", bg=bcl)
                fl.place(x=15, y=20)
                fe = Entry(bts, font="mosarrate 13 bold", width=30 )
                fe.insert(0,fname)
                fe.config(state="disable")
                fe.place(x=110, y=20)
                    
                ll = Label(bts, text="Last Name", font="mosarrate 13 bold", fg="white", bg=bcl )
                ll.place(x=15, y=60)
                le = Entry(bts, width=30, font="mosarrate 13 bold")
                le.insert(0,lname)
                le.config(state="disable")
                le.place(x=110, y=60)

                pl = Label(bts, text="Phone", font="mosarrate 13 bold", fg="white", bg=bcl )
                pl.place(x=15, y=90)
                pe = Entry(bts, width=30, font="mosarrate 13 bold")
                pe.insert(0,phone)
                pe.config(state="disable")
                pe.place(x=110, y=90)

                el = Label(bts, text="email", font="mosarrate 13 bold", fg="white", bg=bcl )
                el.place(x=15, y=120)
                ee = Entry(bts, width=30, font="mosarrate 13 bold")
                ee.insert(0,email)
                ee.config(state="disable")
                ee.place(x=110, y=120)

                al = Label(bts, text="Adress", font="mosarrate 13 bold", fg="white", bg=bcl )
                al.place(x=15, y=150)
                at = Text(bts, width=30, height=5, font="mosarrate 13 bold", fg="black")
                at.insert(1.0,address)
                at.config(state="disable")
                at.place(x=110, y=150)

                def qt():
                    ec_wind.destroy()
                btna = Button(bts, text="Quit", font="mosarrate 11 bold", fg="white", bg="green", width=9, command=qt)
                btna.place(x=115, y=260)
            except:
                messagebox.showwarning("Invalid","Please Select a Contact")

        
        bt2= Button(self.bottom, text="Detail", font="mosarrate 11 bold", fg="white", bg="gray", width=7, command=con_detail)
        bt2.grid(row=0, column=2, sticky=N, padx=(30,0), pady=(50,0))
        
        #---------------for edit contact--------------------
        def con_s():
            try:
                select = lb.curselection()
                pr_id = lb.get(select).split(".")[0]
                
                query = (f"select * from contacts1 where id={pr_id}")
                res = cur.execute(query).fetchone()

                #fatching the data
                fname = res[1]
                lname = res[2]
                phone = res[3]
                email = res[4]
                address = res[5]

                
                ec_wind = Toplevel()
                ec_wind.geometry("400x400+660+160")
                ec_wind.title("Edit Contact")
                ec_wind.resizable(0,0)

                #frame of ec_wind
                #topframe
                bcl = "royalblue"
                top = Frame(ec_wind, height=100, bg="white")
                top.pack(fill=X)
                bts = Frame(ec_wind, height=350, bg=bcl)
                bts.pack(fill=X)

                heading = Label(top, text="Edit Contact",font="mosarrate 18 bold", fg=bcl, bg="white")
                heading.place(x=235, y=30)
                #labels entry and textbox
                fl = Label(bts, text="First Name",font="mosarrate 13 bold", fg="white", bg=bcl)
                fl.place(x=15, y=20)
                fe = Entry(bts, font="mosarrate 13", width=30 )
                fe.insert(0,fname)
                fe.place(x=110, y=20)
                    
                ll = Label(bts, text="Last Name", font="mosarrate 13 bold", fg="white", bg=bcl )
                ll.place(x=15, y=60)
                le = Entry(bts, width=30, font="mosarrate 13")
                le.insert(0,lname)
                le.place(x=110, y=60)

                pl = Label(bts, text="Phone", font="mosarrate 13 bold", fg="white", bg=bcl )
                pl.place(x=15, y=90)
                pe = Entry(bts, width=30, font="mosarrate 13")
                pe.insert(0,phone)
                pe.place(x=110, y=90)

                el = Label(bts, text="email", font="mosarrate 13 bold", fg="white", bg=bcl )
                el.place(x=15, y=120)
                ee = Entry(bts, width=30, font="mosarrate 13")
                ee.insert(0,email)
                ee.place(x=110, y=120)

                al = Label(bts, text="Adress", font="mosarrate 13 bold", fg="white", bg=bcl )
                al.place(x=15, y=150)
                at = Text(bts, width=30, height=5, font="mosarrate 13")
                at.insert(1.0,address)
                at.place(x=110, y=150)


                def edit_db():
                    fna = fe.get()
                    lna = le.get()
                    pno = pe.get()
                    eml = ee.get()
                    add = at.get(1.0, "end-1c")

                    query = (f"update contacts1 set f_name='{fna}', l_name='{lna}', phone_no={pno}, email='{eml}', address='{add}' where id={pr_id}")
                    cur.execute(query)
                    con.commit()
                    messagebox.showinfo("Successful", fna+" Contact Edited")

                btna = Button(bts, text="Save", font="mosarrate 11 bold", fg="white", bg="green", width=9, command=edit_db)
                btna.place(x=115, y=260)

            except Exception as e:
                e = messagebox.showwarning("Invalid","Please Select a Contact")


        bt3= Button(self.bottom, text="Edit", font="mosarrate 11 bold", fg="white", bg="gray", width=7, command=con_s)
        bt3.grid(row=0, column=2, sticky=N, padx=(30,0), pady=(85,0))

        def c_dlt_db():
            try:
                select_c = lb.curselection()
                per_id = lb.get(select_c).split(".")[0]
                per = lb.get(select_c).split(".")[1]
                
                query = (f"delete from contacts1 where id={per_id}")
                q = messagebox.askquestion("Warning","Do You Want to delete "+per)
                
                if (q == "yes"):
                    cur.execute(query)
                    con.commit()
                    messagebox.showinfo("Deleted", per+" deleted successfully")
            except Exception as e:
                e = messagebox.showwarning("Invalid","Please Select a Contact")

        
        bt4= Button(self.bottom, text="Delete", font="mosarrate 11 bold", fg="white", bg="gray", width=7, command=c_dlt_db)
        bt4.grid(row=0, column=2, sticky=N, padx=(30,0), pady=(120,0))

        # bt5= Button(self.bottom, text="Refresh", font="mosarrate 11 bold", fg="white", bg="gray", width=7, command=refresh)
        # bt5.grid(row=0, column=2, sticky=N, padx=(30,0), pady=(155,0))
        def abt():
            aw = Toplevel()
            aw.geometry("400x400+660+160")
            aw.title("About us")
            aw.resizable(0,0)
            tp = Frame(aw, height=100, bg="white")
            tp.pack(fill=X)
            bt= Frame(aw, height=350, bg="royalblue")
            bt.pack(fill=X)
            heading = Label(tp, text="About Us",font="mosarrate 18 bold", fg="royalblue", bg="white")
            heading.place(x=235, y=30)
            info = ("Developed by @shivamvr \nfor education perpose \npowered by Python and tkinter module \nIt's Open source design to develop with T&C \nThank You")
            lb = Label(bt, text=info, font="helvetica 10 bold", bg="royalblue", fg="white")
            lb.place(x=80, y=80)

        bt6= Button(self.bottom, text="About", font="mosarrate 11 bold", fg="white", bg="gray", width=7, command=abt)
        bt6.grid(row=0, column=2, sticky=N, padx=(30,0), pady=(155,0))
        #quit button and function 
        def qt():
            self.master.quit()
        bt7= Button(self.bottom, text="Quit", font="mosarrate 11 bold", fg="white", bg="gray", width=7, command=qt)
        bt7.grid(row=0, column=2, sticky=N, padx=(30,0), pady=(190,0))    

def main():
    root = Tk()
    root.geometry("400x400+650+150")
    root.title("Contactbook")
    app = contacts(root)
    root.resizable(0,0)
    root.mainloop()

if __name__ == '__main__':
    main()