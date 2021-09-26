# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 00:53:16 2021
"""

import PyPDF2
import glob
from natsort import natsorted
import pandas as pd
from nltk.tokenize import word_tokenize 

pdfs = glob.glob(r'E:\datathon\tagged\*.pdf')

new_merged_pdf = 'E:\datathon\tagged\new_merged_pdf.pdf'

merge_pdfs = PyPDF2.PdfFileMerger()

for pdf in natsorted(pdfs):
    merge_pdfs.append(open(pdf, 'rb'))
    
merge_pdfs.write(open(r'E:\datathon\tagged\new_merged_pdf.pdf','wb'))

read_pdf = PyPDF2.PdfFileReader(open(r'E:\datathon\tagged\new_merged_pdf.pdf', 'rb'))
x = read_pdf.numPages


print(x)
extracted_Text = ""

for i in range(1, x):
    extracted_Text += read_pdf.getPage(i).extractText()

with open(r"E:\datathon\tagged\new_merged_text.txt","w", encoding='utf-8') as f:
    f.write(extracted_Text) 

words = word_tokenize(extracted_Text)
#print(words)



import spacy
#from spacy import displacy
spacy.__version__
nlp = spacy.load("en_core_web_sm")
doc = nlp(extracted_Text)

entities = []
labels = []
position_start = []
position_end = []

for ent in doc.ents:
    entities.append(ent)
    labels.append(ent.label_)
    position_start.append(ent.start_char)
    position_end.append(ent.end_char)
    
df = pd.DataFrame({'Entities':entities,'Labels':labels,'Position_Start':position_start, 'Position_End':position_end})

writer = pd.ExcelWriter('E:/datathon/tagged/new_merged.xlsx')
# write dataframe to excel

df.to_excel(writer)
# save the excel
writer.save()
print('DataFrame is written successfully to Excel File.')
energy = spacy.explain("Energy")
energy