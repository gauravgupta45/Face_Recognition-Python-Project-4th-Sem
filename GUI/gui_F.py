from tkinter import*
from tkinter import messagebox as ms
import webbrowser
import sqlite3
import time

win=Tk()
win.geometry("700x670")
win.title("GG's Web")
win.iconbitmap("C:\\Users\\laptop\\Documents\\GG's Doc\\Programming\\Python\\GUI\\Icons\\bitmap_5.ico")

# Win1 Canvas and Variables
canvas1 = Canvas(win,width=700,height=35,bg="Green")
canvas1.place(x=0,y=0)

canvas2 = Canvas(win,width=700,height=45,bg="#c4bcbc")
canvas2.place(x=0,y=35)

canvas_middle = Canvas(win,width=700,height=100)
canvas_middle.place(x=0,y=80)

canvas3 = Canvas(win,width=259,height=344)
canvas3.place(x=30,y=195)

canvas4 = Canvas(win,width=259,height=344)
canvas4.place(x=400,y=195)

canvas_end = Canvas(win,width=700,height=110)
canvas_end.place(x=0,y=550)

final_message=Label(win,text="",font=("Grange",12))
final_message_window = canvas_end.create_window(34, 54, window=final_message,anchor=NW)

Fullname = StringVar(canvas3)
Day = StringVar(canvas3)
Month = StringVar(canvas3)
Year = StringVar(canvas3)
Gender = StringVar(canvas3)
Email = StringVar(canvas3)
Password = StringVar(canvas3)
Country = StringVar(canvas4)
Address_1 = StringVar(canvas4)
Address_2 = StringVar(canvas4)
City = StringVar(canvas4)
Zip_Code = IntVar(canvas4)
Phone = IntVar(canvas4)
Terms = IntVar(canvas_end)


def close_win():
    win.destroy()

def win_signup_alert():
    ms.showerror('Idiot','You are already on Sign Up page')


def win_login():
    win3=Toplevel(win)
    win3.geometry("400x350")
    win3.title("GG's Login")
    win3.iconbitmap("C:\\Users\\laptop\\Documents\\GG's Doc\\Programming\\Python\\GUI\\Icons\\bitmap_4.ico")

    def close_win3():
        win3.destroy()

    canvas1_win3 = Canvas(win3,width=400,height=350,bg="Grey")                          #
    canvas1_win3.place(x=0,y=0)


    canvas1_win3.create_text(200,65,text="Candidate Login",fill='Black',font=("Myriad Pro Light",16))



    idk = PhotoImage(file="C:\\Users\\laptop\\Documents\\GG's Doc\\Programming\\Python\\GUI\\Icons\\login.png")
    canvas1_win3.create_image(100,65,image=idk)


    canvas1_win3.create_text(80,120,text="Email Id",fill='Black')
    entry_id=Entry(win3,width=35,textvar=Email)
    canvas1_win3.create_window(165,140,window=entry_id)
    entry_id.delete(0, 'end')

    canvas1_win3.create_text(85,180,text="Password",fill='Black')
    entry_pwd=Entry(win3,width=35,textvar=Password,show="*")
    canvas1_win3.create_window(165,200,window=entry_pwd)
    entry_pwd.delete(0, 'end')


    def db_signin():
        conn = sqlite3.connect('GUI_F.db')
        with conn:
            cursor=conn.cursor()
        find_user = ('SELECT * FROM GUI_Table WHERE Email = ? and Password = ?')
        cursor.execute(find_user,[(Email.get()),(Password.get())])
        result = cursor.fetchall()
        if result:
            win4=Toplevel(win)
            win4.geometry("300x250")
            win4.title("GG's Login")
            win4.iconbitmap("C:\\Users\\laptop\\Documents\\GG's Doc\\Programming\\Python\\GUI\\Icons\\bitmap_4.ico")

            canvas1_win4 = Canvas(win4,width=300,height=250,bg="Green")                          #
            canvas1_win4.place(x=0,y=0)
            success_login_msg=canvas1_win4.create_text(150,125,text="Succesfully Logined!",fill="#FF8F00",font=("Boulder Bold",18))

        else:
            ms.showerror('Oopsie!','Username or Password is wrong.')

    btn_login = Button(win3,text="Login",fg="Black",command=db_signin)
    canvas1_win3.create_window(80,250,window=btn_login)

    canvas1_win3.create_text(145,276,text="If you have not registerd, please ",fill="Black")
    sign_up = Button(win3,text="Sign Up",fg="Blue",bg="Grey",relief=SUNKEN,borderwidth=0,cursor="hand2",command=close_win3)
    sign_up_window = canvas1_win3.create_window(227, 265, anchor=NW, window=sign_up)




url_fb='http://www.facebok.com'
url_tw='https://twitter.com'
url_ig='http://www.instagram.com'
url_yt='http://www.youtube.com'
url_gg='https://ggcanwrite.wordpress.com/'
url_gmail='https://mail.google.com/'

def OpenFb():
    webbrowser.open_new(url_fb)
def OpenTw():
    webbrowser.open_new(url_tw)
def OpenIg():
    webbrowser.open_new(url_ig)
def OpenYt():
    webbrowser.open_new(url_yt)
def OpenGG():
    webbrowser.open_new(url_gg)
def OpenGmail():
    webbrowser.open_new(url_gmail)

def db_signup():
    name_value = Fullname.get()
    day_value = Day.get()
    month_value = Month.get()
    year_value = Year.get()
    gender_value = Gender.get()
    email_value = Email.get()
    pwd_value = Password.get()
    country_value=Country.get()
    add_value1=Address_1.get()
    add_value2=Address_2.get()
    city_value=City.get()
    zip_value=Zip_Code.get()
    phone_value=Phone.get()
    term_value=Terms.get()

    if len(Fullname.get())!=0:
        conn = sqlite3.connect('GUI_F.db')
        with conn:
            cursor=conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS GUI_Table (Fullname TEXT,Gender TEXT,Email TEXT,Password TEXT,Country TEXT,Address TEXT,City TEXT,Zip_Code INT,Phone INT)')
        cursor.execute('INSERT INTO GUI_Table VALUES(?,?,?,?,?,?,?,?,?)',(name_value,gender_value,email_value,pwd_value,country_value,add_value1,city_value,zip_value,phone_value))
        conn.commit()
        final_message.configure(text="Succesfully Submitted")
    else:
        final_message.configure(text="Fill in all the Details!")


img_fb = PhotoImage(file="C:\\Users\\laptop\\Documents\\GG's Doc\\Programming\\Python\\GUI\\Icons\\fb_s.png")
btn_fb = Button(win,bg='Green',relief = SUNKEN,image=img_fb,borderwidth=0,cursor="hand2",command=OpenFb)
btn_fb.configure(width=25,height=25)
fb_window = canvas1.create_window(26, 18, window=btn_fb)
"""canvas1.create_image(30,18,image=img_fb)"""

img_tw = PhotoImage(file="C:\\Users\\laptop\\Documents\\GG's Doc\\Programming\\Python\\GUI\\Icons\\twitter_s.png")
btn_tw = Button(win,bg='Green',relief = SUNKEN,image=img_tw,borderwidth=0,cursor="hand2",command=OpenTw)
btn_tw.configure(width=25,height=25)
tw_window = canvas1.create_window(63, 18, window=btn_tw)
"""canvas1.create_image(60,18,image=img_tw)"""

img_insta = PhotoImage(file="C:\\Users\\laptop\\Documents\\GG's Doc\\Programming\\Python\\GUI\\Icons\\insta_s.png")
btn_ig = Button(win,bg='Green',relief = SUNKEN,image=img_insta,borderwidth=0,cursor="hand2",command=OpenIg)
btn_ig.configure(width=28,height=28)
ig_window = canvas1.create_window(103, 18, window=btn_ig)
"""canvas1.create_image(95,18,image=img_insta)"""

img_yt = PhotoImage(file="C:\\Users\\laptop\\Documents\\GG's Doc\\Programming\\Python\\GUI\\Icons\\yt_s.png")
btn_yt = Button(win,bg='Green',relief = SUNKEN, image=img_yt,borderwidth=0,cursor="hand2",command=OpenYt)
btn_yt.configure(width=28,height=28)
yt_window = canvas1.create_window(142, 18, window=btn_yt)
"""canvas1.create_image(130,18,image=img_yt)"""

img_reg = PhotoImage(file="C:\\Users\\laptop\\Documents\\GG's Doc\\Programming\\Python\\GUI\\Icons\\regis.png")

canvas1.create_image(382,19,image=img_reg)
btn_sign_up = Button(win,text="Sign Up",fg="White",bg='Green',relief=SUNKEN,borderwidth=0,cursor="hand2",command=win_signup_alert)
btn_sign_up.configure(width=6,height=1)
canvas1.create_window(418,19,window=btn_sign_up)
"""canvas1.create_text(415,19,text="Sign Up",fill="white")"""

canvas1.create_line(450,13,450,28,fill="white")

img_login = PhotoImage(file="C:\\Users\\laptop\\Documents\\GG's Doc\\Programming\\Python\\GUI\\Icons\\login.png")
canvas1.create_image(474,19,image=img_login)
btn_sign_in = Button(win,text="Sign In",fg="White",bg='Green',relief=SUNKEN,borderwidth=0,cursor="hand2",command=win_login)
btn_sign_in.configure(width=5,height=1)
canvas1.create_window(503,19,window=btn_sign_in)
"""canvas1.create_text(503,19,text="Sign In",fill="white")"""

canvas1.create_line(535,13,535,28,fill="white")

img_msg = PhotoImage(file="C:\\Users\\laptop\\Documents\\GG's Doc\\Programming\\Python\\GUI\\Icons\\msg.png")
canvas1.create_image(564,19,image=img_msg)
btn_gmail_open = Button(win,text="info@gg's_page.org",fg="White",bg='Green',relief=SUNKEN,borderwidth=0,cursor="hand2",command=OpenGmail)
btn_gmail_open.configure(width=15,height=1)
canvas1.create_window(630,19,window=btn_gmail_open)
"""canvas1.create_text(630,19,text="info@gg's_page.org",fill="white")"""


img_gg = PhotoImage(file="C:\\Users\\laptop\\Documents\\GG's Doc\\Programming\\Python\\GUI\\Icons\\gg.png")
btn_gg = Button(win,bg='#F0F0F0',relief = SUNKEN,image=img_gg,borderwidth=0,cursor="hand2",command=OpenGG)
btn_gg.configure(width=57,height=40)
yt_window = canvas2.create_window(30, 23, window=btn_gg)
"""canvas2.create_image(32,23,image=img_gg,anchor="center")"""

img_home = PhotoImage(file="C:\\Users\\laptop\\Documents\\GG's Doc\\Programming\\Python\\GUI\\Icons\\home.png")
canvas2.create_image(370,25,image=img_home,anchor="center")

canvas2.create_text(400,25,text="Home",fill="Black")
canvas2.create_text(470,25,text="About Us",fill="Black")
canvas2.create_text(560,25,text="Certification",fill="Black")
canvas2.create_text(650,25,text="Contact",fill="Black")





img_edit=PhotoImage(file="C:\\Users\\laptop\\Documents\\GG's Doc\\Programming\\Python\\GUI\\Icons\\edit.png")
canvas_middle.create_image(45,40,image=img_edit)

canvas_middle.create_text(160,44,text="Candidate Sign up",font=("Myriad Pro Light",18))
canvas_middle.create_text(210,75,text="Fill in the form below to get instant access: If you have an ID, please ",fill="Black")


sign_in = Button(win,text="Sign In",fg="Blue",relief=SUNKEN,borderwidth=0,cursor="hand2",command=win_login)
sign_in_window = canvas_middle.create_window(388, 64, anchor=NW, window=sign_in)
"""canvas_middle.create_text(408,70,text="Sign in",fill="Blue")"""






canvas3.create_rectangle(0,0,260,60,fill="#c4bcbc")
                    #Borders
canvas3.create_line(2,0,2,345,fill="Grey")          #left
canvas3.create_line(260,0,260,345,fill="Grey")      #right
canvas3.create_line(0,0,260,0,fill="Grey")          #upper
canvas3.create_line(0,60,260,60,fill="Grey")        #upper middle
canvas3.create_line(0,345,260,345,fill="Grey")      #lower

img_user = PhotoImage(file="C:\\Users\\laptop\\Documents\\GG's Doc\\Programming\\Python\\GUI\\Icons\\user_1.png")
canvas3.create_image(22,30,image=img_user)
canvas3.create_text(142,31,text="Personal Information",fill="Black",font=("BankGothic Md BT",12))                              #BankGothic Md BT 12

canvas3.create_text(38,75,text="Full Name*",fill="Black",font=("Arial Bold",9))
name=Entry(canvas3,width=25,textvar=Fullname).place(x=15,y=90)


day_opt=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
Day.set("Day")
day_menu=OptionMenu(canvas3,Day,*day_opt).place(x=15,y=140)

month_opt=["January","Feburary","March","April","May","June","July","August","September","October","November","December"]
Month.set("Month")
month_menu=OptionMenu(canvas3,Month,*month_opt)
month_menu.config(width=10)
month_menu.place(x=79,y=140)

canvas3.create_text(45,130,text="Date Of Birth",fill="Black",font=("Arial Bold",9))
year_opt=["2000","1999","1998","1997","1996","1995","1994","1993","1992","1991","1990","1989","1988","1987","1986","1985"]
Year.set("Year")
year_menu=OptionMenu(canvas3,Year,*year_opt).place(x=185,y=140)

canvas3.create_text(32,185,text="Gender",fill="Black",font=("Arial Bold",9))
gender_opt=["Male","Female"]
Gender.set("Select Your Gender")
gender_menu=OptionMenu(canvas3,Gender,*gender_opt)
gender_menu.place(x=15,y=195)


canvas3.create_text(30,240,text="Email",fill="Black",font=("Arial Bold",9))
mail_entry=Entry(canvas3,width=35,textvar=Email).place(x=20,y=255)


canvas3.create_text(56,290,text="Create password",fill="Black",font=("Arial Bold",9))
password_entry=Entry(canvas3,show="*",width=35,textvar=Password).place(x=20,y=305)




canvas4.create_rectangle(0,0,260,60,fill="#c4bcbc")
#Borders
canvas4.create_line(2,0,2,345,fill="Grey")          #left
canvas4.create_line(260,0,260,345,fill="Grey")      #right
canvas4.create_line(0,0,260,0,fill="Grey")          #upper
canvas4.create_line(0,60,260,60,fill="Grey")        #upper middle
canvas4.create_line(0,345,260,345,fill="Grey")      #lower

canvas4.create_text(140,31,text="Contact Information",fill="Black",font=("BankGothic Md BT",12))

img_contact = PhotoImage(file="C:\\Users\\laptop\\Documents\\GG's Doc\\Programming\\Python\\GUI\\Icons\\contact_1.png")
canvas4.create_image(24,30,image=img_contact)

canvas4.create_text(60,75,text="Select Your Country",fill="Black",font=("Arial Bold",9))


country_opt=["India","Russia","New Zeland","United State of America","United Kingdom","South Africa","France","Germany","Denmark","Japan","Portugal","Madagascar"]
Country.set("Country")
country_menu=OptionMenu(canvas4,Country,*country_opt)
country_menu.config(width=20)
country_menu.place(x=10,y=85)

canvas4.create_text(50,126,text="Address Line 1",fill="Black",font=("Arial Bold",9))
addr1=Entry(canvas4,width=35,textvar=Address_1)
addr1.place(x=15,y=138)

canvas4.create_text(50,168,text="Address Line 2",fill="Black",font=("Arial Bold",9))
addr2=Entry(canvas4,width=35,textvar=Address_2)
addr2.place(x=15,y=178)

canvas4.create_text(22,212,text="City",fill="Black",font=("Arial Bold",9))
city_entry=Entry(canvas4,width=35,textvar=City)
city_entry.place(x=15,y=225)

canvas4.create_text(38,260,text="ZIP Code",fill="Black",font=("Arial Bold",9))
zip_entry=Entry(canvas4,width=35,textvar=Zip_Code)
zip_entry.place(x=15,y=270)


canvas4.create_text(38,305,text="Phone No.",fill="Black",font=("Arial Bold",9))
phone_entry=Entry(canvas4,width=35,textvar=Phone)
phone_entry.place(x=15,y=315)


submit = Button(win, text = "Submit",anchor = W, fg='black',bg='#F0F0F0',relief=RAISED,command=db_signup)
submit.configure(width = 6,stat=DISABLED)
submit_window = canvas_end.create_window(32, 25, anchor=NW, window=submit)

def submit_state_2():
    if Terms.get()==0:
        submit.configure(state=DISABLED)
    else:
        submit.configure(state=NORMAL)


terms_c_button=Checkbutton(win, text="I agree with Terms and Condition", variable=Terms,command=submit_state_2)
terms_c_button.configure(width = 35)
terms_window = canvas_end.create_window(0, 0, anchor=NW, window=terms_c_button)







url_pizza="https://www.paypal.me/gauravgupta9"
def OpenPizza():
    webbrowser.open_new(url_pizza)
pizza = Button(win,text="Buy Developer a Pizza!",fg="#FF8F00",relief=SUNKEN,borderwidth=0,cursor="hand2",command=OpenPizza)
pizza.configure(font=("Boulder Bold",20))
pizza_window = canvas_end.create_window(215, 70, anchor=NW, window=pizza)

img_pizza=PhotoImage(file="C:\\Users\\laptop\\Documents\\GG's Doc\\Programming\\Python\\GUI\\Icons\\pizza.png")
canvas_end.create_image(475,90,image=img_pizza)

#For invisible button use 2 functions --------> 1. relief=SUNKEN  2. borderwidth=0 and also keep the bg color of button same as canvas color or whatever color it is lying on
win.mainloop()
