import os
import urllib

def read():
    text = open(os.path.expanduser("~/Desktop/Curses/Curse.txt"))
    contents_of_file = text.read()
    text.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    #website no longer in service
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
    output = connection.read()
    print(output)
    connection.close()

read()
