from pdf2docx import Converter, parse
from docx2pdf import convert

pdf = 'pdf.pdf'
word = 'word.docx'
# word = 'was.docx'

cv = Converter(pdf)
cv.convert(word, start=0, end=None)
cv.close()

# parse(pdf, word)

'''word to pdf'''
# convert(word)