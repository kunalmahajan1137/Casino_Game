import time
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import random
import pygame
from idlelib.tooltip import Hovertip
from login import*
import sys

if state():
    sys.exit()

get_data()
# creating screen
root = tk.Tk()
root.title("Image Guessing Game")
root.geometry('1000x750')
root.resizable(False, False)
# root.iconbitmap(r'online-game.ico')  # default icon change of tkinter window

#flag
x = 1

def reset():
    global image1,res,play_status,img_list,c
    c=1
    img_list.clear()

    play_status=0
    ch1.configure(image=image1)
    ch1.image = image1

    ch2.configure(image=image1)
    ch2.image = image1

    ch3.configure(image=image1)
    ch3.image = image1

    ch4.configure(image=image1)
    ch4.image = image1

    result.configure(image=res)
    result.image = res

    if speak_status == 1:
        pygame.mixer.music.load("D:/python projects/Final_game/Final_game/click.waw.wav")
        pygame.mixer.music.play(loops=0)

# setting Panel
def setting_window():
    global root, theme, x

    f = Frame(root, height=400, width=300, borderwidth=2, relief=GROOVE,bg='#f2ec3d')
    f.place(x=695, y=10)

    tk.Button(f, text='X', font='Arial,12,bold', fg='red',bg='#f2ec3d', border=0, command=lambda: f.destroy(), height=1, width=3,
              cursor='hand2').place(x=250, y=5)
    theme = tk.IntVar(value=x)

    but1 = tk.Radiobutton(f, text="Default", variable=theme, command=backImage, value=1, fg='blue', cursor='hand2',bg='#f2ec3d')
    but1.place(x=5, y=70)

    # theme picture 1
    background1 = Image.open('D:\python projects\Final_game\Final_game\casinobg.jpg')
    resized1 = background1.resize((150, 100))
    bck_end1 = ImageTk.PhotoImage(resized1)

    background2 = Image.open('D:\python projects\Final_game\Final_game\casinoImg.jpg')
    resized2 = background2.resize((155, 105))
    bck_end2 = ImageTk.PhotoImage(resized2)

    lable1 = Label(f, bg='blue', image=bck_end1, height=100, width=150)
    lable1.place(x=100, y=40)

    set_title = Label(f, text='Setting', fg='red', font=('Times', 20, 'bold'),bg='#f2ec3d')
    set_title.place(x=130, y=0)

    but2 = tk.Radiobutton(f, text="Classic", variable=theme, command=backImage, value=2, fg='blue', cursor='hand2',bg='#f2ec3d')
    but2.place(x=5, y=200)
    lable2 = Label(f, bg='red',image=bck_end2,height=100, width=150)
    lable2.place(x=100, y=150)
    lable1.configure(bck_end1)
    lable2.configure(bck_end2)

    if speak_status == 1:
        pygame.mixer.music.load("click.waw.wav")
        pygame.mixer.music.play(loops=0)
# _______________________________________________________________________________________________
def backImage():
    global background, bck_end, x
    if theme.get() == 1:
        background = Image.open('D:\python projects\Final_game\Final_game\casinobg.jpg')
        # resize image
        resized = background.resize((1000, 800))
        bck_end = ImageTk.PhotoImage(resized)
        lable.configure(image=bck_end)
        x = 1
    else:
        background = Image.open('D:\python projects\Final_game\Final_game\casinoImg.jpg')
        # resize image
        resized = background.resize((1000, 800))
        bck_end = ImageTk.PhotoImage(resized)
        lable.configure(image=bck_end)
        x = 2
    if speak_status == 1:
        pygame.mixer.music.load("D:\python projects\Final_game\Final_game\click.waw.wav")
        pygame.mixer.music.play(loops=0)

background = Image.open('D:/python projects/Final_game/Final_game/casinobg.jpg')
# resize image
resized = background.resize((1000, 800))
bck_end = ImageTk.PhotoImage(resized)
lable = Label(root, image=bck_end)
lable.place(x=0, y=0)

########################################################################################################################
images = ["D:/python projects/Final_game/Final_game/res1.png",
          "D:/python projects/Final_game/Final_game/res2.png",
          "D:/python projects/Final_game/Final_game/res3.png",
          "D:/python projects/Final_game/Final_game/res4.png",
          "D:/python projects/Final_game/Final_game/res5.png",
          "D:/python projects/Final_game/Final_game/res6.png",
          "D:/python projects/Final_game/Final_game/res7.png",
          "D:/python projects/Final_game/Final_game/res8.png",
          "D:/python projects/Final_game/Final_game/res9.png",
          "D:/python projects/Final_game/Final_game/res10.png",
          "D:/python projects/Final_game/Final_game/res11.png",
          "D:/python projects/Final_game/Final_game/res12.png",
          ]

res = PhotoImage(file='D:/python projects/Final_game/Final_game/que3.png')

result = Label(root, image=res, height=175, width=300, bg='light green')
result.image = res
result.place(x=600, y=110)
res_tit = Label(root, text='Result', bg='red', fg='yellow', font=('arial', 15, 'bold'))
res_tit.place(x=715, y=90)

# res=Label(root,height=3,width=21,bg='yellow',border=2)
# res.place(x=410,y=157)

image1 = PhotoImage(file='D:/python projects/Final_game/Final_game/que1.png')
choice1 = Label(root, image=image1, height=167, width=320, bg='pink')
# choice1.image = image1
choice1.place(x=70, y=120)
choice_tit = Label(root, text='You have selected', bg='red', fg='yellow', font=('arial', 15, 'bold'))
choice_tit.place(x=129, y=100)
ch1 = Label(choice1,image=image1,height=75,width=140,bg='red')
ch1.image = image1
ch1.grid(row=0,column=0)
ch2 = Label(choice1,image=image1,height=75,width=140,bg='blue')
ch2.image = image1
ch2.grid(row=0,column=1)
ch3 = Label(choice1,image=image1,height=75,width=140,bg='yellow')
ch3.image = image1
ch3.grid(row=1,column=0)
ch4 = Label(choice1,image=image1,height=75,width=140,bg='green')
ch4.image = image1
ch4.grid(row=1,column=1)
########################################################################################################################
image2, my_img = None, None
r, ra = None, None
########################################################################################################################
score = getScore()
score_lable = Label(root, height=3, width=15, bg='white',fg='red', text=f'\tScore \n\t {score}', font=('Algerian',13))
score_lable.place(x=100, y=23)
name= Label(root,text='-Created By-\nKunal Mahajan',fg='yellow',font=('Algerian',15),bg='#4e247d')
name.place(x=410,y=650)
coin = Image.open("D:/python projects/Final_game/Final_game/coin.png")
reduce = coin.resize((50, 50))
bck = ImageTk.PhotoImage(reduce)
lable1 = Label(root, image=bck, bg='white')
lable1.place(x=99, y=28)
########################################################################################################################
pygame.mixer.init()  # initializing pygame

status = 0
def roll():
    global image2, score, Play, speak_status, play_status,img_list,status
    rn_img = random.choice(images)
    for i in img_list:
        if i == rn_img:
            status = 1
            break

    if play_status == 1:


        if speak_status == 1:
            pygame.mixer.music.load("D:/python projects/Final_game/Final_game/click.waw.wav")
            pygame.mixer.music.play(loops=0)

        image2 = ImageTk.PhotoImage(Image.open(rn_img))
        result.configure(image=image2, bg='pink')

        if status == 1:
            # Wining Logics
            # playsound('clap.mpeg')
            res = Label(root, height=3, width=24, bg='white', border=2)
            res.place(x=380, y=50)
            res.configure(text='w i n', font=('Algerian', 10), fg='red')
            score = score + 10
            setScore(score)
            score_lable.configure(text=f'\tScore \n\t{score}', fg='green')
            if speak_status == 1:
                pygame.mixer.music.load("D:/python projects/Final_game/Final_game/clap.wav")
                pygame.mixer.music.play(loops=0)

        else:
            # lose
            res = Label(root, height=3, width=24, bg='white', border=2)
            res.place(x=380, y=50)
            Play = Button(state='disabled')
            res.configure(text='l o s e', font=('Algerian', 10,), fg='red')
            score = score - len(img_list)
            setScore(score)
            score_lable.configure(text=f'\tScore \n\t{score}', fg='red')
            if speak_status == 1:
                pygame.mixer.music.load("D:/python projects/Final_game/Final_game/gameover.wav")
                pygame.mixer.music.play(loops=0)
        status = 0
    play_status = 0



########################################################################################################################

# PLAY BUTTON
play_status = 0
# play = PhotoImage(file='res1.png')
tk.Button(root, text='PLAY', font='Arial,11,bold', width=16, height=2, bg='yellow', fg='red',
          command=roll, cursor='hand2').place(x=388, y=200)

#Setting Button
setting_img = PhotoImage(file="D:/python projects/Final_game/Final_game/settings_1.png")
setting = tk.Button(root,image=setting_img, text='setting', font='Arial,12,bold', width=50, height=50, bg='yellow',
                    command=setting_window, cursor='hand2')
setting.place(x=850, y=20)
myTip=Hovertip(setting,'setting')

#Close Button
close=PhotoImage(file='D:/python projects/Final_game/Final_game/cross.png')
close_btn=tk.Button(root, font='Arial,12,bold', bg='yellow', fg='red', command=quit, height=50, width=50,
          cursor='hand2',image=close)
close_btn.place(x=930, y=20)
close_tip=Hovertip(close_btn,'close')
#restart Button
reset_btn=Button(root,text="RESTART",bg='red',fg='white', width=16, height=2,font='Arial,12,bold',command=reset,cursor='hand2')
reset_btn.place(x=388,y=280)

#user details
def user():
    global root, theme, x,score
    info=get_data()
    print(info)

    f = Frame(root, height=400, width=300, borderwidth=2, relief=GROOVE,bg='white')
    f.place(x=695, y=10)
    tk.Button(f, text='X', font='Arial,12,bold', fg='red',bg='white', border=0, command=lambda: f.destroy(), height=1, width=3,
              cursor='hand2').place(x=250, y=5)
    theme = tk.IntVar(value=x)

    heading=Label(f,text='User Profile',fg='red',bg='white',font=('times',20,'italic'))
    heading.place(x=70,y=10)

    detail1=Label(f,text='UserName = '+info[0],bg='white',font=('times',13,))
    detail1.place(x=10,y=50)

    detail2=Label(f,text='',bg='white',font=('times',13,))
    detail2.place(x=10,y=70)
    detail2.configure(text=f'Score\t = {info[2]}')
    
    detail3=Label(f,text='Email ID   = '+info[3],bg='white',font=('times',13,))
    detail3.place(x=10,y=90)
    
    detail4=Label(f,text='',bg='white',font=('times',13,))
    detail4.place(x=10,y=110)
    detail4.configure(text=f'Age\t = {info[4]}')

    detail5=Label(f,text='',bg='white',font=('times',13,))
    detail5.place(x=10,y=130)
    detail5.configure(text=f'Mobile No = {info[5]}')

    detail6=Label(f,text='Gender   = '+info[6],bg='white',font=('times',13,))
    detail6.place(x=10,y=150)
###########
info1=get_data()
if info1[6]=='Male':
    user_img = PhotoImage(file="D:/python projects/Final_game/Final_game/man.png")
else:
    user_img = PhotoImage(file='D:/python projects/Final_game/Final_game/girl.png')
user=Button(root,image=user_img,text='User',width=50,height=50,bg='yellow',command=user,cursor='hand2')
user.place(x=770, y=20)
######################################################################################################################

#Image selection code

c = 1
img_list = [] #selected images will store in this list
def my_select(i):
    global my_img, sel_list, Play, play_status,c,img_list
    global r
    r = i
    play_status = 1
    if speak_status == 1:
        pygame.mixer.music.load("D:/python projects/Final_game/Final_game/click.waw.wav")
        pygame.mixer.music.play(loops=0)

    # my_img = PhotoImage(images[i])
    my_img = Image.open(images[i])
    compress = my_img.resize((80,75))
    photo3 = ImageTk.PhotoImage(compress)
    if c == 1:
        ch1.configure(image=photo3)
        ch1.image=photo3
        img_list.append(images[i])
    elif c == 2:
        ch2.configure(image=photo3)
        ch2.image=photo3
        img_list.append(images[i])
    elif c == 3:
        ch3.configure(image=photo3)
        ch3.image=photo3
        img_list.append(images[i])
    elif c == 4:
        ch4.configure(image=photo3)
        ch4.image=photo3
        img_list.append(images[i])

    c += 1

##############################################################################################################
#12 Buttons with images
# BUTTON1-----------------------------------------------------------------------------------------------------
photo = PhotoImage(file='D:/python projects/Final_game/Final_game/res1.png')
b1=Button(
    root, image=photo, bg="pink", border=0, command=lambda: my_select(0), height=120, width=120, cursor='hand2',bd=3
)
b1.place(x=70, y=350)
b1_tip=Hovertip(b1,'Rabbit')


#############################################################################################################
# BUTTON 2---------------------------------------------------------------------------------------------------
photo2 = PhotoImage(file="D:/python projects/Final_game/Final_game/res2.png")
b2=Button(
    root, image=photo2,cursor='hand2',bg="pink", border=0, command=lambda: my_select(1), height=120, width=120, text='rabbit',bd=3
)
b2.place(x=210, y=350)
b2_tip=Hovertip(b2,'Butterfly')

##############################################################################################################
# button3-------------------------------------------------------------------------------------------------------------

photo3 = PhotoImage(file="D:/python projects/Final_game/Final_game/res3.png")
b3=Button(
    root, image=photo3,cursor='hand2',bg="pink", border=0, command=lambda: my_select(2), height=120, width=120,bd=3
)
b3.place(x=350, y=350)
b3_tip=Hovertip(b3,'Ball')
##############################################################################################################
# Button4-------------------------------------------------------------------------------------------------------------

photo4 = PhotoImage(file="D:/python projects/Final_game/Final_game/res4.png")
b4=Button(
    root, image=photo4,cursor='hand2',bg="pink", border=0, command=lambda: my_select(3), height=120, width=120,bd=3
)
b4.place(x=490, y=350)
b4_tip=Hovertip(b4,'Sun')
##############################################################################################################
# BUTTON5--------------------------------------------------------------------------------------------------------------
photo5 = PhotoImage(file="D:/python projects/Final_game/Final_game/res5.png")
b5=Button(
    root, image=photo5,cursor='hand2',bg="pink", border=0, command=lambda: my_select(4), height=120, width=120,bd=3
)
b5.place(x=630, y=350)
b5_tip=Hovertip(b5,'Top')

# #############################################################################################################
# BUTTON6--------------------------------------------------------------------------------------------------------------
photo6 = PhotoImage(file="D:/python projects/Final_game/Final_game/res6.png")
b6=Button(
    root, image=photo6,cursor='hand2',bg="pink", border=0, command=lambda: my_select(5), height=120, width=120,bd=3
)
b6.place(x=770, y=350)
b6_tip=Hovertip(b6,'rose')

###############################################################################################################
#BUTTON7--------------------------------------------------------------------------------------------------------------
photo7 = PhotoImage(file="D:/python projects/Final_game/Final_game/res7.png")
b7=Button(
    root, image=photo7,cursor='hand2',bg="pink", border=0, command=lambda: my_select(6), height=120, width=120,bd=3
)
b7.place(x=70, y=500)
b7_tip=Hovertip(b7,'Kite')

###############################################################################################################
# BUTTON8--------------------------------------------------------------------------------------------------------------
photo8 = PhotoImage(file="D:/python projects/Final_game/Final_game/res8.png")
b8=Button(
    root, image=photo8,cursor='hand2', bg="pink", border=0, command=lambda: my_select(7), height=120, width=120,bd=3
)
b8.place(x=210, y=500)
b8_tip=Hovertip(b8,'Pigion')

###############################################################################################################
# BUTTON9--------------------------------------------------------------------------------------------------------------
photo9 = PhotoImage(file="D:/python projects/Final_game/Final_game/res9.png")
b9=Button(
    root, image=photo9,cursor='hand2', bg="pink", border=0, command=lambda: my_select(8), height=120, width=120,bd=3
)
b9.place(x=350, y=500)
b9_tip=Hovertip(b9,'Umbrella')
###############################################################################################################
# BUTTON10--------------------------------------------------------------------------------------------------------------
photo10 = PhotoImage(file="D:/python projects/Final_game/Final_game/res10.png")
b10=Button(
    root, image=photo10,cursor='hand2', bg="pink", border=0, command=lambda: my_select(9), height=120, width=120,bd=3
)
b10.place(x=490, y=500)
b10_tip=Hovertip(b10,'Cow')
################################################################################################################
# BUTTON11--------------------------------------------------------------------------------------------------------------
photo11 = PhotoImage(file="D:/python projects/Final_game/Final_game/res11.png")
b11=Button(
    root, image=photo11,cursor='hand2', bg="pink", border=0, command=lambda: my_select(10), height=120, width=120,bd=3,
)
b11.place(x=630, y=500)
b11_tip=Hovertip(b11,'Bucket')

###############################################################################################################
# BUTTON12--------------------------------------------------------------------------------------------------------------
photo12 = PhotoImage(file="D:/python projects/Final_game/Final_game/res12.png")
b12=Button(
    root, image=photo12,cursor='hand2', bg="pink", border=0, command=lambda: my_select(11), height=120, width=120,bd=3
)
b12.place(x=770, y=500)
b12_tip=Hovertip(b12,'Diya')
###############################################################################################################
#Mute Function code
def off_speak():
    global speak_status,silent_tip

    if speak_status == 1:
        speak_status = 0
        silent_button.configure(image=sound_png)

    else:
        speak_status = 1
        silent_button.configure(image=silence_png)


#mute Button code
speak_status = 1
silence_png = PhotoImage(file='D:/python projects/Final_game/Final_game/sound.png')
sound_png = PhotoImage(file='D:/python projects/Final_game/Final_game/silence.png')
silent_button = Button(root, image=silence_png, relief=GROOVE, borderwidth=2, command=off_speak, border=0, height=55,
                       width=65,cursor='hand2')
silent_button.place(x=10, y=30)
silent_tip=Hovertip(silent_button,'Mute')
root.mainloop()
