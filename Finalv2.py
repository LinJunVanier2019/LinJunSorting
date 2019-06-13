import tkinter as tk
import csv

back = False 

#------------------------------------
"""
Reading text file for list
"""
global ilist2
ilist2 = []
temp_lis = []
with open ("yagmai.txt") as tf:
    rtf = csv.reader(tf, delimiter = ",")
    for line in rtf:
        for p in range (len(line)):
            temp_lis.append(int(line[p]))
        ilist2.extend(temp_lis)
        temp_lis = []

#-------------------------------------
#No Visuals

import sorts_no_visuals as snv

def quick():
    ilist = ilist2
    snv.quick_sort(ilist,0,len(ilist)-1)
    print(ilist)

def bubble():
    ilist = ilist2
    snv.bubblesort(ilist)
    print(ilist)
    
def insertion():
    ilist = ilist2
    snv.insertionsort(ilist)
    print(ilist)

def radix():
    ilist = ilist2
    
def merge():
    ilist = ilist2

#-------------------------------------

def lists():
    print (ilist2)

def visuals():
    mainV()

def no_visuals():
    mainNV()

def ram():
    print ("ram")
    #insert open ram code here
    
def mainV():
    print ("visuals")

def mainNV():
    if back == False:
        root = tk.Tk()
        frame = tk.Frame(root)
        frame.pack()

        button = tk.Button(frame, 
                       text="Back", 
                       fg="red",
                       command=root.destroy)
        button.pack(side=tk.LEFT)
        slogan = tk.Button(frame,
                       text="Quick Sort",
                       command=quick )
    
        slogan.pack(side=tk.LEFT)
        slogan = tk.Button(frame,
                       text="Bubble Sort",
                       command=bubble )
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
                   command=root.destroy)
    button.pack(side=tk.LEFT)

    slogan = tk.Button(frame,
                   text="Print List",
                   command=lists )
    slogan.pack(side=tk.LEFT)

    slogan = tk.Button(frame,
                   text="Visuals",
                   command=visuals )
    slogan.pack(side=tk.LEFT)


    Oof = tk.Button(frame,
                   text="No Visuals",
                   command=no_visuals)
    Oof.pack(side=tk.LEFT)
    
    Oof = tk.Button(frame,
                   text="Open Ram",
                   command=ram)
    Oof.pack(side=tk.LEFT)


    root.minsize(500,500)
    root.maxsize(500,500)
    root.mainloop()
#----------------------------------------------
if ilist2 == []:
    print ("please enter list into yagmai.txt text file")
    print ("with a format like ##,##,##,##")
else:
    print ("Your list is :", ilist2)
main()
