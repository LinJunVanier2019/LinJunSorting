import tkinter as tk
import csv

#------------------------------------
"""
Reading text file for list
"""
global ilist
ilist = []
temp_lis = []
with open ("yagmai.txt") as tf:
    rtf = csv.reader(tf, delimiter = ",")
    for line in rtf:
        for p in range (len(line)):
            temp_lis.append(int(line[p]))
        ilist.extend(temp_lis)
        temp_lis = []

#-------------------------------------

def bubble():
    print ("bitch")
    hi = len(ilist)-1
    check = True
    while check == True:
        checks = False
        for x in range (0,hi):
            if ilist[x] > ilist[x+1]:
                temp = ilist[x]
                ilist[x] = ilist[x+1]
                ilist[x+1] = temp
                yield ilist
                check = True
                checks = True
            else:
                if checks != True:
                    check = False
        hi -= 1
    print (ilist)
def merge():
    print ("merge")
def insertion():
    print ("insertion")
def radix():
    print ("radix")
def quick():
    print ("quick")
#-------------------------------------

def visuals():
    print("visuals graphs")

def no_visuals():
    main2()

def main2():
    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack()

    button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
    button.pack(side=tk.LEFT)

    slogan = tk.Button(frame,
                   text="Bubble Sort",
                   command=bubble )
    slogan.pack(side=tk.LEFT)
    slogan = tk.Button(frame,
                   text="Quick Sort",
                   command=quick )
    slogan.pack(side=tk.LEFT)
    slogan = tk.Button(frame,
                   text="Insertion Sort",
                   command=insertion )
    slogan.pack(side=tk.LEFT)
    slogan = tk.Button(frame,
                   text="Radix Sort",
                   command=radix )
    slogan.pack(side=tk.LEFT)

    slogan = tk.Button(frame,
                   text="Merge Sort",
                   command=merge )
    slogan.pack(side=tk.LEFT)
def main():
    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack()

    button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
    button.pack(side=tk.LEFT)

    slogan = tk.Button(frame,
                   text="Visuals",
                   command=visuals )
    slogan.pack(side=tk.LEFT)


    Oof = tk.Button(frame,
                   text="No Visuals",
                   command=no_visuals)
    Oof.pack(side=tk.LEFT)


    root.minsize(500,500)
    root.maxsize(500,500)
    root.mainloop()
#----------------------------------------------
if ilist == []:
    print ("please enter list into yagmai.txt text file")
    print ("with a format like ##,##,##,##")
else:
    print ("Your list is :", ilist)
    main()

