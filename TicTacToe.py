from tkinter import *
root = Tk()
root.title('Tic Tac Toe')
root.geometry('260x340')
text1 = ""
text2 = ""
text3 = ""
text4 = ""
text5 = ""
text6 = ""
text7 = ""
text8 = ""
text9 = ""
empty = ""
turn_x = True
winner = None
winner_team = None


def all_same(items):
    if items != ["", "", ""]:
        return all(x == items[0] for x in items)
    else:
        return False


def ender():
    global winner, winner_team
    row1 = [text1, text2, text3]
    row2 = [text4, text5, text6]
    row3 = [text7, text8, text9]
    column1 = [text1, text4, text7]
    column2 = [text2, text5, text8]
    column3 = [text3, text6, text9]
    cross1 = [text1, text5, text9]
    cross2 = [text3, text5, text7]
    all_lists = [row1, row2, row3, column1, column2, column3, cross1, cross2]
    winner = None
    all_text = [text1, text2, text3, text4, text5, text6, text7, text8, text9]
    for item in all_lists:
        if all_same(item):
            winner = True
            winner_team = item[0]
    if winner:
        print(f"The winner is the {winner_team}")
        quit()
    else:
        if empty in all_text:
            root.after(1000, ender)
        else:
            print("It is a draw")
            quit()


def sos1():
   global text1, button_1, turn_x
   if turn_x:
       text1 = "X"
       turn_x = False
   else:
       text1 = "O"
       turn_x = True
   button_1 = Button(root, text=text1, font=("Helvetica", 20), width=4, height=4, command=sos1).grid(row=1, column=1)


def sos2():
   global text2, button_2, turn_x
   if turn_x:
       text2 = "X"
       turn_x = False
   else:
       text2 = "O"
       turn_x = True
   button_2 = Button(root, text=text2, font=("Helvetica", 20), width=4, height=4, command=sos2).grid(row=1, column=2)


def sos3():
   global text3, button_3, turn_x
   if turn_x:
       text3 = "X"
       turn_x = False
   else:
       text3 = "O"
       turn_x = True
   button_3 = Button(root, text=text3, font=("Helvetica", 20), width=4, height=4, command=sos3).grid(row=1, column=3)


def sos4():
   global text4, button_4, turn_x
   if turn_x:
       text4 = "X"
       turn_x = False
   else:
       text4 = "O"
       turn_x = True
   button_4 = Button(root, text=text4, font=("Helvetica", 20), width=4, height=4, command=sos4).grid(row=2, column=1)


def sos5():
   global text5, button_5, turn_x
   if turn_x:
       text5 = "X"
       turn_x = False
   else:
       text5 = "O"
       turn_x = True
   button_5 = Button(root, text=text5, font=("Helvetica", 20), width=4, height=4, command=sos5).grid(row=2, column=2)


def sos6():
   global text6, button_6, turn_x
   if turn_x:
       text6 = "X"
       turn_x = False
   else:
       text6 = "O"
       turn_x = True
   button_6 = Button(root, text=text6, font=("Helvetica", 20), width=4, height=4, command=sos6).grid(row=2, column=3)


def sos7():
   global text7, button_7, turn_x
   if turn_x:
       text7 = "X"
       turn_x = False
   else:
       text7 = "O"
       turn_x = True
   button_7 = Button(root, text=text7, font=("Helvetica", 20), width=4, height=4, command=sos7).grid(row=3, column=1)


def sos8():
   global text8, button_8, turn_x
   if turn_x:
       text8 = "X"
       turn_x = False
   else:
       text8 = "O"
       turn_x = True
   button_8 = Button(root, text=text8, font=("Helvetica", 20), width=4, height=4, command=sos8).grid(row=3, column=2)


def sos9():
   global text9, button_9, turn_x
   if turn_x:
       text9 = "X"
       turn_x = False
   else:
       text9 = "O"
       turn_x = True
   button_9 = Button(root, text=text9, font=("Helvetica", 20), width=4, height=4, command=sos9).grid(row=3, column=3)


button_1 = Button(root, text=text1, font=("Helvetica", 20), width=4, height=4, command=sos1).grid(row=1, column=1)
button_2 = Button(root, text=text2, font=("Helvetica", 20), width=4, height=4,  command=sos2).grid(row=1, column=2)
button_3 = Button(root, text=text3, font=("Helvetica", 20), width=4, height=4,  command=sos3).grid(row=1, column=3)
button_4 = Button(root, text=text4, font=("Helvetica", 20), width=4, height=4,  command=sos4).grid(row=2, column=1)
button_5 = Button(root, text=text5, font=("Helvetica", 20), width=4, height=4,  command=sos5).grid(row=2, column=2)
button_6 = Button(root, text=text6, font=("Helvetica", 20), width=4, height=4,  command=sos6).grid(row=2, column=3)
button_7 = Button(root, text=text7, font=("Helvetica", 20), width=4, height=4,  command=sos7).grid(row=3, column=1)
button_8 = Button(root, text=text8, font=("Helvetica", 20), width=4, height=4,  command=sos8).grid(row=3, column=2)
button_9 = Button(root, text=text9, font=("Helvetica", 20), width=4, height=4,  command=sos9).grid(row=3, column=3)
ender()
root.mainloop()
