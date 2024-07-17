from tkinter import*
from PIL import  Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class Room_Booking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+230")

        #===variables==
        self.var_con=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomType=StringVar()
        self.var_roomAvai=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actcost=StringVar()
        self.var_totcost=StringVar()


        #======title====
        lbl_title =Label(self.root,text="ROOM BOOKING DETAILS",font=("times new roman", 20, "bold"), bg="black",fg="gold",relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        #==logo==
        img2=Image.open(r"C:\Users\CHAKRI\OneDrive\Desktop\pypro\img\logo.jpg") 
        img2=img2.resize((100,50),Image.LANCZOS) 
        self.photoimg2=ImageTk.PhotoImage(img2)

        lbling=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lbling.place(x=0,y=0, width=100,height=50)

        #===lalbelframe===
        labelFrameleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Booking",font=("times new roman", 12, "bold"),padx=2)
        labelFrameleft.place(x=5,y=50,width=425,height=490)

        #cust Contact
        lbl_cust_con=Label(labelFrameleft,text="Customer Contact:",font=("times new roman",12,"bold"),padx=2,pady=7)
        lbl_cust_con.grid(row=0,column=0,sticky=W)

        enty_con=ttk.Entry(labelFrameleft,textvariable=self.var_con,font=("times new roman",14,"bold"),width=20)
        enty_con.grid(row=0,column=1,sticky=W)

        #fetch data button
        btnFetch=Button(labelFrameleft,command=self.fetch_con,text="FETCH",font=("times new roman",13,"bold"),bg="black",fg="gold",width=6)
        btnFetch.place(x=346,y=3)

        #Check_in date
        check_in=Label(labelFrameleft,text="Check_In Date:",font=("times new roman",12,"bold"),padx=2,pady=6)
        check_in.grid(row=1,column=0,sticky=W)

        txtcheckin=ttk.Entry(labelFrameleft,textvariable=self.var_checkin,font=("times new roman",14,"bold"),width=27)
        txtcheckin.grid(row=1,column=1)

        #Check_out date
        check_out=Label(labelFrameleft,text="Check_Out Date:",font=("times new roman",12,"bold"),padx=2,pady=6)
        check_out.grid(row=2,column=0,sticky=W)

        txtcheckout=ttk.Entry(labelFrameleft,textvariable=self.var_checkout,font=("times new roman",14,"bold"),width=27)
        txtcheckout.grid(row=2,column=1)

        #Room type
        lbl_room=Label(labelFrameleft,text="Room Type:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_room.grid(row=3,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",password="#scan2005",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select roomType from details")
        ide=my_cursor.fetchall()

        combo_checkout=ttk.Combobox(labelFrameleft,textvariable=self.var_roomType,font=("times new roman",14,"bold"),width=26,state="readonly")
        combo_checkout["value"]=ide
        combo_checkout.current(0)
        combo_checkout.grid(row=3,column=1)

        #Available Room
        lblRoomAvai=Label(labelFrameleft,text="Available Room:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblRoomAvai.grid(row=4,column=0,sticky=W)

        #txtravai=ttk.Entry(labelFrameleft,textvariable=self.var_roomAvai,font=("times new roman",14,"bold"),width=27)
        #txtravai.grid(row=4,column=1)
        conn=mysql.connector.connect(host="localhost",username="root",password="#scan2005",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select roomNo from details")
        row=my_cursor.fetchall()

        combo_checkout=ttk.Combobox(labelFrameleft,textvariable=self.var_roomAvai,font=("times new roman",14,"bold"),width=26,state="readonly")
        combo_checkout["value"]=row
        combo_checkout.current(0)
        combo_checkout.grid(row=4,column=1)

        #Meal
        custmeal=Label(labelFrameleft,text="Meal:",font=("times new roman",12,"bold"),padx=2,pady=6)
        custmeal.grid(row=5,column=0,sticky=W)

        txtcmeal=ttk.Entry(labelFrameleft,textvariable=self.var_meal,font=("times new roman",14,"bold"),width=27)
        txtcmeal.grid(row=5,column=1)

        #No.of days
        cust_stay=Label(labelFrameleft,text="No.of Days:",font=("times new roman",12,"bold"),padx=2,pady=6)
        cust_stay.grid(row=6,column=0,sticky=W)

        txtcstay=ttk.Entry(labelFrameleft,textvariable=self.var_noofdays,font=("times new roman",14,"bold"),width=27)
        txtcstay.grid(row=6,column=1)

        #Paid tax
        cusPaidTax=Label(labelFrameleft,text="Tax Paid:",font=("times new roman",12,"bold"),padx=2,pady=6)
        cusPaidTax.grid(row=7,column=0,sticky=W)

        txtpaidtax=ttk.Entry(labelFrameleft,textvariable=self.var_paidtax,font=("times new roman",14,"bold"),width=27)
        txtpaidtax.grid(row=7,column=1)

        #Sub total
        lblSTcost=Label(labelFrameleft,text="Sub Cost:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblSTcost.grid(row=8,column=0,sticky=W)

        txtscost=ttk.Entry(labelFrameleft,textvariable=self.var_actcost,font=("times new roman",14,"bold"),width=27)
        txtscost.grid(row=8,column=1)

        #Total cost
        lblTcost=Label(labelFrameleft,text="Total Cost:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblTcost.grid(row=9,column=0,sticky=W)

        txtcost=ttk.Entry(labelFrameleft,textvariable=self.var_totcost,font=("times new roman",14,"bold"),width=27)
        txtcost.grid(row=9,column=1)

        #===Bill Button===
        btnBill=Button(labelFrameleft,text="BILL",command=self.total,font=("times new roman",13,"bold"),bg="black",fg="gold",width=9)
        btnBill.grid(row=10,column=0,padx=1,sticky=W)

        #===buttons===
        btn_frame=Frame(labelFrameleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="ADD",command=self.add_data,font=("times new roman",13,"bold"),bg="black",fg="gold",width=9)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="UPDATE",command=self.update,font=("times new roman",13,"bold"),bg="black",fg="gold",width=9)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="DELETE",command=self.nDelete,font=("times new roman",13,"bold"),bg="black",fg="gold",width=9)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="RESET",command=self.reset,font=("times new roman",13,"bold"),bg="black",fg="gold",width=9)
        btnReset.grid(row=0,column=3,padx=1)

        #==ight side image==
        img3=Image.open(r"C:\Users\CHAKRI\OneDrive\Desktop\pypro\img\hotelroom.jpg") 
        img3=img3.resize((500,300),Image.LANCZOS) 
        self.photoimg3=ImageTk.PhotoImage(img3)
        lbling=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lbling.place(x=760,y=55,width=500,height=300)


        #===table frame search system=====
        tabelFrame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("times new roman", 12, "bold"),padx=2)
        tabelFrame.place(x=435,y=280,width=860,height=260)

        lblSearchBy=Label(tabelFrame,font=("times new roman",12,"bold"),text="Search By:",bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        combo_search=ttk.Combobox(tabelFrame,textvariable=self.search_var,font=("times new roman",14,"bold"),width=24,state="readonly")
        combo_search["value"]=("Contact","Room")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        txtSear=ttk.Entry(tabelFrame,textvariable=self.txt_search,font=("times new roman",14,"bold"),width=24)
        txtSear.grid(row=0,column=2,padx=2)

        btnSearch=Button(tabelFrame,text="SEARCH",command=self.search,font=("times new roman",13,"bold"),bg="black",fg="gold",width=9)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(tabelFrame,text="SHOW ALL",command=self.fetch_data,font=("times new roman",13,"bold"),bg="black",fg="gold",width=9)
        btnShowAll.grid(row=0,column=4,padx=1)

        #===show data table=====
        tbl_frame=Frame(tabelFrame,bd=2,relief=RIDGE)
        tbl_frame.place(x=0,y=50,width=860,height=180)

        scroll_x=ttk.Scrollbar(tbl_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(tbl_frame,orient=VERTICAL)

        self.room_Table=ttk.Treeview(tbl_frame,column=("contact","checkin","checkout","roomType","roomAvailable",
                                             "meal","noOfDays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_Table.xview)
        scroll_y.config(command=self.room_Table.yview)

        self.room_Table.heading("contact",text="Contact")
        self.room_Table.heading("checkin",text="Checkin")
        self.room_Table.heading("checkout",text="Checkout")
        self.room_Table.heading("roomType",text="Room Type")
        self.room_Table.heading("roomAvailable",text="Room Available")
        self.room_Table.heading("meal",text="Meal")
        self.room_Table.heading("noOfDays",text="NoOfDays")

        self.room_Table["show"]="headings"

        self.room_Table.column("contact",width=120)
        self.room_Table.column("checkin",width=120)
        self.room_Table.column("checkout",width=120)
        self.room_Table.column("roomType",width=120)
        self.room_Table.column("roomAvailable",width=120)
        self.room_Table.column("meal",width=120)
        self.room_Table.column("noOfDays",width=120)

        self.room_Table.pack(fill=BOTH,expand=1)
        self.room_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    #======add data====
    def add_data(self):
            if self.var_con.get()=="" or self.var_checkin.get()=="":
                messagebox.showerror("Error","All fields are required")
            else:
                try:
                    conn=mysql.connector.connect(host="localhost",username="root",password="#scan2005",database="management")
                    my_cursor=conn.cursor()
                    my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_con.get(),
                                                                                        self.var_checkin.get(),
                                                                                        self.var_checkout.get(),
                                                                                        self.var_roomType.get(),
                                                                                        self.var_roomAvai.get(),
                                                                                        self.var_meal.get(),
                                                                                        self.var_noofdays.get()
                                                                                                   )) 
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success","Room has been Booked",parent=self.root)
                except Exception as es:
                     messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)    
    
    #======fetch data====
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="#scan2005",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_Table.delete(*self.room_Table.get_children())
            for i in rows:
                self.room_Table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #====get cursor===
    def get_cursor(self,event=""):
        cursor_row=self.room_Table.focus()
        content=self.room_Table.item(cursor_row)
        row=content["values"]      

        self.var_con.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomType.set(row[3]),
        self.var_roomAvai.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noofdays.set(row[6])

    def update(self):
        if self.var_con.get()=="":
            messagebox.showerror("Error,Please enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="#scan2005",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update room set checkin=%s,checkout=%s,roomType=%s,roomAvailable=%s,meal=%s,noOfDays=%s where contact=%s",(
                                                                                                                            self.var_checkin.get(),
                                                                                                                            self.var_checkout.get(),
                                                                                                                            self.var_roomType.get(),
                                                                                                                            self.var_roomAvai.get(),
                                                                                                                            self.var_meal.get(),
                                                                                                                            self.var_noofdays.get(),
                                                                                                                            self.var_con.get()  
                                                                                                                          ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("update","Room details has been updated successfully",parent=self.root)
    
    def nDelete(self):
        nDelete=messagebox.askyesno("Hotel Management System","Do you want delete this room booking?",parent=self.root)
        if nDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="#scan2005",database="management")
            my_cursor=conn.cursor()
            query="delete from room where contact=%s"
            value=(self.var_con.get(),)
            my_cursor.execute(query,value)
        else:
            if not nDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()     

    def reset(self):
        self.var_con.set(""),
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        self.var_roomType.set(""),
        self.var_roomAvai.set(""),
        self.var_meal.set(""),
        self.var_noofdays.set("")   

        self.var_paidtax.set("")
        self.var_actcost.set("")
        self.var_totcost.set("")

    #===All data fetch===========
    def fetch_con(self):
        if self.var_con.get()=="":
            messagebox.showerror("Error","Please enter Contact Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="#scan2005",database="management")
            my_cursor=conn.cursor()
            query=("select name from customer where mobileno=%s")
            value=(self.var_con.get(),)      
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","Number not found",parent=self.root)
            else:
                conn.commit()
                conn.close()
             
             #======Name========
                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataframe.place(x=450,y=55,width=300,height=180)

                lblName=Label(showDataframe,text="Name:",font=("times new roman",12,"bold"))
                lblName.place(x=0,y=0)    

                lbl=Label(showDataframe,text=row,font=("times new roman",12,"bold"))
                lbl.place(x=90,y=0)

             #=====Gender=====
                conn=mysql.connector.connect(host="localhost",username="root",password="#scan2005",database="management")
                my_cursor=conn.cursor()
                query=("select gender from customer where mobileno=%s")
                value=(self.var_con.get(),)      
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataframe,text="Gender:",font=("times new roman",12,"bold"))
                lblGender.place(x=0,y=30)    

                lblg=Label(showDataframe,text=row,font=("times new roman",12,"bold"))
                lblg.place(x=90,y=30)

                #=======Email======
                conn=mysql.connector.connect(host="localhost",username="root",password="#scan2005",database="management")
                my_cursor=conn.cursor()
                query=("select email from customer where mobileno=%s")
                value=(self.var_con.get(),)      
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblEmail=Label(showDataframe,text="Email:",font=("times new roman",12,"bold"))
                lblEmail.place(x=0,y=60)    

                lble=Label(showDataframe,text=row,font=("times new roman",12,"bold"))
                lble.place(x=90,y=60)

                #=====Nationality======
                conn=mysql.connector.connect(host="localhost",username="root",password="#scan2005",database="management")
                my_cursor=conn.cursor()
                query=("select nationality from customer where mobileno=%s")
                value=(self.var_con.get(),)      
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblNation=Label(showDataframe,text="Nationality:",font=("times new roman",12,"bold"))
                lblNation.place(x=0,y=90)    

                lbln=Label(showDataframe,text=row,font=("times new roman",12,"bold"))
                lbln.place(x=90,y=90)

                #=====Address======
                conn=mysql.connector.connect(host="localhost",username="root",password="#scan2005",database="management")
                my_cursor=conn.cursor()
                query=("select address from customer where mobileno=%s")
                value=(self.var_con.get(),)      
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblAddr=Label(showDataframe,text="Address:",font=("times new roman",12,"bold"))
                lblAddr.place(x=0,y=120)
    

                lblad=Label(showDataframe,text=row,font=("times new roman",12,"bold"))
                lblad.place(x=90,y=120)
    #====search system====            
    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="#scan2005",database="management")
        my_cursor=conn.cursor()

        my_cursor.execute("select * from room where "+str(self.search_var.get())+ " LIKE'%" +str(self.txt_search.get())+ "%' ")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_Table.delete(*self.room_Table.get_children())
            for i in rows:
                self.room_Table.insert("",END,values=i)
            conn.commit()
        conn.close()   




    #===total=====            
    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y")
        self.var_noofdays.set(abs(outDate-inDate).days)

        if (self.var_meal.get()=="Breakfast" and self.var_roomType.get()=="Luxury"):
            q1=float(300)
            q2=float(1000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            SubTax="Rs."+str("%.2f"%((q5)))
            TotTax="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actcost.set(SubTax)
            self.var_totcost.set(TotTax)

        elif (self.var_meal.get()=="Lunch" and self.var_roomType.get()=="Double"):
            q1=float(500)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            SubTax="Rs."+str("%.2f"%((q5)))
            TotTax="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actcost.set(SubTax)
            self.var_totcost.set(TotTax)

        elif (self.var_meal.get()=="Breakfast" and self.var_roomType.get()=="Single"):
            q1=float(300)
            q2=float(500)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            SubTax="Rs."+str("%.2f"%((q5)))
            TotTax="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actcost.set(SubTax)
            self.var_totcost.set(TotTax)        

        elif (self.var_meal.get()=="Breakfast" and self.var_roomType.get()=="Double"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            SubTax="Rs."+str("%.2f"%((q5)))
            TotTax="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actcost.set(SubTax)
            self.var_totcost.set(TotTax)

        elif (self.var_meal.get()=="Lunch" and self.var_roomType.get()=="Single"):
            q1=float(500)
            q2=float(500)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            SubTax="Rs."+str("%.2f"%((q5)))
            TotTax="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actcost.set(SubTax)
            self.var_totcost.set(TotTax)

        elif (self.var_meal.get()=="Lunch" and self.var_roomType.get()=="Luxury"):
            q1=float(500)
            q2=float(1000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            SubTax="Rs."+str("%.2f"%((q5)))
            TotTax="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actcost.set(SubTax)
            self.var_totcost.set(TotTax)

        elif (self.var_meal.get()=="Dinner" and self.var_roomType.get()=="Single"):
            q1=float(600)
            q2=float(500)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            SubTax="Rs."+str("%.2f"%((q5)))
            TotTax="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actcost.set(SubTax)
            self.var_totcost.set(TotTax)

        elif (self.var_meal.get()=="Dinner" and self.var_roomType.get()=="Double"):
            q1=float(600)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            SubTax="Rs."+str("%.2f"%((q5)))
            TotTax="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actcost.set(SubTax)
            self.var_totcost.set(TotTax)

        elif (self.var_meal.get()=="Dinner" and self.var_roomType.get()=="Luxury"):
            q1=float(600)
            q2=float(1000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            SubTax="Rs."+str("%.2f"%((q5)))
            TotTax="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actcost.set(SubTax)
            self.var_totcost.set(TotTax)  

        else:
            messagebox.showerror("Error","Select correct meal type and room type")                      
        






if __name__=="__main__":
    root=Tk()
    obj=Room_Booking(root)
    root.mainloop()        