import tkinter as tk
from PIL import ImageTk, Image
import sqlite3
import re

def create_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (username TEXT, password TEXT,score INT, email TEXT, age INT, mob INT, gender TEXT)''')
    conn.commit()
    conn.close()
def getScore():

    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? ", (username, ))
    data = c.fetchone()
    print('current score', data[2])
    conn.close()

    return data[2]

def setScore(point):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('UPDATE users SET score =?  WHERE username=?',(point,username))
    conn.commit()
    conn.close()

username = ''

def signup():
    global username,Mob_num,gender,email,gender_var,Age
    username = signup_username.get()
    password = signup_password.get()
    mail = email.get()
    ag = Age.get()
    Mob = Mob_num.get()
    gen = gender_var.get()
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=?", (username,))
    if c.fetchone():
        signup_status.set('Username already exists')
    else:
        c.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?)", (username, password, 100, mail, ag, Mob, gen))
        conn.commit()
        signup_status.set('Signup successful')
        log = 1
    conn.close()
log = 0 
def login():
    global username,login_button,log,password
    username = login_username.get()
    password = login_password.get()
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    if username !=None and password !=None:
        if c.fetchone():
            login_status.set('Login successful')
            log = 1
            root.destroy()
        else:
            login_status.set('Invalid username or password')
        conn.close()

def state():
    if log == 0:
        return True
    else:
        return False


def delete():
    query = 'DROP TABLE users'
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute(query)
    print('table deleted')

# delete()

def get_data():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    info = c.fetchone() #user details
    return info





root = tk.Tk()
root.geometry('1100x700+50+50')
root.title('Login')
root.configure(bg='#f7c11e')

create_db()

# Signup Frame
# signup_frame = tk.Frame(root,height=400, width=300)
# signup_frame.configure(bg='yellow')
# signup_frame.place(x=100,y=50)

background = Image.open("D:\python projects\Final_game\Final_game\Login_bg (1).jpg")
# resize image
resized = background.resize((1100, 700))
bck_end = ImageTk.PhotoImage(resized)
bglable = tk.Label(root, image=bck_end)
bglable.place(x=0, y=0)

back_lbl=tk.Label(root,width=65,height=30,bg='#fff')
back_lbl.place(x=350,y=50)

signup_label = tk.Label(root,bg='#fff',text='Signup',fg='#ef57f7',font=("Times 20 italic bold"))
signup_label.place(x=520,y=80)

signup_label1 = tk.Label(root,bg='#fff',text='Create new Account',fg='red',font=("Times 15 italic"))
signup_label1.place(x=480,y=60)

border=tk.Label(root,text='________________________',font=('times',10),bg='#fff')
border.place(x=520,y=140)

border2=tk.Label(root,text='________________________',font=('times',10,'bold'),bg='#fff')
border2.place(x=520,y=180)

signup_username_label = tk.Label(root,text='Username',font=('arial',15),bg='#fff')
signup_username_label.place(x=420,y=130)

signup_username = tk.Entry(root,border=0,font=('arial',12))
signup_username.place(x=525,y=135)

signup_password_label = tk.Label(root, text='Password',font=('arial',15),bg='#fff')
signup_password_label.place(x=420,y=170)

signup_password = tk.Entry(root, show='*',border=0,font=('arial',12))
signup_password.place(x=525,y=175)

border3=tk.Label(root,text='________________________',font=('times',10,'bold'),bg='#fff')
border3.place(x=520,y=220)

emaillb = tk.Label(root,text='Email',font=('arial',15),bg='#fff')
emaillb.place(x=420,y=210)

email = tk.Entry(root,border=0,font=('arial',12))
email.place(x=525,y=215)

border4=tk.Label(root,text='________________________',font=('times',10,'bold'),bg='#fff')
border4.place(x=520,y=260)

Agelb = tk.Label(root,text='Age',font=('arial',15),bg='#fff')
Agelb.place(x=420,y=250)

def validate_age(new_value):
    # Only allow digits
    if new_value.isdigit():
        # Limit to 2 digits
        if len(new_value) <= 2:
            return True
    # Disallow other input
    return False

Age = tk.Entry(root, border=0, font=('arial', 12), validate='key')
Age.configure(validatecommand=(root.register(validate_age), '%P'))
Age.place(x=525, y=255)

border5=tk.Label(root,text='________________________',font=('times',10,'bold'),bg='#fff')
border5.place(x=520,y=300)

Mob_numlb = tk.Label(root,text='Mobile.No:.',font=('arial',15),bg='#fff')
Mob_numlb.place(x=420,y=290)

# import re

# Validate the mob number
def validate_mob_num(new_value):
    # Only allow digits
    if new_value.isdigit():
        # Limit to 10 digits
        if len(new_value) <= 10:
            return True
    # Disallow other input
    return False

Mob_num = tk.Entry(root, border=0, font=('arial', 12), validate='key')
Mob_num.configure(validatecommand=(root.register(validate_mob_num), '%P'))
Mob_num.place(x=525, y=295)


# Gender radio buttons
lbl = tk.Label(root, text='Gender', font=('times', 12, 'bold'),bg='#fff')
lbl.place(x=420, y=330)
gender_var = tk.StringVar()
check_male = tk.Radiobutton(root, text='Male', fg='black', bg='#fff',variable=gender_var, value="Male")
check_male.place(x=520, y=330)
check_female = tk.Radiobutton(root, text='Female', fg='black',bg='#fff', variable=gender_var, value="Female")
check_female.place(x=580, y=330)
check_male.select() # set female radio button to be selected by default



signup_button = tk.Button(root, text='Signup', command=signup,width=25,bg='#1675fa',fg='white')
signup_button.place(x=475,y=405)


signup_status = tk.StringVar()
signup_status_label = tk.Label(root, textvariable=signup_status,bg='#fff',fg='#331ef7',font=("Times 15"))
signup_status_label.place(x=465,y=375)


# # Login Page 
def login_pg(): 
    global login_username,login_password,login_status,login_button

    back=tk.Frame(root,width=320,height=450,bg='#fff')
    back.place(x=400,y=50)

    log_border=tk.Label(back,text='________________________',font=('times',10),bg='#fff')
    log_border.place(x=137,y=120)

    log_border2=tk.Label(back,text='________________________',font=('times',10,'bold'),bg='#fff')
    log_border2.place(x=137,y=170)
    #
    login_label = tk.Label(back, text='Login',fg='#ef57f7',font=("Times 20 italic bold"),bg='#fff')
    login_label.place(x=120,y=35)

    login_label1 = tk.Label(back, text='Already have an account ?',fg='red',font=("Times 15 italic"),bg='#fff')
    login_label1.place(x=70,y=10)
    #
    login_username_label = tk.Label(back, text='Username',font=('arial',15),bg='#fff')
    login_username_label.place(x=20,y=120)
    #
    login_username = tk.Entry(back,border=0,font=('arial',12))
    login_username.place(x=137,y=115)
    #
    login_password_label = tk.Label(back, text='Password',font=('arial',15),bg='#fff')
    login_password_label.place(x=20,y=170)
    #
    login_password = tk.Entry(back, show='*',border=0,font=('arial',12))
    login_password.place(x=137,y=165)
    #
    login_button = tk.Button(back, text='Login', command=login,width=25,bg='#1675fa',fg='white')
    login_button.place(x=85,y=225)
    #
    def khtm():
        back.destroy()


    login_status = tk.StringVar()
    login_status_label = tk.Label(back, textvariable=login_status,bg='#fff',fg='#331ef7',font=("Times 15"))
    login_status_label.place(x=60,y=280)
    close=tk.Button(back,text='X',font=('arial',15,'bold'),bg='#fff',bd=0,fg='red',command=khtm)
    close.place(x=290,y=10)

login_lbl=tk.Label(root,text="Already have an account ? -> ",font=('times',10),bg='#fff')
login_lbl.place(x=460,y=450)
log=tk.Button(root,text='login',bg='#fff',bd=0,fg='#1675fa',command=login_pg,cursor='hand2')
log.place(x=620,y=450)



root.mainloop()
