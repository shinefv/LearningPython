#!/usr/bin/python
def hantei():
    a=0
    r=0
    while a<1:
        a=1
        b=raw_input("Yes:1 No:0\nYou:")
        if b=='1':
            r=1
            break
        elif b=='0':
            r=0
            break
        a=0
    return r

def firstans():
    print "Would you like to use this program?"
    if hantei():
        hikaru()
    else:
        print "See you!"

def hikaru():
    print"Hello, What your name?"
    str=raw_input("Name:")
    print"Hello,",str
    print"Would you like to save this data?"
    if hantei():
        str=raw_input("what is file name?")
        fo=open(str,"wb")
        print"Name of the file:",fo.name
        print"Closed or not:",fo.closed
        print"Opening mode:",fo.mode
        print"Softspace flag",fo.softspace
    else:
        print "see you"
    
    print"Would you like to write this file?"
    if hantei():
        fo=open(str,"a")
        str=raw_input("where do you want to save this file?\n")
        fo.write(str)
        fo.close()
    else:
        print"bye"

firstans()
