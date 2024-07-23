from PyPDF2 import PdfFileWriter, PdfFileReader
import getpass
import pyfiglet
from colorama import init
init()
from colorama import Fore , Back , Style

writer = PdfFileWriter()
pdf_name = input('Enter name of pdf with (.pdf) :')
original_file = PdfFileReader(pdf_name)
for page in range(original_file.numPages):
    writer.addPage(original_file.getPage(page))
password = getpass.getpass(prompt = "Create Password: ")
writer.encrypt(password)
with open('new_secret.pdf', 'wb') as f:
    writer.write(f)
    f.close()
    word = pyfiglet.figlet_format("new secret.pdf",font="alphabet")
    print(word)
    print("you get copy of your pdf in your current dir .")
    print(Back.RED,"With Name #### new_secret.pdf ####")

