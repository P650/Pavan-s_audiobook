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
import os


def read_book():
    
    # pdf = 'C:/Users/Pavankumar/Downloads/Living with the Himalayan Masters ( PDFDrive ).pdf'
    print("Enter the path of the file location!!")
    pdfPath = str(input())     
    if not pdfPath:
        print("You must have to enter the PDF path")
    else:
        filename = os.path.basename(pdfPath)
        print("You are reading: " + filename)
        
          
    # path of the PDF file
    path = open(pdfPath, 'rb')
    
    # creating a PdfFileReader object
    pdfReader = PyPDF2.PdfReader(path)
    
    number_of_pages = len(pdfReader.pages)
    print("Enter the page number you want to read out of: " + str(number_of_pages))
    page_number = int(input())
    page = pdfReader.pages[page_number]
    
    text = page.extract_text()
    # print(text)
    
    engine = pyttsx3.init()
    
    voices = engine.getProperty('voices')
    #Male
    engine.setProperty('voice', voices[0].id)  
    
    #Female
    # engine.setProperty('voice', voices[0].id)
    
    # print("Default speed set to 150 words per minute")
    # wordCount = ''
    # if not wordCount:
    #     engine.setProperty('rate', 150)
    # else:
    #     print("Enter the desired words per minute")
    #     wordCount = int(input())
    #     engine.setProperty('rate', wordCount)
    
    
    engine.setProperty('rate', 150)
    engine.setProperty('volume',.75)
    
    engine.say(text)
    engine.runAndWait()
    

def main():
    read_book()
    

if __name__ == "__main__":
    main()    