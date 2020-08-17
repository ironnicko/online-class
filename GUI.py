import tkinter
import Thirdrd_Try as m


def start():
    entered = textentry.get()
    # output.delete(0.0,tkinter.END)
    if entered == '1':
        op = str(m.main.clock()) + '\n'
        output.insert(tkinter.END, op)


o = m.open

main = tkinter.Tk()
main.geometry('1200x500')
main.title('ONLINE LINK OPENER FOR VELAMMAL INL SCHOOL')

canvas = tkinter.Canvas(main, borderwidth=1, relief='raised')
canvas.grid(row='1', column='0')

label = tkinter.Label(canvas, text='Welcome to Online Class Link-Opener')
label.grid(row='0', column='0')

photo = tkinter.PhotoImage(file="icon.JPG")
main.iconphoto(False, photo)

button = tkinter.Button(canvas, text='Start', command=o)
button.grid(row='1', column='4')

cancelb = tkinter.Button(canvas, text="cancel", command=main.destroy)
cancelb.grid(row='4', column='4', sticky='w')

button1 = tkinter.Button(canvas, text='OKAY', command=start)
button1.grid(row='1', column='1', sticky='w')

output = tkinter.Text(canvas, width=75, height=20, bg='white', wrap=tkinter.WORD, font='none 12 bold')
output.grid()

textentry = tkinter.Entry(canvas, bg='white')
textentry.grid(row='2', column='0')

label1 = tkinter.Label(canvas, text='Press \'1\' to see the time:')
label1.grid(row='1', column='0')

main.mainloop()
