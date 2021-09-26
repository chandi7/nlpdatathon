# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 00:53:16 2021

@author: claxman093019
"""

import PyPDF2

import glob
from natsort import natsorted
import pandas as pd
import nltk
nltk.download()
from nltk.tokenize import word_tokenize 


#pdfFileObj = open(r'C:\Users\claxman093019\OneDrive - GROUP DIGITAL WORKPLACE\Desktop\datathon\tagged\cmacgm-2020.pdf', 'rb')

pdfs = glob.glob(r'C:\Users\claxman093019\OneDrive - GROUP DIGITAL WORKPLACE\Desktop\datathon\tagged\*.pdf')

new_merged_pdf = 'C:\Users\claxman093019\OneDrive - GROUP DIGITAL WORKPLACE\Desktop\datathon\tagged\new_merged_pdf.pdf'

merge_pdfs = PyPDF2.PdfFileMerger()

for pdf in natsorted(pdfs):
    merge_pdfs.append(open(pdf, 'rb'))
    

merge_pdfs.write(open(new_merged_pdf, 'wb'))

read_pdf = PyPDF2.PdfFileReader(open(r'C:\Users\claxman093019\OneDrive - GROUP DIGITAL WORKPLACE\Desktop\datathon\tagged\new_merged_pdf.pdf', 'rb'))
x = read_pdf.numPages
#print(x)
#pdf_Obj = read_pdf.getPage(x-1)

#print(pdf_Obj.extractText())

#extracted_Text = pdf_Obj.extractText()

extracted_Text = ""

for i in range(1, x):
    extracted_Text += read_pdf.getPage(i).extractText()

with open(r"C:\Users\claxman093019\OneDrive - GROUP DIGITAL WORKPLACE\Desktop\datathon\tagged\new_merged_text.txt","w", encoding='utf-8') as f:
    f.write(extracted_Text)  


print(extracted_Text)

words = word_tokenize(extracted_Text)
words

