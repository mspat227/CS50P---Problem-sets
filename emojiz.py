from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 3 and (sys.argv[1].lower() == "-f" or sys.argv[1].lower() == "--font"):
    for i in range(len(fonts)):
        if fonts[i] == sys.argv[2].lower():
            input_font = sys.argv[2].lower()
            break
        else:
            sys.exit("Invalid usage")  
elif len(sys.argv) == 1:
    input_font = random.choice(fonts) 
else:
    sys.exit("Invalid usage")   


x = input("Input: ").strip()

f = Figlet(font = input_font)

print(f.renderText(x))





#f = Figlet(font='slant')

#print(f.renderText('text to render'))