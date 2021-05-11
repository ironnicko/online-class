import time
from datetime import datetime
from webbrowser import open as op
import os
from dotenv import load_dotenv

# Constants

load_dotenv()
English = os.getenv('English')


# Clocks
# something

class main:
    @classmethod
    def time(cls, mode='%X'):
        return datetime.now().strftime(mode)

    @classmethod
    def process(cls, hour, minute, week, url):
        condition = int(cls.time('%H')) == int(hour) and int(cls.time("%M")) == int(minute)
        if week == "Eve" or week == cls.time("%a"):
            if condition:
                pass
            elif int(cls.time("%H")) - int(hour) == 0 and 0< int(cls.time("%M")) - int(minute) <= 20 and input("You're late!\nDo you still want to open?[y\n]").lower()=="y":
                pass
            else:
                for _ in iter(lambda: cls.time("%H"), hour):
                    print(cls.time())
                    time.sleep(1)
                for _ in iter(lambda: cls.time("%M"), minute):
                    print(cls.time())
                    time.sleep(1)
            op(url)
            time.sleep(60)

    def call(cls, *a):
        for i in a:
            cls.process(i[:2], i[2:4], i[5:8], i[9:])

if __name__ == '__main__':
    main().call(English)
