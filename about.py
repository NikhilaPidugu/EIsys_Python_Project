from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
# from customer import Cust_Win
# from room import Room_Booking
# from details import DetailsRoom

class AboutHotel:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+230")

        #======title====
        lbl_title =Label(self.root,text="ABOUT HOTEL",font=("times new roman", 20, "bold"), bg="black",fg="gold",relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        img2=Image.open(r"C:\Users\CHAKRI\OneDrive\Desktop\pypro\img\logo.jpg") 
        img2=img2.resize((100,50),Image.LANCZOS) 
        self.photoimg2=ImageTk.PhotoImage(img2)

        lbling=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lbling.place(x=0,y=0, width=100,height=50)

        # ====mainframe====
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=60, width=1295, height=490)

        # Background image for main_frame
        bg_image = Image.open(r"C:\Users\CHAKRI\OneDrive\Desktop\pypro\img\bg.jpg")  # Update the path to your background image
        bg_image = bg_image.resize((1295, 490), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(bg_image)

        bg_label = Label(main_frame, image=self.bg_photo)
        bg_label.place(x=0, y=0, width=1295, height=490)

        canvas=Canvas(main_frame,width=1295,height=490)
        canvas.pack(fill="both",expand=True)
        canvas.create_image(0,0,image=self.bg_photo,anchor="nw")

        # Hotel information text
        hotel_info = (
            "Embodying the 110-year-old legacy of John Jacob Astor IV, our 5-star hotel in South Mumbai made its debut as the first St. Regis hotel in India. Every element of the hotel is infused "
            "with timeless elegance, from the luxurious rooms and suites to our expansive ballrooms, banquet halls, "
            "and outdoor venues, highlighted by our award-winning specialty restaurants with breathtaking panoramic views "
            "of the cityscape.\n\n"
            "The lavishly designed one-bedroom apartments make our hotel the perfect choice for families or those seeking "
            "extra room to relax. Nestled within the High Street Phoenix in Lower Parel, our hotel is just steps away from "
            "premium shopping & entertainment and major commercial business districts. Immerse yourself in luxury hotel amenities, "
            "including the treasured St. Regis Butler Service, as you explore the finest offerings of Mumbai."
        )

        
        canvas.create_text(647,245,text=hotel_info,font=("times new roman",18,"bold"),fill="white",justify=LEFT,width=1200)


if __name__ == "_main_":
    root = Tk()
    obj = AboutHotel(root)
    root.mainloop()       