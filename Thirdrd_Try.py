import time, webbrowser

# Contants
c: int = 7
local = time.localtime()
first = 'https://zoom.us/j/92944074947?pwd=eGFJYWRwa2pEOWRZbDk1dkg5ZVFrZz09'
second = 'https://zoom.us/j/92944074947?pwd=eGFJYWRwa2pEOWRZbDk1dkg5ZVFrZz09'
third = 'https://zoom.us/j/91802273425?pwd=Kzc1YmRIWW9nM1NzY3ZaRDlnZzdVQT09'
four = 'https://zoom.us/j/97270225115?pwd=Q1IwMkRnclVGODJmU29kdHlCMllpZz09'
five = 'https://zoom.us/j/97270225115?pwd=Q1IwMkRnclVGODJmU29kdHlCMllpZz09'
six = 'https://zoom.us/j/97270225115?pwd=Q1IwMkRnclVGODJmU29kdHlCMllpZz09'


# time
class main:
    @staticmethod
    def second() -> int:
        local = time.localtime()
        time.sleep(1)
        return local[5]

    @staticmethod
    def minute() -> int:
        local = time.localtime()
        return local[4]

    @staticmethod
    def hour() -> int:
        local = time.localtime()
        return local[3]

    @staticmethod
    def clock():
        return f'{main.hour()}:{main.minute()}:{main.second()}'


# open
def one(h, m, url):
    for _ in iter(main.hour, h):
        pass
    for _ in iter(main.minute, m):
        if main.hour()>h and main.minute()>m:
            break
        else:
            pass
    webbrowser.open(url)


# check if it is the time
def checker():
    global c, local
    if local[3] == 8:
        c = 0
    elif local[3] == 9:
        c = 1
    elif local[3] == 11:
        c = 2
    elif local[3] == 12:
        c = 3
    elif local[3] == 15:
        c = 4
    elif local[3] == 16:
        c = 5
    elif local[3] == 17:
        c = 6
    else:
        c = 7

# call time in 24Hr-Format
def open():
    global c
    while c==7:
        checker()
        print(main.clock())
    if c == 0:
        one(8, 43, first)
    checker()
    if c == 1:
        one(9, 43, first)
    checker()
    if c == 2:
        one(11, 13, first)
    checker()
    if c == 3:
        one(12, 13, third)
    checker()
    if c == 4:
        one(15, 13, four)
    checker()
    if c == 5:
        one(16, 13, four)
    checker()
    if c == 6:
        one(17, 13, four)


# end
if __name__ == '__main__':
    open()
