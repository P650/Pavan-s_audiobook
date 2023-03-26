# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 00:38:30 2023

@author: Pavankumar
"""

#required
# pip install PyPDF2 pyttsx3

from PyPDF2 import PdfFileReader
import pyttsx3
import PyPDF2

# path of the PDF file
path = open('C:/Users/Pavankumar/Downloads/Living with the Himalayan Masters ( PDFDrive ).pdf', 'rb')

# creating a PdfFileReader object
pdfReader = PyPDF2.PdfReader(path)

number_of_pages = len(pdfReader.pages)
page = pdfReader.pages[50]

text = page.extract_text()

engine = pyttsx3.init()

voices = engine.getProperty('voices')
#Male
engine.setProperty('voice', voices[0].id)  

#Female
# engine.setProperty('voice', voices[1].id)

engine.setProperty('rate', 150)

engine.setProperty('volume',.75)

engine.say(text)
engine.runAndWait()