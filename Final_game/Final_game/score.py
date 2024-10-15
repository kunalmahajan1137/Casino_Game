import time
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import random
import pygame
from idlelib.tooltip import Hovertip

# creating screen
root = tk.Tk()
root.title("Image Guessing Game")
root.geometry('1000x750')
root.resizable(False, False)
root.iconbitmap(r'online-game.ico')  # default icon change of tkinter window

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
    background1 = Image.open('casinobg.jpg')
    resized1 = background1.resize((150, 100), Image.ANTIALIAS)
    bck_end1 = ImageTk.PhotoImage(resized1)

    background2 = Image.open('casinoImg.jpg')
    resized2 = background2.resize((155, 105), Image.ANTIALIAS)
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
# _______________________________________________________________________________________________
def backImage():
    global background, bck_end, x
    if theme.get() == 1:
        background = Image.open('casinobg.jpg')
        # resize image
        resized = background.resize((1000, 800), Image.ANTIALIAS)
        bck_end = ImageTk.PhotoImage(resized)
        lable.configure(image=bck_end)
        x = 1
    else:
        background = Image.open('casinoImg.jpg')
        # resize image
        resized = background.resize((1000, 800), Image.ANTIALIAS)
        bck_end = ImageTk.PhotoImage(resized)
        lable.configure(image=bck_end)
        x = 2


background = Image.open('casinobg.jpg')
# resize image
resized = background.resize((1000, 800), Image.ANTIALIAS)
bck_end = ImageTk.PhotoImage(resized)
lable = Label(root, image=bck_end)
lable.place(x=0, y=0)

########################################################################################################################
images = ['res1.png', 'res2.png', 'res3.png', 'res4.png', 'res5.png', 'res6.png', 'res7.png', 'res8.png', 'res9.png',
          'res10.png', 'res11.png', 'res12.png']

res = PhotoImage(file='que3.png')

result = Label(root, image=res, height=175, width=300, bg='light green')
result.image = res
result.place(x=600, y=110)
res_tit = Label(root, text='Result', bg='red', fg='yellow', font=('arial', 15, 'bold'))
res_tit.place(x=715, y=90)

# res=Label(root,height=3,width=21,bg='yellow',border=2)
# res.place(x=410,y=157)

image1 = PhotoImage(file='que1.png')
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
#score
with open('score.txt', 'w') as f:
    f.write('100')


def check_answer(choice):
    global score

    if choice == answer:
        score += 1
        score_label.config(text="Score: {}".format(score))

        # update the score in the file
        with open('score.txt', 'w') as f:
            f.write(str(score))

        # show a message box
        messagebox.showinfo("Correct", "Congratulations! Your answer is correct.")

        # ask a new question
        ask_question()
    else:
        # show a message box
        messagebox.showerror("Incorrect", "Sorry, your answer is incorrect. Please try again.")

with open('score.txt', 'r') as f:
    score = int(f.read())

score_label = Label(root, text="Score: {}".format(score),height=3, width=15, bg='white',fg='red',font=('Algerian',13))
score_label.place(x=130, y=23)

########################################################################################################################
#score = 100
# score_lable = Label(root, height=3, width=15, bg='white',fg='red', text=f'\tScore \n\t {score}', font=('Algerian',13))
# score_lable.place(x=100, y=23)
name= Label(root,text='-Created By-\nghanshyam',fg='yellow',font=('Algerian',15),bg='#4e247d')
name.place(x=410,y=650)
coin = Image.open("D:\\shyam\\basketball\\coin.png")
reduce = coin.resize((50, 50), Image.ANTIALIAS)
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
            pygame.mixer.music.load("click.waw.wav")
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
            score_lable.configure(text="Score: {}".format(score), fg='green')
            if speak_status == 1:
                pygame.mixer.music.load("clap.wav")
                pygame.mixer.music.play(loops=0)

        else:
            # lose
            res = Label(root, height=3, width=24, bg='white', border=2)
            res.place(x=380, y=50)
            Play = Button(state='disabled')
            res.configure(text='l o s e', font=('Algerian', 10,), fg='red')
            score = score - len(img_list)
            score_lable.configure(text="Score: {}".format(score), fg='red')
            if speak_status == 1:
                pygame.mixer.music.load("gameover.wav")
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
setting_img = PhotoImage(file='001-settings.png')
setting = tk.Button(root,image=setting_img, text='setting', font='Arial,12,bold', width=50, height=50, bg='yellow',
                    command=setting_window, cursor='hand2')
setting.place(x=850, y=20)
myTip=Hovertip(setting,'setting')

#Close Button
close=PhotoImage(file='cross.png')
close_btn=tk.Button(root, font='Arial,12,bold', bg='yellow', fg='red', command=quit, height=50, width=50,
          cursor='hand2',image=close)
close_btn.place(x=930, y=20)
close_tip=Hovertip(close_btn,'close')
#restart Button
reset_btn=Button(root,text="RESTART",bg='red',fg='white', width=16, height=2,font='Arial,12,bold',command=reset,cursor='hand2')
reset_btn.place(x=388,y=280)

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
        pygame.mixer.music.load("click.waw.wav")
        pygame.mixer.music.play(loops=0)

    # my_img = PhotoImage(images[i])
    my_img = Image.open(images[i])
    compress = my_img.resize((80,75),Image.ANTIALIAS)
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
photo = PhotoImage(file='res1.png')
Button(
    root, image=photo, bg="pink", border=0, command=lambda: my_select(0), height=120, width=120, cursor='hand2',bd=3
).place(x=70, y=350)

#############################################################################################################
# BUTTON 2---------------------------------------------------------------------------------------------------
photo2 = PhotoImage(file="res2.png")
Button(
    root, image=photo2, bg="pink", border=0, command=lambda: my_select(1), height=120, width=120, text='rabbit',bd=3
).place(x=210, y=350)

##############################################################################################################
# button3-------------------------------------------------------------------------------------------------------------

photo3 = PhotoImage(file="res3.png")
Button(
    root, image=photo3, bg="pink", border=0, command=lambda: my_select(2), height=120, width=120,bd=3
).place(x=350, y=350)

##############################################################################################################
# Button4-------------------------------------------------------------------------------------------------------------

photo4 = PhotoImage(file="res4.png")
Button(
    root, image=photo4, bg="pink", border=0, command=lambda: my_select(3), height=120, width=120,bd=3
).place(x=490, y=350)

##############################################################################################################
# BUTTON5--------------------------------------------------------------------------------------------------------------
photo5 = PhotoImage(file="res5.png")
Button(
    root, image=photo5, bg="pink", border=0, command=lambda: my_select(4), height=120, width=120,bd=3
).place(x=630, y=350)

# #############################################################################################################
# BUTTON6--------------------------------------------------------------------------------------------------------------
photo6 = PhotoImage(file="res6.png")
Button(
    root, image=photo6, bg="pink", border=0, command=lambda: my_select(5), height=120, width=120,bd=3
).place(x=770, y=350)

###############################################################################################################
#BUTTON7--------------------------------------------------------------------------------------------------------------
photo7 = PhotoImage(file="res7.png")
Button(
    root, image=photo7, bg="pink", border=0, command=lambda: my_select(6), height=120, width=120,bd=3
).place(x=70, y=500)

###############################################################################################################
# BUTTON8--------------------------------------------------------------------------------------------------------------
photo8 = PhotoImage(file="res8.png")
Button(
    root, image=photo8, bg="pink", border=0, command=lambda: my_select(7), height=120, width=120,bd=3
).place(x=210, y=500)

###############################################################################################################
# BUTTON9--------------------------------------------------------------------------------------------------------------
photo9 = PhotoImage(file="res9.png")
Button(
    root, image=photo9, bg="pink", border=0, command=lambda: my_select(8), height=120, width=120,bd=3
).place(x=350, y=500)

###############################################################################################################
# BUTTON10--------------------------------------------------------------------------------------------------------------
photo10 = PhotoImage(file="res10.png")
Button(
    root, image=photo10, bg="pink", border=0, command=lambda: my_select(9), height=120, width=120,bd=3
).place(x=490, y=500)

################################################################################################################
# BUTTON11--------------------------------------------------------------------------------------------------------------
photo11 = PhotoImage(file="res11.png")
Button(
    root, image=photo11, bg="pink", border=0, command=lambda: my_select(10), height=120, width=120,bd=3,
).place(x=630, y=500)
###############################################################################################################
# BUTTON12--------------------------------------------------------------------------------------------------------------
photo12 = PhotoImage(file="res12.png")
Button(
    root, image=photo12, bg="pink", border=0, command=lambda: my_select(11), height=120, width=120,bd=3
).place(x=770, y=500)
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
silence_png = PhotoImage(file='sound.png')
sound_png = PhotoImage(file='silence.png')
silent_button = Button(root, image=silence_png, relief=GROOVE, borderwidth=2, command=off_speak, border=0, height=55,
                       width=65,cursor='hand2')
silent_button.place(x=10, y=30)
silent_tip=Hovertip(silent_button,'Mute')
root.mainloop()
