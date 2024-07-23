import pyfiglet
from colorama import init
init()
from colorama import Fore , Back , Style

word = pyfiglet.figlet_format("Novemebr",font="alphabet")

print(word)
print(Fore.GREEN,"hello November")
print(Back.RED,"hello November")
