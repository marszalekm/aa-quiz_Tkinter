#!/usr/bin/env python3

# For Python 3.6.9, Tkinter 8.6
# Author: Michal Marszalek
# Simple script, which is sort of a quiz with GUI based on Tkinter module to Python, 
# that lets you check your knowledge of aminoacid naming, i.e. one letter and three letters names.

import tkinter as tk
import random

aa = []
with open('aminoacids-list.txt', 'r') as f:
    for line in f:
        '''
        aa is a list containing information about aminoacids
        extracted from aformentioned file.
        '''
        aa.append(line.strip().split())
        

class Quiz():

    def __init__(self, root):
        '''
        Establishment of basic parts of quiz i.e. buttons, labels or entry box 
        as well as their position inside the widget.
        '''

        self.root = root
        self.root.title("Aminoacids quiz")
        self.frame = tk.Frame(self.root)
        self.one = tk.Button(self.frame, text = "One letter quiz",command=self.oneletter)
        self.three = tk.Button(self.frame, text = "Three letters quiz",command=self.threeletter)
        self.check = tk.Button(self.frame, text = "Check answer",command=self.result)
        self.draw = tk.Button(self.frame, text = "Draw other aa",command=self.draw)
        self.titletext = tk.Label(self.frame, text = " Welcome to aminoacids quiz. Pick which type of test you would like.")
        self.instr = tk.Label(self.frame, text="")
        self.amino = tk.Label(self.frame, text="")
        self.score = tk.Label(self.frame, text="")
        self.entry = tk.Entry(self.frame, width=5)
        
        #Layout part
        self.frame.pack()
        self.titletext.pack(side='top', ipady=8)
        self.one.pack(side='left', anchor='nw', fill='both')
        self.three.pack(side='right', anchor='ne', fill='both')
        self.instr.pack(anchor='center')
        self.amino.pack(anchor='center', ipady=5)
        self.entry.pack(anchor='center')
        self.score.pack(anchor='center', ipady=5)
        self.check.pack(side='right', anchor='se')
        self.draw.pack(side='left', anchor='sw')
        #olet and tlet variables allows to distinguish which type of test was chosen
        self.olet = self.tlet = False
        self.rand = random.choice(aa)
        
    def draw(self):
        '''
        Allows to draw another aminoacid.
        '''
        self.rand = random.choice(aa)
        if self.olet is True and self.tlet is False:
            self.instr.configure(text="Enter a 'one letter' aminoacid: ")
            self.amino.configure(text="%s"%(self.rand[2]))
        elif self.olet is False and self.tlet is True:
            self.instr.configure(text="Enter a 'three letters' aminoacid: ")
            self.amino.configure(text="%s"%(self.rand[2]))
        elif self.olet is False and self.tlet is False:
            self.score.configure(text="First pick quiz type")
        else:
            self.score.configure(text="Unexpected error")

    def result(self):
        '''
        Checks if the answer in entry box is correct,
        depending on type of quiz which was chosen.
        '''
        self.box = self.entry.get()
        self.box = self.box.lower().capitalize()
        if self.olet is True and self.box == self.rand[0]:
            self.score.configure(text="Correct ")
        elif self.tlet is True and self.box == self.rand[1]:
            self.score.configure(text="Correct ")
        elif self.box == '':
            self.score.configure(text="Entry window is empty")
        else:
            self.score.configure(text="Wrong ")

    def oneletter(self):
        '''
        Defines 'one letter' quiz.
        '''
        self.instr.configure(text="Enter a 'one letter' aminoacid: ")
        self.score.configure(text="")
        self.amino.configure(text="%s"%(self.rand[2]))
        self.olet = True
        self.tlet = False

    def threeletter(self):
        '''
        Defines 'three letters' quiz.
        '''
        self.instr.configure(text="Enter a 'three letters' aminoacid: ")
        self.score.configure(text="")
        self.amino.configure(text="%s"%(self.rand[2]))
        self.olet = False    
        self.tlet = True

def main():
    root = tk.Tk()
    root.geometry('500x180')
    Quiz(root)
    root.mainloop()

if __name__ == "__main__":
    main()
