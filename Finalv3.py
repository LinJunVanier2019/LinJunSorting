import tkinter as tk
import csv

back = False 

#------------------------------------
"""
Reading text file for list
"""
def readlist():
    ilistO = []
    temp_lis = []
    with open ("yagmai.txt") as tf:
        rtf = csv.reader(tf, delimiter = ",")
        for line in rtf:
            for p in range (len(line)):
                temp_lis.append(int(line[p]))
            ilistO.extend(temp_lis)
            temp_lis = []
    return ilistO
#-------------------------------------
#Visuals

def quickV():
    ilistO = readlist()
    ilist = ilistO

    print (" ")
    print ("Quick Sort")
    print (ilistO)
    
def bubbleV():
    ilistO = readlist()
    ilist = ilistO

    print (" ")
    print ("Quick Sort")
    print (ilistO)
    
def insertionV():
    ilistO = readlist()
    ilist = ilistO
    
    print (" ")
    print ("Quick Sort")
    print (ilistO)
    
def radixV():
    ilistO = readlist()
    ilist = ilistO
    
    print (" ")
    print ("Quick Sort")
    print (ilistO)
    
def mergeV():
    ilistO = readlist()
    ilist = ilistO
    
    print (" ")
    print ("Quick Sort")
    print (ilistO)

#-------------------------------------
#No Visuals

import sorts_no_visuals as snv

def quick():
    ilistO = readlist()
    ilist = ilistO
    
    snv.quick_sort(ilist,0,len(ilist)-1)
    
    print (" ")
    print ("Quick Sort")
    print (ilistO)


def bubble():
    ilistO = readlist()
    ilist = ilistO
    
    snv.bubblesort(ilist)
    
    print (" ")
    print ("Bubble Sort")
    print(ilist)
    
def insertion():
    ilistO = readlist()
    ilist = ilistO
    
    snv.insertionsort(ilist)
    
    print (" ")
    print ("Insertion Sort")
    print(ilist)

def radix():
    ilistO = readlist()
    ilist = ilistO

    snv.radixsort(ilist)

    print (" ")
    print ("Radix Sort")
    print(ilist)
    
def merge():
    ilistO = readlist()
    ilist = ilistO

    snv.mergesort(ilist)

    print (" ")
    print ("Merge Sort")
    print(ilist)

#-------------------------------------

def lists():
    ilistO = readlist()
    print (" ")
    print ("Original List")
    print (ilistO)

def visuals():
    mainV()

def no_visuals():
    mainNV()

def ram():
    print ("ram")
    #insert open ram code here
    
def mainV():

    
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
                    command=quickV )
    
    slogan.pack(side=tk.LEFT)
    slogan = tk.Button(frame,
                    text="Bubble Sort",
                    command=bubbleV )
    slogan.pack(side=tk.LEFT)
    slogan = tk.Button(frame,
                   text="Insertion Sort",
                    command=insertionV )
    slogan.pack(side=tk.LEFT)
    slogan = tk.Button(frame,
                    text="Radix Sort",
                    command=radixV )
    slogan.pack(side=tk.LEFT)
    slogan = tk.Button(frame,
                    text="Merge Sort",
                    command=mergeV )
    slogan.pack(side=tk.LEFT)

    root.minsize(400,400)
    root.maxsize(400,400)

def mainNV():

        
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

    root.minsize(400,400)
    root.maxsize(400,400)
    
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
ilistO = readlist()
if ilistO == []:
    print ("please enter list into yagmai.txt text file")
    print ("with a format like ##,##,##,##")
else:
    print ("Your list is :", ilistO)
main()
