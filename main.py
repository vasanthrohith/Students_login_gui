import time

import pymysql
import tkinter as tk
from tkinter import *
from tkinter import ttk,messagebox

win = tk.Tk()
win.geometry("500x500")
win.title("Students login")
# ------------------------------DB-------------------------------------
db_con = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "vasanth",
    database = "python_db_03032023"
)
my_db = db_con.cursor()
print("Connection Done")
# ----------------------------------------------------------------------
frame1 = Frame(win,width=10,highlightbackground="red",highlightthickness=3,bg='#ADD8E6')
frame1.pack(padx=10,pady=10,ipady=50,ipadx=50,expand=True,fill='both')


#Frame 2 login success -----------------------------------------------------------
def login_success(fetchname):
    messagebox.showinfo('success',f'{fetchname} login Successful')
    win1 = tk.Tk()
    win1.geometry("500x500")
    win1.title("Students login")
    frame2 = Frame(win1,width=10,highlightbackground="red",highlightthickness=3)
    frame2.pack(padx=10,pady=10,ipady=50,ipadx=50,expand=True,fill='both')
    marks_query= f"select * from marks where username = '{fetchname}'"
    my_db.execute(marks_query)
    output = my_db.fetchall()
    print(output)
    count = 0
    len(output)
    for i in output:
        print("in loop")
        print(i)
        print(len(i))
        for j in range(len(output)):
            print(j)
            print(output[j])
            f2_l1 = Label(frame2, text = output[j],font='14',borderwidth=2,relief='ridge', anchor="w",pady=20,padx=20)
            # i_list = list(i)
            f2_l1.grid(row=count,column=j)
        count = count + 1


def login_fn():
    username = name_entry.get()
    password1 = password.get()
    empty_spaces = []
    empty_spaces.append(username)
    empty_spaces.append(password1)
    print(empty_spaces)

    query_username = "select username from students_03032023"
    my_db.execute(query_username)
    output = my_db.fetchall()
    for i in output:
        print(i[0])
        fetchname = i[0]
        if fetchname == username:
            print("username is correct")
            # try:
            query_password = f"select password from students_03032023 where username = '{username}'"
            my_db.execute(query_password)
            output_password = my_db.fetchall()
            for j in output_password:
                print(j[0])
                if password1 == j[0]:
                    success = Label(frame1, text="Login success!", fg='green',)
                    success.place(x=230, y=270)
                    print("User Logged in success")
                    login_success(fetchname)
                else:
                    fail1 = Label(frame1, text="Login failed!", fg='red')
                    fail1.place(x=230, y=270)
                    print("Incorrect Password")


            # except:
            #     fail = Label(frame1,text = "Login failed!", fg = 'red')
            #     fail.place(x = 230,y = 270)
            #     print("Incorrect Password except")



#Frame 3 signup ---------------------------------------------------------------

def signup_fn():
    def refresh():
        pass_error.destroy()
        rpass_error.destroy()

    def signup_1():
        def add_user_db():
            sup_query = "insert into students_03032023 (username,password)values(%s,%s)"
            values = (name_sup1,password_sup2)
            my_db.execute(sup_query,values)
            output_sup = db_con.commit()
            print("query executed")

        # print("-------")
        # we have to get directly from the entry notfrom the text variable
        name_sup1 = name_s_entry.get()
        password_sup1 = password_s_entry.get()
        password_sup2 = password_s_rentry.get()

        # print((name_sup1),password_sup1,password_sup2)
        if len(name_sup1)>0:
            if len(password_sup1) > 5:
                print(password_sup1)
                pass_error.destroy()
                if password_sup1 == password_sup2:
                    print("Password set gooood")
                    add_user_db()
                    rpass_error.destroy()
                    messagebox.showinfo('Success','User added!')
                else:
                    print("Please re-enter the password correctly")
                    messagebox.showerror('Error', 'Please re-enter the password correctly')
                    rpass_error.place(x=200, y=420)

            else:
                print("Passwords should be greater than 5 characters")
                messagebox.showinfo('Invalid','Passwords should be greater than 5 characters')
                pass_error.place(x=200, y=350)
                # refresh()
        else:
            messagebox.showerror('Error','Invalid Username')
            print("please enter the username correctly")

    win2 = tk.Tk()
    win2.geometry("500x550")
    win2.title("Students SIGNUP")
    frame3 = Frame(win2, width=10, highlightbackground="red", highlightthickness=3,bg='#ADD8E6')
    frame3.pack(padx=10, pady=10, ipady=50, ipadx=50, expand=True, fill='both')
    l1_s = Label(frame3, text="STUDENTS SIGNUP", font='Georgia 24 bold', fg='red',bg='#ADD8E6')
    l1_s.pack()
    l2_s  = Label(frame3, text="Please fill the below details ", font='Georgia 16 bold', fg='green',bg='#ADD8E6')
    l2_s.place(x = 10,y = 150)

    name_s = Label(frame3,text = "Username",font='Georgia 18',bg='#ADD8E6')
    name_s.place(x = 50,y = 250)
    name_s_entry1 = StringVar()
    name_s_entry = Entry(frame3, width=28, textvariable=name_s_entry1)
    name_s_entry.place(x=200, y=260)

    password_s = Label(frame3,text = "Password",font='Georgia 18',bg='#ADD8E6')
    password_s.place(x = 50,y = 320)
    password_s_entry1 = StringVar()
    password_s_entry = Entry(frame3,width=28, textvariable=password_s_entry1)
    password_s_entry.place(x=200, y=330)

    repassword_s = Label(frame3, text="Confirm", font='Georgia 18',bg='#ADD8E6')
    repassword_s.place(x=50, y=390)
    password_s_rentry1 = StringVar()
    password_s_rentry = Entry(frame3,width=28, textvariable=password_s_rentry1)
    password_s_rentry.place(x=200, y=400)

    create_user = Button(frame3,text = "Create user" ,font='Georgia 10 bold',borderwidth=5,command= signup_1)
    create_user.place(x = 190,y = 450)

    rpass_error = Label(frame3, text="Please re-enter the password correctly", fg='red', bg='#ADD8E6')
    pass_error = Label(frame3, text="min password length '5'", fg='red', bg='#ADD8E6')
    refresh_btn = Button(frame3,text = "Refresh",font='Georgia 10 bold',borderwidth=5, command=refresh)
    refresh_btn.place(x = 310, y = 450)



#Frame1 login------------------------------------------------------------

l1 = Label(frame1,text = "STUDENTS LOGIN",font='Georgia 24 bold',fg='red', bg='#ADD8E6')
l1.pack()

name_l = Label(frame1, text = "Username ",font='Georgia 18', bg='#ADD8E6')
name_l.place(x = 50,y = 150)

name = StringVar()
name_entry = Entry(frame1, width=28, textvariable=name)
name_entry.place(x = 190,y = 160)

password_l = Label(frame1, text = "Password ",font='Georgia 18', bg='#ADD8E6')
password_l.place(x = 50,y = 220)

passw = StringVar()
password = Entry(frame1, width=28, textvariable=passw)
password.place(x = 190,y = 230)

# buttons

login = Button(frame1,text = "Login",font='Georgia 10 bold',borderwidth=5,command=login_fn)
login.place(x = 200,y = 300)

new_user = Button(frame1,text = "Signup",font='Georgia 10 bold',borderwidth=5,command=signup_fn)
new_user.place(x = 280,y = 300)




win.mainloop()









































