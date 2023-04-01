from tkinter import *
import random


class Set:
    def Settings():
        global count_n

        title = "Hafıza Oyunu"
        geometry = "625x575+550+150"
        count_n = 10

        Set.Window(title, geometry)



    def TargetNumber():
        global target_n

        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        target_n = random.choice(numbers)




    def CountDown():
        global TargetNumber
        global target_n
        global count_n

        Set.TargetNumber()

        try:
            time = p.after(1000, Set.CountDown)
            count_n -= 1

            Count['text'] = "Geri sayım: "+str(count_n)

            if(count_n == 0):
                p.after_cancel(time)
                Count.destroy()

                Button1['stat'] = NORMAL
                Button2['stat'] = NORMAL
                Button3['stat'] = NORMAL
                Button4['stat'] = NORMAL
                Button5['stat'] = NORMAL
                Button6['stat'] = NORMAL
                Button7['stat'] = NORMAL
                Button8['stat'] = NORMAL
                Button9['stat'] = NORMAL

                TargetNumber = Label(p,
                              text="Hedef sayı: " + str(target_n),
                              font=("arial", 15, "bold"))
                TargetNumber.place(x=225, y=50)

                Button1['text'] = ''
                Button2['text'] = ''
                Button3['text'] = ''
                Button4['text'] = ''
                Button5['text'] = ''
                Button6['text'] = ''
                Button7['text'] = ''
                Button8['text'] = ''
                Button9['text'] = ''

            else:
                pass

        except Exception:
            pass



    def RandomNumbers():
        global random_numbers
        global numbers

        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        random_numbers = []

        for i in range(len(numbers)):
            random_n = random.choice(numbers)
            numbers.remove(random_n)

            random_numbers.append(random_n)



    def Window(title, geometry):
        global p
        global Count
        global Button1, Button2, Button3, Button4, Button5, Button6, Button7, Button8, Button9

        p = Tk()

        p.title(title)
        p.geometry(geometry)
        p.resizable(FALSE, FALSE)

        Count = Label(p,
                      text="Geri sayım: "+str(count_n),
                      font=("arial",15,"bold"))
        Count.place(x = 225, y = 50)

        Set.CountDown()
        Set.RandomNumbers()

        global button1n, button2n, button3n, button4n, button5n, button6n, button7n, button8n, button9n

        button1n, button2n, button3n = random_numbers[0], random_numbers[1], random_numbers[2]
        button4n, button5n, button6n = random_numbers[3], random_numbers[4], random_numbers[5]
        button7n, button8n, button9n = random_numbers[6], random_numbers[7], random_numbers[8]


        Button1 = Button(p,
                         text=str(button1n),
                         font=("arial",17,"bold"),
                         bd=7, width=3, stat=DISABLED,
                         command= lambda : ButtonAct.Button1Action(str(button1n), target_n))
        Button1.place(x = 115, y = 150)

        Button2 = Button(p,
                         text=str(button2n),
                         font=("arial",17,"bold"),
                         bd=7, width=3, stat=DISABLED,
                         command= lambda : ButtonAct.Button2Action(str(button2n), target_n))
        Button2.place(x = 215, y = 150)

        Button3 = Button(p,
                         text=str(button3n),
                         font=("arial",17,"bold"),
                         bd=7, width=3, stat=DISABLED,
                         command= lambda : ButtonAct.Button3Action(str(button3n), target_n))
        Button3.place(x = 315, y = 150)

        Button4 = Button(p,
                         text=str(button4n),
                         font=("arial",17,"bold"),
                         bd=7, width=3, stat=DISABLED,
                         command= lambda : ButtonAct.Button4Action(str(button4n), target_n))
        Button4.place(x = 415, y = 150)

        Button5 = Button(p,
                         text=str(button5n),
                         font=("arial",17,"bold"),
                         bd=7, width=3, stat=DISABLED,
                         command= lambda : ButtonAct.Button5Action(str(button5n), target_n))
        Button5.place(x = 115, y = 250)

        Button6 = Button(p,
                         text=str(button6n),
                         font=("arial",17,"bold"),
                         bd=7, width=3, stat=DISABLED,
                         command= lambda : ButtonAct.Button6Action(str(button6n), target_n))
        Button6.place(x = 215, y = 250)

        Button7 = Button(p,
                         text=str(button7n),
                         font=("arial",17,"bold"),
                         bd=7, width=3, stat=DISABLED,
                         command= lambda : ButtonAct.Button7Action(str(button7n), target_n))
        Button7.place(x = 315, y = 250)

        Button8 = Button(p,
                         text=str(button8n),
                         font=("arial",17,"bold"),
                         bd=7, width=3, stat=DISABLED,
                         command= lambda : ButtonAct.Button8Action(str(button8n), target_n))
        Button8.place(x = 415, y = 250)


        Button9 = Button(p,
                         text=str(button9n),
                         font=("arial",17,"bold"),
                         bd=7, width=3, stat=DISABLED,
                         command= lambda : ButtonAct.Button9Action(str(button9n), target_n))
        Button9.place(x = 265, y = 350)



        p.mainloop()


def Correct():
    Button1.destroy()
    Button2.destroy()
    Button3.destroy()
    Button4.destroy()
    Button5.destroy()
    Button6.destroy()
    Button7.destroy()
    Button8.destroy()
    Button9.destroy()
    TargetNumber.destroy()

    CORRECT_TEXT = Label(p,
                         text="TEBRİKLER!!!", fg='red',
                         font=("arial", 30, "bold"))
    CORRECT_TEXT.place(x=175, y=175)


class ButtonAct:
    def Button1Action(n, target_n):
        if(int(n) == int(target_n)):
            Correct()

        else:
            Button1['bg'] = 'red'


    def Button2Action(n, target_n):
        if(int(n) == int(target_n)):
            Correct()

        else:
            Button2['bg'] = 'red'


    def Button3Action(n, target_n):
        if(int(n) == int(target_n)):
            Correct()

        else:
            Button3['bg'] = 'red'


    def Button4Action(n, target_n):
        if(int(n) == int(target_n)):
            Correct()

        else:
            Button4['bg'] = 'red'


    def Button5Action(n, target_n):
        if(int(n) == int(target_n)):
            Correct()

        else:
            Button5['bg'] = 'red'


    def Button6Action(n, target_n):
        if(int(n) == int(target_n)):
            Correct()

        else:
            Button6['bg'] = 'red'


    def Button7Action(n, target_n):
        if(int(n) == int(target_n)):
            Correct()

        else:
            Button7['bg'] = 'red'


    def Button8Action(n, target_n):
        if(int(n) == int(target_n)):
            Correct()

        else:
            Button8['bg'] = 'red'


    def Button9Action(n, target_n):
        if(int(n) == int(target_n)):
            Correct()

        else:
            Button9['bg'] = 'red'




if(__name__ == '__main__'):
    Set.Settings()