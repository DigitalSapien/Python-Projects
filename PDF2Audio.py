# PDF --> Audio  

import pyttsx3
import PyPDF2

book = open('A+.pdf','rb' )
pdfReader = PyPDF2.PdfReader(book)
pages = len(pdfReader.pages)
print(pages)

audio = pyttsx3.init()
page = pdfReader.pages[31]
text = page.extract_text()
audio.say(text)
audio.runAndWait()

# !! Outputs a mp3 File, Saves it to the Downloads folder.

