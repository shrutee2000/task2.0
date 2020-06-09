from tkinter import *
import os
import sqlite3

'''           ------------         GUI 2       -------------      '''


def loggedin():
    global screen2
    global name
    global branch
    global regdid
    global name_entry
    global branch_entry
    global regdid_entry

    screen2 = Toplevel(screen)
    screen2.title("checking")
    screen2.geometry("500x500")
    name = StringVar()
    branch = StringVar()
    regdid = StringVar()

    Label(screen2, text="Name :").pack()
    #    userid = StringVar()
    name_entry = Entry(screen2, textvariable=name)
    name_entry.pack()

    Label(screen2, text="Branch :").pack()
    #    password = StringVar()
    branch_entry = Entry(screen2, textvariable=branch)
    branch_entry.pack()
    #    Label(screen2, text = "Successfully Logged in.", fg = "green",command = open_window()).pack()
    #    Button(screen2, text = "continue", command = open_window()).pack()

    Label(screen2, text="Regd Id :").pack()
    #    password = StringVar()
    regdid_entry = Entry(screen2, textvariable=regdid)
    regdid_entry.pack()

    Button(screen2, text="continue", command=do).pack()


#    Label(screen2,text='',textvariable = status).pack()

'''             -----------              SUBJECTS SUBMISSION          -----------                          '''


def open_window():
    tip = Toplevel()
    tip.title("SUBJECTS")
    tip.geometry("500x500")

    Label(tip, text="MARKS SUBMISSION", font=("arial", 14, "bold")).pack()

    Label(tip, text="Input for respective marks :", font=("arial", 11, "bold")).pack()

    Button(tip, text="FCT", width=10, bg="yellow", command=open_window_fct).pack()

    Button(tip, text="IDS", width=10, bg="yellow", command=open_window_ids).pack()

    Button(tip, text="EMFT", width=10, bg="yellow", command=open_window_emft).pack()

    Button(tip, text="SUBMIT", fg="black", bg="light blue", width=10, command=open_window3).pack()


def open_window_fct():
    global fct_marks
    global fct_entry
    fct_marks = StringVar()

    fct = Toplevel()
    fct.title("FCT")
    fct.geometry("500x500")
    Label(fct, text="Enter the marks obtained :").pack()

    fct_entry = Entry(fct, textvariable=fct_marks)
    fct_entry.pack()

    Button(fct, text="Done", command=fct_submission).pack()


def fct_submission():
    fct1 = fct_marks.get()
    name1 = name.get()

    conn = sqlite3.connect("Information.db")
    with conn:
        cur = conn.cursor()
    #    addColumn = "ALTER TABLE USERDETAILS ADD COLUMN FCT varchar(32)"
    #    cur.execute(addColumn)
    cur.execute('''UPDATE USERDETAILS SET FCT == "%s" WHERE Name == "%s"''' % (fct1, name1))
    conn.commit()
    cur.close()
    conn.close()


def open_window_ids():
    global ids_marks
    global ids_entry
    ids_marks = StringVar()

    ids = Toplevel()
    ids.title("IDS")
    ids.geometry("500x500")
    Label(ids, text="Enter the marks obtained :").pack()

    ids_entry = Entry(ids, textvariable=ids_marks)
    ids_entry.pack()

    Button(ids, text="Done", command=ids_submission).pack()


def ids_submission():
    ids1 = ids_marks.get()
    name1 = name.get()

    conn = sqlite3.connect("Information.db")
    with conn:
        cur = conn.cursor()
    #    addColumn2 = "ALTER TABLE USERDETAILS ADD COLUMN IDS varchar(32)"
    #    cur.execute(addColumn2)
    cur.execute('''UPDATE USERDETAILS SET IDS == "%s" WHERE Name == "%s"''' % (ids1, name1))
    conn.commit()
    cur.close()
    conn.close()


def open_window_emft():
    global emft_marks
    global emft_entry
    emft_marks = StringVar()

    emft = Toplevel()
    emft.title("EMFT")
    emft.geometry("500x500")
    Label(emft, text="Enter the marks obtained :").pack()

    emft_entry = Entry(emft, textvariable=emft_marks)
    emft_entry.pack()

    Button(emft, text="Done", command=emft_submission).pack()


def emft_submission():
    emft1 = emft_marks.get()
    name1 = name.get()

    conn = sqlite3.connect("Information.db")
    with conn:
        cur = conn.cursor()
    #    addColumn3 = "ALTER TABLE USERDETAILS ADD COLUMN EMFT varchar(32)"
    #    cur.execute(addColumn3)
    cur.execute('''UPDATE DETAILS SET EMFT == "%s" WHERE Name == "%s"''' % (emft1, name1))
    conn.commit()
    cur.close()
    conn.close()


def do():
    open_window()
    put()


def invalid():
    screen3 = Toplevel(screen)
    screen3.title("checking")
    screen3.geometry("200x200")
    Label(screen3, text="Invalid UserID or Password.", fg="red").pack()


'''         ------------        GUI 3        ---------------        '''


def open_window3():
    tom = Toplevel()
    tom.title("GUI 3")
    tom.geometry("500x500")

    Label(tom, text="RESULTS", font=("arial", 14, "bold")).pack()

    Label(tom, text="Input options :", font=("arial", 11, "bold")).pack()

    Button(tom, text="CGPA", width=10, bg="yellow").pack()

    Button(tom, text="GRADE", width=10, bg="yellow").pack()

    Button(tom, text="NEW INPUT", width=10, bg="yellow").pack()

    Button(tom, text="CLOSE", width=10, bg="yellow").pack()


#    Button(tip, text = "SUBMIT",fg = "black",bg = "light blue",width =10).pack()


'''        ------------        DATABASE CONNECTION         ----------       '''

conn = sqlite3.connect('Information.db')
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS USERDETAILS(Name TEXT, Branch TEXT, RegdID REAL)")

# sql = "DELETE FROM USERDETAILS WHERE Name = 'shrutee'"

# cur.execute(sql)

conn.commit()


# print(cur.rowcount, "record(s) deleted")


# conn.commit()


def put():
    name1 = name.get()
    branch1 = branch.get()
    regdid1 = regdid.get()
    conn = sqlite3.connect('Information.db')
    cur = conn.cursor()

    cur.execute("INSERT INTO USERDETAILS (Name,Branch, RegdID) VALUES (?,?,? )", (name1, branch1, regdid1))
    conn.commit()


'''          ----------          SIGN UP PART        ----------        '''


def login_verify():
    user1 = userid.get()
    password1 = password.get()
    username_entry.delete(0, END)
    password_entry.delete(0, END)

    list_of_files = os.listdir()

    if user1 in list_of_files:

        file1 = open(user1, "r")
        verify = file1.read().splitlines()

        if password1 in verify:

            loggedin()

        else:
            invalid()
    else:
        invalid()


def signin():
    global screen
    global userid
    global password
    global username_entry
    global password_entry
    screen = Tk()
    screen.geometry("500x500")
    screen.title("Student Management system")
    Label(screen, text="Username :").pack()
    userid = StringVar()
    username_entry = Entry(textvariable=userid)
    username_entry.pack()
    Label(screen, text="Password :").pack()
    password = StringVar()
    password_entry = Entry(textvariable=password, show="*")
    password_entry.pack()
    Button(screen, text="Submit", command=login_verify).pack()
    screen.mainloop()


signin()
cur.close()
conn.close()


'''        ---------------          CGPA CALCULATION     -------------        '''


def cgpa_func():
    global cgpa
    fct1 = fct_marks.get()

    ids1 = ids_marks.get()

    emft1 = emft_marks.get()

    avg = 0
    tot = 0
    avg_per = 0
    cgpa = 0

    tot = fct1 + ids1 + emft1
    avg = tot / 300
    avg_per = avg * 100

    cgpa = (avg_per) / 9.5
    print("The cgpa is:", cgpa)


def display_cgpa():
    tuf = Toplevel()
    tuf.title("Displaying CGPA")
    tuf.geometry("300x300")
    Label(tuf, text="THE CGPA OBTAINED IS :", font=("arial", 9, "bold"), bg="yellow", fg="red").pack()
    Label(tuf, text=float(cgpa), bg="cyan").pack()


def do1():
    cgpa_func()
    display_cgpa()


'''      --------------      GRADE CALCULATION     ---------------'''


#       CGPA          GRADE
#     9 - 10.0          O
#     8 - 8.9           E
#     7 - 7.9           A
#     6 - 6.9           B
#     5 - 5.9           C
#     below 5           D


def grade_func():
    global grade

    if (cgpa < 5.0):
        grade = "D"
    elif (cgpa < 6.0):
        grade = "C"
    elif (cgpa < 7.0):
        grade = "B"
    elif (cgpa < 8.0):
        grade = "A"
    elif (cgpa < 9.0):
        grade = "E"
    elif (cgpa < 10.1):
        grade = "O"

    print("The grade obtained is:", grade)


def display_grade():
    tub = Toplevel()
    tub.title("Displaying Grade")
    tub.geometry("300x300")

    Label(tub, text="THE GRADE OBTAINED IS :", font=("arial", 9, "bold"), bg="yellow", fg="red").pack()
    Label(tub, text=str(grade), width=10, bg="cyan").pack()


def do2():
    grade_func()
    display_grade()


'''         ------------        GUI 3        ---------------        '''


def open_window3():
    tom = Toplevel()
    tom.title("GUI 3")
    tom.geometry("500x500")
    tom.configure(bg="aquamarine")

    Label(tom, text="RESULTS", font=("arial", 14, "bold")).pack()

    Label(tom, text="Input options :", font=("arial", 11, "bold")).pack()

    Button(tom, text="CGPA", width=10, bg="yellow", command=do1).pack()

    Button(tom, text="GRADE", width=10, bg="yellow", command=do2).pack()

    Button(tom, text="NEW INPUT", width=10, bg="yellow", command=new_input).pack()

    Button(tom, text="CLOSE", width=10, bg="yellow", command=close).pack()


'''         -----------------       FINAL CLOSE       -----------------'''


def close():
    screen.destroy()


'''          ------------       NEW INPUT        ----------------'''


def new_input():
    loggedin()  