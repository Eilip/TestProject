from tkinter import *
import random
q=[ "where is the capital of nepal?",
    "which one is the land lock country?",
    "who invented c language? ",
    " what are machine language?",
    " what is OS?",
    "what  is key board?",
    "what is linux?",
    "who founded windows?",
    "what is windos?",
    "who founded apple?"]
ac=[["kathmandu","birathnagar","lumbini","dharan" ],
        ["china","japan","india","nepal"],
        ["sir issac newton","mark zuckerberg","dennis ritchie","tom cruise" ],
        ["alphabet","1 to 10","python code","1 and 0"],
        ["hardware","software","game","music player"],
        ["hardware","software","game","music player"],
        ["game","opensource o.s","microsoft o.s","ios"],
        ["steave jobs","mark zuckerberg","dennis ritchie","bill gates"],
        ["game","opensource o.s","microsoft o.s","ios"],
        ["steave jobs","mark zuckerberg","dennis ritchie","bill gates"]]
index=[]
def gen():
    global index
    while(len(index) < 5):
        x=random.randint(0,9)
        if x in index:
            continue
        else:
            index.append(x)
    print(index)
def selected():
    global rv
    x = rv.get()
    print(x)



def quiz():
    q1=Label(
        root,
        text=q[0],
        width=900,
        justify="center",
        wraplength =800
    )
    q1.pack()
    global rv
    rv = IntVar()
    rv.set(-1)
    r1=Radiobutton(
        root,text=ac[0][0],value=0,variable= rv, command= selected,
    )
    r1.pack()
    r2 = Radiobutton(
        root, text=ac[0][1], value=1, variable=rv,command= selected,
    )
    r2.pack()
    r3 = Radiobutton(
        root, text=ac[0][2], value=2, variable=rv,command= selected,
    )
    r3.pack()
    r4 = Radiobutton(
        root, text=ac[0][3], value=3, variable=rv,command= selected,
    )
    r4.pack()




def start_p():

    labletext.destroy()
    labletext.destroy()
    rules.destroy()
    rules1.destroy()
    start.destroy()
    quiz()
root = Tk()

root.title("My Quiz")
root.geometry("1000x600")
root.config(background="light green")
root.resizable(0,0)

img1= PhotoImage(file="Softwarica-logo.png")
lableimage =    Label(
    root,
    image = img1,
    background="light green"
)
lableimage.pack(pady=(40,0))
labletext= Label(
    root,
    text = "lets start",
    font=("Comic sans MS",24,"bold"),
    background="light green"

)
labletext.pack()
img2= PhotoImage(file ="start.png")
start=Button(
    root,
    image = img2,
    relief = FLAT,
    border = 0,
    command= start_p,

)
start.pack()
rules1=Label(
    root,
    text = "click start after reading this rules",
    background = "red",
    font =("Bernand MT", 16, "italic")

)
rules1.pack(pady=(10,100))
rules = Label(
    text=   '''              rules\n
              1) you can only answer once                    \n
              2)give the answer as number not word           \n
              3) every correct answer will give you 2 points \n
              4) every wrong answer will decuct your ponts.\n\n\n''',
    width=100,
    background = "yellow",
    foreground = "red",
)
rules.pack()
root.mainloop()