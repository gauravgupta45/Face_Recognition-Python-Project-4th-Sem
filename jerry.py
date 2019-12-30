
"""--------------------******GG_01*******--------------------"""
import cv2
import os
import numpy as np
from PIL import Image
import sqlite3
from tkinter import *
from tkinter import messagebox as ms
import datetime
now = datetime.datetime.now()

win=Tk()
win.title("Netbanking Face Recognition Portal")
win.geometry("700x350")


canvas_end = Canvas(win,width=700,height=60)
canvas_end.place(x=0,y=305)

final_message=Label(win,text="",font=("Grange",10))
final_message_window = canvas_end.create_window(34, 10, window=final_message,anchor=NW)


canvas1 = Canvas(win,width=700,height=35,bg="Orange")
canvas1.place(x=0,y=0)



def win_signup_alert():
    ms.showerror('Attention','You are already on Sign Up page')



img_fb = PhotoImage(file="/home/pi/fb_s.png")
btn_fb = Button(win,bg='Orange',relief = SUNKEN,image=img_fb,borderwidth=0,cursor="hand2")
btn_fb.configure(width=25,height=25)
fb_window = canvas1.create_window(26, 18, window=btn_fb)


img_tw = PhotoImage(file="/home/pi/twitter_s.png")
btn_tw = Button(win,bg='Orange',relief = SUNKEN,image=img_tw,borderwidth=0,cursor="hand2")
btn_tw.configure(width=25,height=25)
tw_window = canvas1.create_window(63, 18, window=btn_tw)


img_insta = PhotoImage(file="/home/pi/insta_s.png")
btn_ig = Button(win,bg='Orange',relief = SUNKEN,image=img_insta,borderwidth=0,cursor="hand2")
btn_ig.configure(width=28,height=28)
ig_window = canvas1.create_window(103, 18, window=btn_ig)


img_yt = PhotoImage(file="/home/pi/yt_s.png")
btn_yt = Button(win,bg='Orange',relief = SUNKEN, image=img_yt,borderwidth=0,cursor="hand2")
btn_yt.configure(width=28,height=28)
yt_window = canvas1.create_window(142, 18, window=btn_yt)







def recognize():

    print("\nStarting Face Recognition\n")
    final_message.configure(text="Starting Face Recognition")
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath);

    font = cv2.FONT_HERSHEY_SIMPLEX


    id = 0
    def exit_win():
        cam.release()
        cv2.destroyAllWindows()



    
    #names=['None']
    #names.append(name)
    text_file = open("names_list.txt", "r")
    names_list = text_file.readlines()

    cam = cv2.VideoCapture(0)
    cam.set(3, 640)
    cam.set(4, 480)

    # Define min window size to be recognized as a face
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)

    while True:

        ret, img =cam.read()
        #img = cv2.flip(img, -1) # Flip vertically

        if ret==True:

            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor = 1.2,
                minNeighbors = 5,
                minSize = (int(minW), int(minH)),
               )

            for(x,y,w,h) in faces:

                cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

                id, confidence = recognizer.predict(gray[y:y+h,x:x+w])




                # Check if confidence is less them 100 ==> "0" is perfect match

                user_id=id
                print(user_id)
                if (confidence < 72):
                    id = names_list[id]
                    confidence = "  {0}%".format(round(100 - confidence))
                    print("{0}Detected \nUser Id {1}".format(str(id),user_id))
                    #"""
                    conn = sqlite3.connect('users_sign_in.db')
                    with conn:
                        cursor=conn.cursor()
                    cursor.execute('CREATE TABLE IF NOT EXISTS Sign_In_Table (Date_and_Time TEXT, Fullname TEXT,User_Id INT)')
                    cursor.execute('INSERT INTO Sign_In_Table VALUES(?,?,?)',(str(now),str(id),user_id))
                    conn.commit()
                    exit_win()
                    def on_detect():
                        win4=Toplevel(win)
                        win4.geometry("400x250")
                        win4.title("GG's Login")
                        canvas1_win4 = Canvas(win4,width=450,height=250,bg="Green")
                        canvas1_win4.place(x=0,y=0)
                        success_login_msg=canvas1_win4.create_text(200,125,text="Succesfully Logined as {0}".format(str(id)),fill="#FF8F00",font=("Boulder Bold",15))
                    on_detect()
                    #"""

                else:
                    id = "unknown"
                    confidence = "  {0}%".format(round(100 - confidence))
                    print("\n-----> ",str(id))

                cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
                cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)

            cv2.imshow('camera',img)


        else:
            break

        k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break
    print("\nExiting Programme!\n")
    final_message.configure(text="Exiting Programme!")
    cam.release()
    cv2.destroyAllWindows()








img_reg = PhotoImage(file="/home/pi/regis.png")
canvas1.create_image(300,19,image=img_reg)
btn_sign_up = Button(win,text="Sign Up",fg="White",bg='Orange',relief=SUNKEN,borderwidth=0,cursor="hand2",command=win_signup_alert)
btn_sign_up.configure(width=6,height=1)
canvas1.create_window(350,19,window=btn_sign_up)


canvas1.create_line(400,13,400,28,fill="white")

img_login = PhotoImage(file="/home/pi/login.png")
canvas1.create_image(420,19,image=img_login)
btn_sign_in = Button(win,text="Sign In",fg="White",bg='Orange',relief=SUNKEN,borderwidth=0,cursor="hand2",command=recognize)
btn_sign_in.configure(width=5,height=1)
canvas1.create_window(469,19,window=btn_sign_in)


canvas1.create_line(512,13,512,28,fill="white")

img_msg = PhotoImage(file="/home/pi/msg.png")
canvas1.create_image(530,19,image=img_msg)
btn_gmail_open = Button(win,text="info@gg's_page.org",fg="White",bg='Orange',relief=SUNKEN,borderwidth=0,cursor="hand2")
btn_gmail_open.configure(width=15,height=1)
canvas1.create_window(625,19,window=btn_gmail_open)


canvas_middle = Canvas(win,width=700,height=120)
canvas_middle.place(x=0,y=40)

canvas_middle.create_text(350,30,text="SBI NetBanking",font=("Boulder Bold",28))

img_edit=PhotoImage(file="/home/pi/edit.png")
canvas_middle.create_image(45,70,image=img_edit)

canvas_middle.create_text(145,75,text="User Sign up",font=("Myriad Pro Light",18))
canvas_middle.create_text(245,101,text="Fill in the form below to get instant access: If you have an ID, please ",fill="Black")


sign_in = Button(win,text="Sign In.",fg="Blue",relief=SUNKEN,borderwidth=0,cursor="hand2",command=recognize)
sign_in.configure(width=5)
sign_in_window = canvas_middle.create_window(425, 90, anchor=NW, window=sign_in)


canvas3 = Canvas(win,width=60,height=100)#,bg="Orange")
canvas3.place(x=20,y=195)

Name = StringVar(canvas3)
ID = StringVar(canvas3)




canvas3.create_text(30,15,text="Full Name",fill="Black",font=("Arial Bold",9))
name_entry=Entry(win,width=35,textvar=Name).place(x=90,y=202)


canvas3.create_text(22,57,text="User Id",fill="Black",font=("Arial Bold",9))
id_entry=Entry(win,width=15,textvar=ID).place(x=90,y=240)

canvas4=Canvas(win,width=300,height=170)
canvas4.place(x=380,y=150)
img_face=PhotoImage(file="/home/pi/face_m.png")
canvas4.create_image(150,80,image=img_face)




def register():

    cam = cv2.VideoCapture(0)
    face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    #face_id = input('\nEnter Your User Id:  ')
    face_id = ID.get()
    #name = input('\nEnter Your Name:  ')
    name=Name.get()
    #empty line error:
    """" Following code will remove any empty line that exists in the names_list.txt file """
    with open("names_list.txt", 'r+') as fd:
        lines = fd.readlines()
        fd.seek(0)
        fd.writelines(line for line in lines if line.strip())
        fd.truncate()
    with open("names_list.txt","a") as myfile:
        myfile.write("{}\n".format(name))

    print("\nInitializing face capture. Look the camera and wait ...")
    final_message.configure(text="Initializing face capture. Look the camera and wait ...")
    count = 0

    while(True):

        ret, img = cam.read()

        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        faces = face_detector.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:

            cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
            count += 1

            cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

            cv2.imshow('image', img)

        k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break
        elif count >= 100:
             break


    cam.release()
    cv2.destroyAllWindows()


    print("\nInitiating Training Sequence! This may take a while.")
    final_message.configure(text="Initiating Training Sequence! This may take a while.")

    """--------------------******GG_02*******--------------------"""

    path = 'dataset'
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");


    def getImagesAndLabels(path):
        from PIL import Image
        imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
        faceSamples=[]
        ids = []

        for imagePath in imagePaths:

            PIL_img = Image.open(imagePath).convert('L')
            img_numpy = np.array(PIL_img,'uint8')

            id = int(os.path.split(imagePath)[-1].split(".")[1])
            faces = detector.detectMultiScale(img_numpy)

            for (x,y,w,h) in faces:
                faceSamples.append(img_numpy[y:y+h,x:x+w])
                ids.append(id)

        return faceSamples,ids


    faces,ids = getImagesAndLabels(path)
    recognizer.train(faces, np.array(ids))


    recognizer.write('trainer/trainer.yml')

    print("\n{0} faces trained.".format(len(np.unique(ids))))
    print("\nYou've been registered!")
    final_message.configure(text="You've been registered!")

submit = Button(win, text = "Submit",anchor = W, fg='black',bg='#F0F0F0',relief=RAISED,command=register)
submit.place(x=30,y=300)
submit_window = canvas3.create_window(30, 75, anchor=NW, window=submit)


win.mainloop()









"""--------------------******GG_03*******--------------------"""


"""
print("\n                     Welcome to GG's Face Recognition Portal!\n\n1.)Register Your Face\n2.)Login\n")
choice=int(input("Enter Your Choice: "))

if choice==1:
    register()
    cont=input("Do you want to sign in now(y/n)? ")
    if cont=='y':
        recognize()
    elif cont=='n':
        print("Exiting Programme!")


elif choice==2:
    recognize()
"""
