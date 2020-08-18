import tkinter
import Thirdrd_Try as m


# start button command
def start():
    entered = textentry.get()
    # output.delete(0.0,tkinter.END)
    if entered == '1':
        op = str(m.main.clock()) + '\n'
        output.insert(tkinter.END, op)


# initialize it to a variable
o = m.open

#main body
main = tkinter.Tk()
main.geometry('1200x500')
main.title('ONLINE LINK OPENER FOR VELAMMAL INL SCHOOL')

#Canvas
canvas = tkinter.Canvas(main, borderwidth=1, relief='raised')
canvas.grid(row='1', column='0')

#Label
label = tkinter.Label(canvas, text='Welcome to Online Class Link-Opener')
label.grid(row='0', column='0')


#icon
photo = tkinter.PhotoImage(file="icon.JPG")
main.iconphoto(False, photo)


#start button
button = tkinter.Button(canvas, text='Start', command=o)
button.grid(row='1', column='4')


#Cancel Button
cancelb = tkinter.Button(canvas, text="cancel", command=main.destroy)
cancelb.grid(row='4', column='4', sticky='w')


#Okay button
button1 = tkinter.Button(canvas, text='OKAY', command=start)
button1.grid(row='1', column='1', sticky='w')


#output for the timer
output = tkinter.Text(canvas, width=75, height=20, bg='white', wrap=tkinter.WORD, font='none 12 bold')
output.grid()


#text-entry block
textentry = tkinter.Entry(canvas, bg='white')
textentry.grid(row='2', column='0')


#label to the block
label1 = tkinter.Label(canvas, text='Press \'1\' to see the time:')
label1.grid(row='1', column='0')


#end
main.mainloop()
