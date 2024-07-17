from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from customer import Cust_Win
from room import Room_Booking
from details import DetailsRoom
from about import AboutHotel

class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")
        #==== img=======---------- 
        img1=Image.open(r"C:\Users\CHAKRI\OneDrive\Desktop\pypro\img\st.regis hotel.jpg")
        img1=img1.resize((1550,140),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lbling=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE) 
        lbling.place(x=0,y=8,width=1550,height=140)

        #====logo===
        img2=Image.open(r"C:\Users\CHAKRI\OneDrive\Desktop\pypro\img\logo.jpg") 
        img2=img2.resize((230,140),Image.LANCZOS) 
        self.photoimg2=ImageTk.PhotoImage(img2)

        lbling=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lbling.place(x=0,y=8, width=230,height=140)
        #title
        lbl_title =Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman", 40, "bold"), bg="black",fg="gold",relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)

        #====mainframe====
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)

        #=======menu====
        lbl_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)

         #====btnframe====
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=190)

        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)

        cust_btn=Button(btn_frame,text="ROOM",command=self.room_booking,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=1,column=0,pady=1)

        cust_btn=Button(btn_frame,text="DETAILS",command=self.details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=2,column=0,pady=1)

        cust_btn=Button(btn_frame,text="ABOUT",command=self.about,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=3,column=0,pady=1)

        cust_btn=Button(btn_frame,text="LOGOUT",command=self.logout,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=4,column=0,pady=1)

        #==== img=======---------- 
        img3=Image.open(r"C:\Users\CHAKRI\OneDrive\Desktop\pypro\img\regisoutlook.jpg")
        img3=img3.resize((1310,590),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lbling1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE) 
        lbling1.place(x=225,y=0,width=1310,height=590)

        #==== img=======---------- 
        img4=Image.open(r"C:\Users\CHAKRI\OneDrive\Desktop\pypro\img\food.jpg")
        img4=img4.resize((230,210),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lbling1=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE) 
        lbling1.place(x=0,y=225,width=230,height=210)

        #==== img=======---------- 
        img5=Image.open(r"C:\Users\CHAKRI\OneDrive\Desktop\pypro\img\roof.jpg")
        img5=img5.resize((230,190),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lbling1=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE) 
        lbling1.place(x=0,y=420,width=230,height=190)

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_Win(self.new_window)

    def room_booking(self):
        self.new_window=Toplevel(self.root)
        self.app=Room_Booking(self.new_window)  

    def details(self):
        self.new_window=Toplevel(self.root)
        self.app=DetailsRoom(self.new_window) 

    def about(self):
         self.new_window=Toplevel(self.root)
         self.app=AboutHotel(self.new_window)   

    def logout(self):
        self.root.destroy()
        


if __name__=="__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()    
    