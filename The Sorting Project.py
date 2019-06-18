import tkinter as tk
import csv
import time
import math
from memory_profiler import profile
import visual_sort as spa


"""
This function (SORTING) is the function called in order to run the entire program
"""
def SORTING():

    back = False 
  
#------------------------------------
    """
    This function reads the list from the yagmai text file located in the same place this program is stored. This is used to quickly 
    read a list without having to input it everytime the program runs.
    """
    def readlist():
        ilistO = []
        temp_lis = []
        with open ("textfile.txt") as tf:
            rtf = csv.reader(tf, delimiter = ",")
            for line in rtf:
                for p in range (len(line)):
                    temp_lis.append(int(line[p]))
                ilistO.extend(temp_lis)
                temp_lis = []
        return ilistO

    """
    This function holds all the infomation the needs to be printed out when a sort completes running
    This is done in order to save space in where the functions are called 
    """
    def info(ilist, end, start, no,itype):
        n = len(ilist)
        print (" ")
        print ("Time used = ", end - start)
        print (" ")
        print ("#O = ", no) #FIND NUMBER OF OPERATIONS AND PUT HERE
        if itype == 1 :
            print ("Best Case: ", (n*math.log(n)))
            print ("Worst Case: ", (n**2))
            print ("Average Case : ", (n*math.log(n)))
        elif itype == 2:
            print ("Best Case: ", (n))
            print ("Worst Case: ", (n**2))
            print ("Average Case: ",(n**2))
        elif itype == 3:
            print ("Best Case: ", (n))
            print ("Worst Case: ", (n**2))
            print ("Average Case: ",(n**2))
        elif itype == 4:
            print ("Best Case: ", (n*10))
            print ("Worst Case: ", (n*10))
            print ("Average Case: ",(n*10))
        elif itype == 5:
            print ("Best Case: ", (n*math.log(n)))
            print ("Worst Case: ", (n**2))
            print ("Average Case: ",(n*math.log(n)))
    #-------------------------------------
    #Visuals

    """
    These functions are the command ran when corresponding button is pressed. inside the function, the list is taken from the text file
    and then put through the sorting functions located in the visual_sort. The function will also then print out the time it took and
    the number of operations, in this case, number of operations will be displayed on the graph.
    """
    def quickV():
        ilistO = readlist()
        ilist = ilistO

        spa.visual_graph(1,ilist)

        print (" ")
        print ("Quick Sort")
        print (ilistO)
        
    def bubbleV():
        ilistO = readlist()
        ilist = ilistO

        spa.visual_graph(2,ilist)

        print (" ")
        print ("Quick Sort")
        print (ilistO)
        
    def insertionV():
        ilistO = readlist()
        ilist = ilistO

        spa.visual_graph(3,ilist)
        
        print (" ")
        print ("Quick Sort")
        print (ilistO)
        
    def radixV():
        ilistO = readlist()
        ilist = ilistO

        spa.visual_graph(4,ilist)
        
        print (" ")
        print ("Quick Sort")
        print (ilistO)
        
    def mergeV():
        ilistO = readlist()
        ilist = ilistO

        spa.visual_graph(5,ilist)
        
        print (" ")
        print ("Quick Sort")
        print (ilistO)

    #-------------------------------------
    #No Visuals

    import sorts_no_visuals as snv
    
    """
    These functions act the same as the ones above, as they are the command functions that run when the corresponding button is pressed.
    These functions will take this list from the text file, and then sort it using the corrisponding sort function.
    They will also print out the time it took for the list to be sorted and the number of operations required. They will also print the 
    best case, worst case, and the average case for the corresponding sort choosen. This is all taken from the info function above
    """
    
    @profile
    def quick():
        ilistO = readlist()
        ilist = ilistO

        start = time.time()
        no=snv.quick_sort(ilist,0,len(ilist)-1,0)
        end = time.time ()

       
        print (" ")
        print ("Quick Sort")
        print (ilist)
        info(ilist, end, start,no,1) 

    @profile
    def bubble():
        ilistO = readlist()
        ilist = ilistO

        start = time.time()
        no=snv.bubblesort(ilist)
        end = time.time ()
        
        print (" ")
        print ("Bubble Sort")
        print(ilist)
        info(ilist, end, start,no,2)
    @profile
    def insertion():
        ilistO = readlist()
        ilist = ilistO

        start = time.time()
        no= snv.insertionsort(ilist)
        end = time.time ()
        
        print (" ")
        print ("Insertion Sort")
        print(ilist)
        info(ilist, end, start,no,3) 
    @profile
    def radix():
        ilistO = readlist()
        ilist = ilistO
        
        start = time.time()
        no=snv.radixsort(ilist)
        end = time.time ()

        print (" ")
        print ("Radix Sort")
        print(ilist)
        info(ilist, end, start,no,4) 
    @profile    
    def merge():
        ilistO = readlist()
        ilist = ilistO

        start = time.time()
        no=snv.mergesort(ilist)
        end = time.time ()

        print (" ")
        print ("Merge Sort")
        print(ilist)
        info(ilist, end, start,no,5) 

    #-------------------------------------

    """
    This function simpliy reads the list from the text file, and prints it for the user to see
    """
    def lists():
        ilistO = readlist()
        print (" ")
        print ("Original List")
        print (ilistO)

        
    """
    This is the command function that runs another function, mainV, being the central hub for visual sort buttons
    """
    def visuals():
        mainV()

    """
    This is the command function the runs another function, mainNV, being the central hub for non visual sort buttons
    """    
    def no_visuals():
        mainNV()
    
    
    """
    This function, opens a windows from tkinter and displays 6 buttons; the back button,the Quick Sort button,the Bubble Sort button,
    the Insertion Sort button, the Radix Sort button, and the Merge Sort button.
    These will run the functions above, and depending on the button choosen, select the corrisponding sort to be used.
    This is only for visuals however, as in these will open a graph and display a animated version of the list being sorted
    """
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

        
    """
    This is the central hub for all the buttons that run the sorting functions that do not have the animated graph. Pressing the button
    will run the corresponding function, that was displayed and sort the list with the corresponding sorting function. Similar to the function
    mentioned above, where as this one does not open a new window to show the list being sorted
    """
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

    """
    This function is the main hub for where this user selects whether they want to see the list be sorted with a visual display or
    without a visual display. The buttons will run either mainV or mainNV which will open new windows with more buttons allowing
    the user to select which specific sort they want to use. the main hub also has a button to print out the current unorganized list
    """
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


        novis = tk.Button(frame,
                       text="No Visuals",
                       command=no_visuals)
        novis.pack(side=tk.LEFT)

        root.minsize(500,500)
        root.maxsize(500,500)
        root.mainloop()
    #----------------------------------------------
    
    """
    This first reads the text file and determines of if it contains a list.
    If it does not, the program print out instructions for the user to how and where to input their list.
    If it does contain a list, it will print the list and run the tkinter main hub window
    """
    ilistO = readlist()
    if ilistO == []:
        print ("please enter list into textfile.txt file")
        print ("with a format like ##,##,##,##")
    else:
        print ("Your list is :", ilistO)
        main()
SORTING()
