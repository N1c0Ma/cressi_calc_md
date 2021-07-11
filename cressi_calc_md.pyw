# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 21:28:57 2021

@author: Nicola Matthieu Mann
"""
from tkinter import*
from tkinter import filedialog as fd

def open_file():
    in_file = fd.askopenfilename(title = "Datei öffnen", filetypes = (("txt files","*.txt"), ("all files","*.*")), multiple = True)
    #in_file = fd.askopenfilename(initialdir = "/", title = "Datei öffnen", filetypes = (("txt files","*.txt"), ("all files","*.*")))
    in_file = list(in_file)
    for i in in_file:
        output_fn.insert(END, i.split("/")[-1])
    calc_md(in_file)

def calc_md(in_file):
    global md
    for files in in_file:
        int_d10 = []
        int_d1 = []
        int_d = []
        rat_d = []
        file = open(files, "r")
        lines = file.readlines()
        depths_raw = str(lines[3:4])    #choose lines for depths-data
        depths_sp = depths_raw.split("\\t") #split delimiter "\t"
        depths_ch = depths_sp[1:]   #choose data-points
        print(depths_ch)
        for i in range(len(depths_ch)):
            int_d10.append(depths_ch[i][0])  #make integer ten num-list
            if depths_ch[i][1].isdecimal():
                int_d1.append(depths_ch[i][1])  #append if number of ones = True as string
            else:
                int_d1.append(0)    #append if not 0 as integer
            if isinstance(int_d1[i], str):
                int_d.append(int_d10[i] + int_d1[i])    #assemble tens and ones as strings    
            else:
                int_d.append(int(int_d10[i]) + int_d1[i])   #or convert to int and assemble ints
            if depths_ch[i][2].isdecimal(): 
                rat_d.append(depths_ch[i][2])  #make rational num-list if [2] is decimal
            else:
                rat_d.append(depths_ch[i][3])   #if not take [3]
            try:
                int_d[i] = int(int_d[i])    #convert to int
                rat_d[i] = int(rat_d[i])    #convert to int
            except notallnumbers:
                output_sol.insert(END, "error")
            md = round((sum(int_d) + sum(rat_d) / 10) / len(depths_ch), 1)  #make sums, divide rational sum / 10, divide through num data-points, round
        if int_d == [] or rat_d == []:
            output_sol.insert(END, "error")
        else:
            output_sol.insert(END, md)
        print(int_d)
        print(rat_d)
        print(md)
    

        
            
#def callback():
    #output_sol.insert(0, md_t)
    
def del_listbox():
    for i in output_fn, output_sol:
        i.delete(0, END)

window=Tk()
window.geometry("410x175")
window.title("TG-Durchschnittstiefe berechnen")

button_of = Button(window, text = "Dateien öffnen", command = open_file)
#button_calc = Button(window, text = "berechne", command = callback)
button_del = Button(window, text = "löschen", command = del_listbox)
scrollbar_fn = Scrollbar(window)
scrollbar_sol = Scrollbar(window)
output_fn = Listbox(window, yscrollcommand = scrollbar_fn.set, width = 30, height = 4)
output_sol = Listbox(window, yscrollcommand = scrollbar_sol.set, width = 30, height = 4)
scrollbar_fn.config(command = output_fn.yview)
scrollbar_sol.config(command = output_sol.yview)
label1 = Label(window, text = "Durchschnittstiefe:")

output_fn.grid(row = 1, column = 2, padx = 20, pady = 10)
output_sol.grid(row = 2, column = 2, padx = 20, pady = 5)
scrollbar_fn.grid(row = 1, column = 2, sticky = "ens", pady = 10)
scrollbar_sol.grid(row = 2, column = 2, sticky = "ens", pady = 5)
button_of.grid(row = 1, column = 1, padx = 20, pady = 10, sticky = "n")
button_del.grid(row = 1, column = 1, padx = 20, pady = 10, sticky = "s")
#button_calc.grid(row = 3, column = 1, columnspan = 1, padx = 20, pady = 10)
label1.grid(row = 2, column = 1, rowspan = 2, columnspan = 1, padx = 20, pady = 5)
mainloop()
