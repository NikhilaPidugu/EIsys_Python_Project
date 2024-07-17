from tkinter import*
from PIL import  Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox

class Cust_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+230")


        #=========variables=======
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))
        
        self.var_cust_name=StringVar()
        self.var_cust_gender=StringVar()
        self.var_cust_mobno=StringVar()
        self.var_cust_email=StringVar()
        self.var_cust_nation=StringVar()
        self.var_cust_id=StringVar()
        self.var_cust_addr=StringVar()

        #======title====
        lbl_title =Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman", 20, "bold"), bg="black",fg="gold",relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        img2=Image.open(r"C:\Users\CHAKRI\OneDrive\Desktop\pypro\img\logo.jpg") 
        img2=img2.resize((100,50),Image.LANCZOS) 
        self.photoimg2=ImageTk.PhotoImage(img2)

        lbling=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lbling.place(x=0,y=0, width=100,height=50)


        #===lalbelframe===
        labelFrameleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("times new roman", 12, "bold"),padx=2)
        labelFrameleft.place(x=5,y=50,width=425,height=490)

        #custRef
        lbl_cust_ref=Label(labelFrameleft,text="Customer Ref:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        enty_ref=ttk.Entry(labelFrameleft,textvariable=self.var_ref,font=("times new roman",14,"bold"),width=29,state="readonly")
        enty_ref.grid(row=0,column=1)

        #custName
        custName=Label(labelFrameleft,text="Customer Name:",font=("times new roman",12,"bold"),padx=2,pady=6)
        custName.grid(row=1,column=0,sticky=W)

        txtcname=ttk.Entry(labelFrameleft,textvariable=self.var_cust_name,font=("times new roman",14,"bold"),width=29)
        txtcname.grid(row=1,column=1)

        #custGender Custbox
        lbl_gender=Label(labelFrameleft,text="Gender:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_gender.grid(row=2,column=0,sticky=W)
        combo_gender=ttk.Combobox(labelFrameleft,textvariable=self.var_cust_gender,font=("times new roman",14,"bold"),width=27,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=2,column=1)

        #custMobileno
        cust_no=Label(labelFrameleft,text="Mobile No:",font=("times new roman",12,"bold"),padx=2,pady=6)
        cust_no.grid(row=3,column=0,sticky=W)

        txtcno=ttk.Entry(labelFrameleft,textvariable=self.var_cust_mobno,font=("times new roman",14,"bold"),width=29)
        txtcno.grid(row=3,column=1)

        #custEmail
        custemail=Label(labelFrameleft,text="Email Id:",font=("times new roman",12,"bold"),padx=2,pady=6)
        custemail.grid(row=4,column=0,sticky=W)

        txtcem=ttk.Entry(labelFrameleft,textvariable=self.var_cust_email,font=("times new roman",14,"bold"),width=29)
        txtcem.grid(row=4,column=1)

        #custNationalty
        custNation=Label(labelFrameleft,text="Nationality:",font=("times new roman",12,"bold"),padx=2,pady=6)
        custNation.grid(row=5,column=0,sticky=W)
        combo_nation=ttk.Combobox(labelFrameleft,textvariable=self.var_cust_nation,font=("times new roman",14,"bold"),width=27,state="readonly")
        combo_nation["value"]=("Indian","American","Germans","Canadian","British","Spaniard")
        combo_nation.current(0)
        combo_nation.grid(row=5,column=1)

        #id proof
        cid=Label(labelFrameleft,text="ID Proof:",font=("times new roman",12,"bold"),padx=2,pady=6)
        cid.grid(row=6,column=0,sticky=W)
        combo_id=ttk.Combobox(labelFrameleft,textvariable=self.var_cust_id,font=("times new roman",14,"bold"),width=27,state="readonly")
        combo_id["value"]=("Aadhar Card","Driving Liscense","Passport")
        combo_id.current(0)
        combo_id.grid(row=6,column=1)


        #custaddress
        custadd=Label(labelFrameleft,text="Address:",font=("times new roman",12,"bold"),padx=2,pady=6)
        custadd.grid(row=7,column=0,sticky=W)

        txtAddr=ttk.Entry(labelFrameleft,textvariable=self.var_cust_addr,font=("times new roman",14,"bold"),width=29)
        txtAddr.grid(row=7,column=1)

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

        #===table frame serach system=====
        tabelFrame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("times new roman", 12, "bold"),padx=2)
        tabelFrame.place(x=435,y=50,width=860,height=490)

        lblSearchBy=Label(tabelFrame,font=("times new roman",12,"bold"),text="Search By:",bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        combo_search=ttk.Combobox(tabelFrame,textvariable=self.search_var,font=("times new roman",14,"bold"),width=24,state="readonly")
        combo_search["value"]=("Mobile","Ref")
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
        tbl_frame.place(x=0,y=50,width=860,height=360)

        scroll_x=ttk.Scrollbar(tbl_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(tbl_frame,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(tbl_frame,column=("ref","name","gender","mobileno","email",
                                             "nationality","idproof","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref",text="Refer No")
        self.Cust_Details_Table.heading("name",text="Name")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("mobileno",text="Mobile No")
        self.Cust_Details_Table.heading("email",text="Email")
        self.Cust_Details_Table.heading("nationality",text="Nationality")
        self.Cust_Details_Table.heading("idproof",text="Id Proof")
        self.Cust_Details_Table.heading("address",text="Address")

        self.Cust_Details_Table["show"]="headings"

        self.Cust_Details_Table.column("ref",width=120)
        self.Cust_Details_Table.column("name",width=120)
        self.Cust_Details_Table.column("gender",width=120)
        self.Cust_Details_Table.column("mobileno",width=120)
        self.Cust_Details_Table.column("email",width=120)
        self.Cust_Details_Table.column("nationality",width=120)
        self.Cust_Details_Table.column("idproof",width=120)
        self.Cust_Details_Table.column("address",width=120)

        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
            if self.var_cust_mobno.get()=="" or self.var_cust_name.get()=="":
                messagebox.showerror("Error","All fields are required")
            else:
                try:
                    conn=mysql.connector.connect(host="localhost",username="root",password="#scan2005",database="management")
                    my_cursor=conn.cursor()
                    my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_ref.get(),
                                                                                        self.var_cust_name.get(),
                                                                                        self.var_cust_gender.get(),
                                                                                        self.var_cust_mobno.get(),
                                                                                        self.var_cust_email.get(),
                                                                                        self.var_cust_nation.get(),
                                                                                        self.var_cust_id.get(),
                                                                                        self.var_cust_addr.get()   
                                                                                                   ))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success","Customer has been added",parent=self.root)
                except Exception as es:
                     messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)    

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="#scan2005",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close() 

    def get_cursor(self,event=""):
        cursor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cursor_row)
        row=content["values"]      

        self.var_ref.set(row[0]), 
        self.var_cust_name.set(row[1]),
        self.var_cust_gender.set(row[2]),
        self.var_cust_mobno.set(row[3]),
        self.var_cust_email.set(row[4]),
        self.var_cust_nation.set(row[5]),
        self.var_cust_id.set(row[6]),
        self.var_cust_addr.set(row[7])

    def update(self):
        if self.var_cust_mobno.get()=="":
            messagebox.showerror("Error,Please enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="#scan2005",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update customer set name=%s,gender=%s,mobileno=%s,email=%s,nationality=%s,idproof=%s,address=%s where ref=%s",(
                                                                                                                            self.var_cust_name.get(),
                                                                                                                            self.var_cust_gender.get(),
                                                                                                                            self.var_cust_mobno.get(),
                                                                                                                            self.var_cust_email.get(),
                                                                                                                            self.var_cust_nation.get(),
                                                                                                                            self.var_cust_id.get(),
                                                                                                                            self.var_cust_addr.get(),
                                                                                                                            self.var_ref.get()  
                                                                                                                          ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("update","Customer details has been updated successfully",parent=self.root)
    
    def nDelete(self):
        nDelete=messagebox.askyesno("Hotel Management System","Do you want delete this customer",parent=self.root)
        if nDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="#scan2005",database="management")
            my_cursor=conn.cursor()
            query="delete from customer where ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not nDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()     

    def reset(self):
        self.var_ref.set(""),
        self.var_cust_name.set(""),
        #self.var_cust_gender.set(""),
        self.var_cust_mobno.set(""),
        self.var_cust_email.set(""),
        #self.var_cust_nation.set(""),
        #self.var_cust_id.set(""),
        self.var_cust_addr.set("")
        
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="#scan2005",database="management")
        my_cursor=conn.cursor()

        my_cursor.execute("select * from customer where "+str(self.search_var.get())+ " LIKE'%" +str(self.txt_search.get())+ "%' ")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()    

if __name__=="__main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()
