#intarface
import os
os.system("clear")
import smtplib
import json
import os
try:
 import requests
except:
 os.system("pip install requests")
 import requests
import time
from requests.structures import CaseInsensitiveDict

from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
#CVALUE
blue= '\33[94m'
lightblue = '\033[94m'
red = '\033[91m'
white = '\33[97m'
yellow = '\33[93m'
green = '\033[1;32m'
cyan  = "\033[96m"
end = '\033[0m'
purple="\033[0;35m"
os.system('clear')
line=red+" The Tools Varson : 2.0 "

space=" "
os.system("clear")
logo=print(blue+"""
······················;ρβΜΜΜΜΜΜμ;
···················;ρΜΜΠ΅Ε;ΪΜΜΪΫΜΜμ
··················ΔΜΒ΄ΚΚκκΚΪΜΜΜΜΜΪΜΜΝ
················χβΒ;ΚΚκΚΚκκΪΜΜΜΜΜΜΜΫΜΜμ
···············ΔΜΠΚΨκΚΚκΚΚκΪΜΜΜΜΜΜΜΜΜΜΜμ
··············βΜΠΨκΚΨκΚΨκΚΚΪΜΜΜΜΜΜΜΜΜΜΆΜΝ
·············βΜΠκΚΨκΚΨκΚΨκΚΪΜΜΜΜΜΜΜΜΜΜΜΆΜΝ
············βΜΉΚ;κΚ;κΚΨκΚΨκΪΜΜΜΜΜΜΜΜΜΜΜΜΆβΝ
···········βΜΠ;χρρβββΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜβββββΆΜΝ
··········ΔΜΜΜΜΜΜΫΆΫΫΫΫΫΫΫΫΫΫΆΫΫΆΫΫΫΜΪΆΜΜΜΜΜΝ
·········έΜΜΚΜΜΜΜΜΝ········Τ;κΚΨκΚΨΕβΜΜΜΜΜΫΜΜΉ
·········΅ΜΜβΜΜΜΜΜΜμ·······;Κ;κΚ;κΚΚΜΜΜΜΜΜχβΜ
···········΅ΜΜβΜΜΜΜΜμ······ΤκΚ;κΚ;χΜΜΜΜΜββΜΓ
············;ΪΜΜββΜΜΜμ·····ΤκκΚκ;κΜΜΜψβΜΜΏ
·········;ρβΜΜΫΫΆΜΜββΜΜΜμμμΙρχρβΜΜψββΜΜΚΪΜΜΜμ;
······χρΜΜΜΫΜΜΜΜΜΜΪΜΜΜββΜΜΜΜΜΜΜβββΜΜΫΜΜΜΜΜΜΪΜΜΜμ
·····βΜΜβΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜβΜΝ
····βΜΜΜΠ·····································ΪΜβΜΝ
···ΔΜΜΜΜΉ·····································ΪΜΜΆΜΝ
··ΔΜΜΜΜΜΝ············;ρβΜΜΜΜΜΜΜμ··············ΚΜΜΜΜΜ
·χΜΒΜΜΜΜψ···········χΜΜΜΜΜΜΜΜΜΜΜΜ·············βΜΜΜΜΜΜ
χΜΒΜΜΜΜΜΝ···········ΜΜΜΜΜΜΜΜΜΜΜΜΜΝ············βΜΜΜΜΜΜ
βΜΜΜΜΜΜΜβ···········Μψ·΅΅ΓΜΏ΅΅΄·ΜΡ············ΜβΜΜΜΜΫ
ΜβΜΜΜΜΜβΜ···········ΫΜΝμρβΜΜΝμρβΜ·············ΜβΜΜΜΜΜ
ΪΜβΜΜΜΜβΜ············ΜΜΜΜΏΔμΪΜΜΜΝ·············ΜβΜΜΜΜβ
·΅ΜΜβΜΜβΜ············΅΅ΪΜΜΜΜΜΜ΅΅··············ΜβΜΜββΜ
··;ΫβΜββΜ··············΄΅ΓΓ΅ΓΓ················πΜΒχβΜΠ
·;··ΜΜΜΜΜ;····································χΜΜΜΜΜ
·····΄ΫΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜMMMΜΜΜΜΜΜΜΜΜΜΜΜΜΠ
·······ΪΜμμμμμ  Adnan  Islam  Pankkhas μμμμμμμμμμ
·······΅ΫΫΫΫΫΫΫΫΫΫΫΫΫΫΫΫΫΫΫΫΫΫΫΫΫΫΫΫΫΫΫΫΫΫΫΫΫΫΫ""")


text=str(input(yellow+" \n\n\n Wellcom —=—........  \n\n\n \t\tEnter To Continue [>] : "))

text=lightblue+"\t\tModified By : "+yellow+"ADNAN..........Elite Cracker"+cyan+"\n\n\t\t★★ "+purple+"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"+cyan+"★★   \n" 
def header():
 print(logo)
 print(text)
 print(line)

#SEC
header()
print(red+"____________________________________________________")
print(blue+"\t\tYou need to security key")
print(red+"---------------------------------------------------‌‌‌‌‌‌‌-")
n=2
while n==2:
 a=str(input(red+"\n\n\t\t[>] Enter`~   Creator Security Key [>]"+green))
 if a=="Get_Love":
  print(green+"\n\n\t\t[ √ ] Request Accepted")
  n=3
 else:
  print(red+"\n\n\t\t[ × ] Incorrect security code!\n\t\tPlease Try Again")
  n=2
  text=str(input(" Press Entar To Continue :  "))

#main part
import os
os.system(" clear")
print("""
▇▇┈┈┈┈╱▔▔▔▔╲┈┈┈┈▇▇  ▇▇┈┈┈┈╱▔▔▔▔╲┈┈┈┈▇▇
▇▇┈┈┈▕▕╲┊┊╱▏▏┈┈┈▇▇  ▇▇┈┈┈▕▕╲┊┊╱▏▏┈┈┈▇▇
▇▇┈┈┈▕▕▂╱╲▂▏▏┈┈┈▇▇  ▇▇┈┈┈▕▕▂╱╲▂▏▏┈┈┈▇▇
▇▇┈┈┈┈╲┊┊┊┊╱┈┈┈┈▇▇  ▇▇┈┈┈┈╲┊┊┊┊╱┈┈┈┈▇▇
▇▇┈┈┈┈▕╲▂▂╱▏┈┈┈┈▇▇  ▇▇┈┈┈┈▕╲▂▂╱▏┈┈┈┈▇▇
▇▇╱▔▔▔▔┊┊┊┊▔▔▔▔╲▇▇  ▇▇╱▔▔▔▔┊┊┊┊▔▔▔▔╲▇▇
▇▇┈┈┈┈┈┈┈┈┈┈┈┈┈┈▇▇  ▇▇┈┈┈┈┈┈┈┈┈┈┈┈┈┈▇▇
▇▇┈┈┈┈┈┈┈┈┈┈┈┈┈┈▇▇  ▇▇┈┈┈┈┈┈~~~~~┈┈┈▇▇""")

#past 

import os
while True:
	os.system ("clear")
	print(red+"""
······················;ρβΜΜΜΜΜΜμ;
···················;ρΜΜΠ΅Ε;ΪΜΜΪΫΜΜμ
··················ΔΜΒ΄ΚΚκκΚΪΜΜΜΜΜΪΜΜΝ
················χβΒ;ΚΚκΚΚκκΪΜΜΜΜΜΜΜΫΜΜμ
···············ΔΜΠΚΨκΚΚκΚΚκΪΜΜΜΜΜΜΜΜΜΜΜμ
··············βΜΠΨκΚΨκΚΨκΚΚΪΜΜΜΜΜΜΜΜΜΜΆΜΝ
·············βΜΠκΚΨκΚΨκΚΨκΚΪΜΜΜΜΜΜΜΜΜΜΜΆΜΝ
············βΜΉΚ;κΚ;κΚΨκΚΨκΪΜΜΜΜΜΜΜΜΜΜΜΜΆβΝ
···········βΜΠ;χρρβββΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜβββββΆΜΝ
··········ΔΜΜΜΜΜΜΫΆΫΫΫΫΫΫΫΫΫΫΆΫΫΆΫΫΫΜΪΆΜΜΜΜΜΝ
·········έΜΜΚΜΜΜΜΜΝ········Τ;κΚΨκΚΨΕβΜΜΜΜΜΫΜΜΉ
·········΅ΜΜβΜΜΜΜΜΜμ·······;Κ;κΚ;κΚΚΜΜΜΜΜΜχβΜ
···········΅ΜΜβΜΜΜΜΜμ······ΤκΚ;κΚ;χΜΜΜΜΜββΜΓ
············;ΪΜΜββΜΜΜμ·····ΤκκΚκ;κΜΜΜψβΜΜΏ
·········;ρβΜΜΫΫΆΜΜββΜΜΜμμμΙρχρβΜΜψββΜΜΚΪΜΜΜμ;
······χρΜΜΜΫΜΜΜΜΜΜΪΜΜΜββΜΜΜΜΜΜΜβββΜΜΫΜΜΜΜΜΜΪΜΜΜμ
·····βΜΜβΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜβΜΝ
····βΜΜΜΠ·····································ΪΜβΜΝ
···ΔΜΜΜΜΉ·····································ΪΜΜΆΜΝ
··ΔΜΜΜΜΜΝ············;ρβΜΜΜΜΜΜΜμ··············ΚΜΜΜΜΜ
·χΜΒΜΜΜΜψ···········χΜΜΜΜΜΜΜΜΜΜΜΜ·············βΜΜΜΜΜΜ
χΜΒΜΜΜΜΜΝ···········ΜΜΜΜΜΜΜΜΜΜΜΜΜΝ············βΜΜΜΜΜΜ
βΜΜΜΜΜΜΜβ···········Μψ·΅΅ΓΜΏ΅΅΄·ΜΡ············ΜβΜΜΜΜΫ
ΜβΜΜΜΜΜβΜ···········ΫΜΝμρβΜΜΝμρβΜ·············ΜβΜΜΜΜΜ
ΪΜβΜΜΜΜβΜ············ΜΜΜΜΏΔμΪΜΜΜΝ·············ΜβΜΜΜΜβ
·΅ΜΜβΜΜβΜ············΅΅ΪADNANΜ΅΅··············ΜβΜΜββΜ
··;ΫβΜββΜ··············΄΅ΓΓ΅ΓΓ················πΜΒχβΜΠ
·;··ΜΜΜΜΜ;····································χΜΜΜΜΜ
·····΄ΫΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜMMMΜΜΜΜΜΜΜΜΜΜΜΜΜΠ
·······ΪΜμμμμμ  Adnan  Islam  Pankkhas μμμμμμμμμμ
·······΅ΫΫΫΫΫΫΫΫΫΫΫΫΫΫΫΫΫΫΫΫΫΫΫΫΫΫΫΫΫΫΫΫΫΫΫΫΫΫΫ""")


	print(red+" [>] ADNAN SMS BombeR ~For BD~\n [>] Contact Me–")
	a=str(input(" [+]select Your Option : "))
	if a =="1":
		os.system ("python3 bomb.py ")
		a=input()
	elif a=="2":
		os.system ("python3 cn.py")
		a=input()
	else:
		print(red+"[✘] Worng Value Entered")
		a=input()