#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkFileDialog
import tkMessageBox
import Tkinter
import os
import sys

# init root tk and finish it
root = Tkinter.Tk()
root.withdraw()


# VARS

JPG_LIST = []
NEF_LIST = []
DEL_LIST = []


# MAIN: ask for dir
dirname = tkFileDialog.askdirectory(title="Izberi mapo", initialdir='D://', mustexist=True)

if not dirname:
  sys.exit()

# MAIN: list the dir
for filename in os.listdir(dirname):

  if filename.lower().endswith('.jpg'):
    JPG_LIST.append(dirname + '/' + filename)
  elif filename.lower().endswith('.nef'):
    NEF_LIST.append(dirname + '/' + filename)

# MAIN: compare .nef vs .jpg files
for NEF_FILE in NEF_LIST:

  JPG_FILE = NEF_FILE.replace('.NEF', '.JPG').replace('.nef', '.jpg')

  if JPG_FILE not in JPG_LIST:
    DEL_LIST.append(NEF_FILE)

# MAIN: delete .nef files
DEL_COUNT = len(DEL_LIST)
if not len(DEL_COUNT):
  tkMessageBox.showinfo(title='Prazen seznam', message='Ne najdem nobene .nef brez .jpg para')
else:
  yesno = tkMessageBox.askyesno(title='Izbrišem datoteke?', message='Izbrisanih bo %d datotek.' % DEL_COUNT)

  if not yesno:
    sys.exit()
    
  for DEL_FILE in DEL_LIST:
    print 'Brisem', DEL_FILE
    os.unlink(DEL_FILE)
