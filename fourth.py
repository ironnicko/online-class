import os
import time
from datetime import datetime as D
from webbrowser import open
try:
    import pynput
except:
    os.system('pip install pynput')
    import pynput

""" Hey! Thanks for opening up the right one. It might seem unreadable[that's cuz im an amatur] but basically paste your first, second, etc... period links onto
    the respective variables as strings. And futhur down at check(), replace them by the periods that change weekly; feel free to add more conditions or remove them.
    'F5' starts the program and 'Esc' closes it."""

# time
LOCAL = D.now()
Condition = True


class Clock:
    # Constants
    global LOCAL, Condition
    C = Condition
    first = 'https://zoom.us/j/92944074947?pwd=eGFJYWRwa2pEOWRZbDk1dkg5ZVFrZz09'  # 8:45-9:45
    second = 'https://zoom.us/j/92944074947?pwd=eGFJYWRwa2pEOWRZbDk1dkg5ZVFrZz09'  # 9:45 - 10:45
    # 11:15 - 12:15
    third = 'https://zoom.us/j/92944074947?pwd=eGFJYWRwa2pEOWRZbDk1dkg5ZVFrZz09'
    four = 'https://zoom.us/j/91802273425?pwd=Kzc1YmRIWW9nM1NzY3ZaRDlnZzdVQT09'  # 12:15 - 1:15
    five = 'https://zoom.us/j/97270225115?pwd=Q1IwMkRnclVGODJmU29kdHlCMllpZz09'  # 3:15 - 4:15
    six = 'https://zoom.us/j/97270225115?pwd=Q1IwMkRnclVGODJmU29kdHlCMllpZz09'  # 4:15 - 5:15
    seven = 'https://zoom.us/j/97270225115?pwd=Q1IwMkRnclVGODJmU29kdHlCMllpZz09'  # 5:15 - 6:15
    l = LOCAL

    # Functions
    def __str__(cls):
        cls.l = D.now().strftime('%X')
        time.sleep(1)
        return cls.l

    @classmethod
    def second(cls):
        cls.l = D.now().strftime('%S')
        time.sleep(1)
        return int(cls.l)

    @classmethod
    def minute(cls):
        cls.l = D.now().strftime('%M')
        return int(cls.l)

    @classmethod
    def hour(cls):
        cls.l = D.now().strftime('%H')

        return int(cls.l)

    @classmethod
    def week(cls):
        cls.l = D.now().strftime('%a')

        return cls.l

    @classmethod
    def check(cls):
        if str(Clock.week()) == 'Wed':
            cls.four = 'https://zoom.us/j/96750768662?pwd=a1JINmUya3VxRzhxdjdmZStTZHJZZz09'
        elif str(Clock.week()) == 'Thu':
            cls.six = 'https://zoom.us/j/93122077432?pwd=YUFIaDVwSDVZYjNnOWNHK2lzV1dyZz09'
        elif str(Clock.week()) == 'Fri':
            cls.seven = 'https://zoom.us/j/93122077432?pwd=YUFIaDVwSDVZYjNnOWNHK2lzV1dyZz09'
        elif str(Clock.week()) == 'Sat':
            cls.third = 'https://zoom.us/j/95951066806?pwd=d2ZEQStTRHlXc2pTM3JuVGlkVWU4QT09'

    @classmethod
    def open(cls):
        if Clock.hour() == 8 and Clock.minute() > 40 and cls.C is True:
            cls.C = False
            open(cls.first)
            for _ in iter(Clock.hour, 9):
                pass
            cls.C = True

        elif Clock.hour() == 9 and Clock.minute() > 40 and cls.C is True:
            cls.C = False
            open(cls.second)
            for _ in iter(Clock.hour, 10):
                pass
            cls.C = True

        elif Clock.hour() == 11 and Clock.minute() > 13 and cls.C is True:
            cls.C = False
            open(cls.third)
            for _ in iter(Clock.hour, 12):
                pass
            cls.C = True

        elif Clock.hour() == 12 and Clock.minute() > 13 and cls.C is True:
            cls.C = False
            open(cls.four)
            for _ in iter(Clock.hour, 13):
                pass
            cls.C = True

        elif Clock.hour() == 15 and Clock.minute() > 13 and cls.C is True:
            cls.C = False
            open(cls.five)
            for _ in iter(Clock.hour, 16):
                pass
            cls.C = True

        elif Clock.hour() == 16 and Clock.minute() > 13 and cls.C is True:
            cls.C = False
            open(cls.six)
            for _ in iter(Clock.hour, 17):
                pass
            cls.C = True

        elif Clock.hour() == 17 and Clock.minute() > 13 and cls.C is True:
            cls.C = False
            open(cls.seven)
            for _ in iter(Clock.hour, 18):
                pass
            cls.C = True


if __name__ == '__main__':
    while True:
        Clock.check()
        Clock.open()
