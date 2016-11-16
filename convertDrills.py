# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 12:54:25 2016

@author: DTalaiver

This script converts G83 instructions to grbl accepted G-code.
"""

#drill parser

import Tkinter as tk
import tkFileDialog 

root = tk.Tk()
root.withdraw()
root.deiconify()
root.lift()
root.focus_force()
root.withdraw()
file_path = tkFileDialog.askopenfilename(parent=root)

outfile = open(file_path[:-3]+'4grbl.nc', 'w')
retractFeed = 'F20'
clearHeight = '0.25'
with open(file_path) as f:
    for line in f:
        content = line
        elements = content.split(" ")
        if elements[0] != "G83": #if its not G83 just pass it out
            outfile.write(content)
        else:
            #extract elements from command
            for q in range(0,len(elements)):
                if "X" in elements[q]:
                    xCmd = elements[q]
                elif "Y" in elements[q]:
                    yCmd = elements[q]
                elif "Z" in elements[q]:
                    bottom = float(elements[q][1:])
                elif "Q" in elements[q]:
                    increment = float(elements[q][1:])
                elif "R" in elements[q]:
                    retract = (elements[q][1:])
                elif "F" in elements[q]:
                    plunge = elements[q]
            #begin pecking
            #go to position
            outfile.write('G0'+xCmd+yCmd+"\n")
            curDepth=0
            outfile.write('G0Z0'+"\n")
            while (curDepth>bottom):
                curDepth=curDepth-increment
                if curDepth<=bottom:
                    curDepth=bottom
                #plunge
                outfile.write('G1'+'Z'+str(curDepth)+plunge)
                #retract
                outfile.write('G1'+'Z'+retract+retractFeed+"\n")
            #pecking done
            outfile.write('G0Z'+clearHeight+"\n")
           
                
        


outfile.close()
