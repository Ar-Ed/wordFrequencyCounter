import tkinter as tk
from tkinter  import filedialog
import os
from pathlib import Path, PureWindowsPath
def wordFrequencytext():
    text = entry1.get(1.0, tk.END)
    numberOfWords = int(entry2.get())
    rem = numberOfWords
    f = open("text.txt", "w")
    f.write(text)
    f.close()
    f = open("text.txt")
    a = f.read().strip()
    lines = a.split("\n")
    f.close()
    dic = dict()
    for line in lines:
        line = line.split(" ")
        for word in line:
                word = word.upper().capitalize()
                dic[word] = dic.get(word, 0) + 1
    NumberOfWords = 0
    for k in sorted(dic, key=dic.get, reverse=True):
       if NumberOfWords < numberOfWords:
            Outlabel = tk.Label(results, text=str(NumberOfWords+1)+ "- " + str(k) + " : " + str(dic[k]), bg="Light Sea Green")
            Outlabel.pack(pady=5)
            NumberOfWords+=1

text = None
def wordFrequencytxtfile():
    global text
    f = open(os.path.normpath(text.name) ,"r")
    numberOfWords = int(entry2.get())
    a = f.read().strip()
    lines = a.split("\n")
    f.close()
    dic = dict()
    for line in lines:
        line = line.split(" ")
        for word in line:
                word = word.upper().capitalize()
                dic[word] = dic.get(word, 0) + 1
    NumberOfWords = 0
    for k in sorted(dic, key=dic.get, reverse=True):
        if NumberOfWords < numberOfWords:
            Outlabel = tk.Label(results, text=str(NumberOfWords+1)+ "- " + str(k) + " : " + str(dic[k]), bg="Light Sea Green")
            Outlabel.pack(pady=5)
            NumberOfWords+=1

def txtfileopener():
    window.filename = filedialog.askopenfile(initialdir="/C:", title="Select a File", filetypes=[("txt files", "*.txt")])
    global text
    text = window.filename

def FrameRefresher():
    global results
    results = tk.LabelFrame(window, text="Word Frequency\n Calculator", bd=5, height=340, width=150, bg="Light Sea Green", relief="sunken")
    results.pack_propagate(0)
    results.grid(row=0, column=7)

def clear_entry(event):
    if index == True:
        entry2.delete(0,tk.END)
def clear_entry1(event):
    if index1 == True:
        entry1.delete(1.0, tk.END)

window = tk.Tk()
window.geometry("650x500")
window.configure(bg="chartreuse3")
window.iconbitmap("C:/Users/Toshiba/Desktop/gui/karakter finder/__pycache__/w.ico")

index1=True
entry1 = tk.Text(window, width=50, height=20, bg="Light Sea Green", borderwidth=5)
entry1.insert(0.0, "Please Enter Your Text")
entry1.grid(row=0,column=0, padx=30, pady=20, columnspan=3)
entry1.bind("<Button-1>", clear_entry1)

index = True
entry2 = tk.Entry(window, bg="Light Sea Green", borderwidth=5, width=30)
entry2.insert(0,"Please Enter Number of Words")
entry2.grid(row=3,column=2, pady=10)
entry2.bind("<Button-1>", clear_entry)

sendfile = tk.Button(window, text="Send Text",fg="ghostwhite", bg="Light Sea Green",command=wordFrequencytext,width=10)
sendfile.grid(row=5,column=0)

sendtxt = tk.Button(window, text="Open txt file",fg="ghostwhite", bg="Light Sea Green", command=txtfileopener, width=13)
sendtxt.grid(row=5,column=7)

showtxtfile=tk.Button(window, text="Show file results",fg="ghostwhite", bg="Light Sea Green", command=wordFrequencytxtfile, width=13)
showtxtfile.grid(row=6,column=7,pady=5)

results= tk.LabelFrame(window,text="Word Frequency\n Calculator", bd=5, height=340, width=150, bg="Light Sea Green", relief="sunken")
results.pack_propagate(0)
results.grid(row=0, column=7)

clearbutton = tk.Button(window,command=FrameRefresher, text="Clear Board", fg="ghostwhite", bg="Light Sea Green", width=10)
clearbutton.grid(pady=5, column=0,row=6)

window.mainloop()