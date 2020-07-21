import requests,re,os
import time
import sys
from os import system
from platform import platform
from time import sleep
import os

time.sleep(1)

print("loading modules...")
time.sleep(0.05)
os.system('clear')
print("lOading modules...")
time.sleep(0.05)
os.system('clear')
print("loAding modules...")
time.sleep(0.1)
os.system('clear')
print("loaDing modules...")
time.sleep(0.1)
os.system('clear')
print("loadIng modules...")
time.sleep(0.1)
os.system('clear')
print("loadiNg modules...")
time.sleep(0.1)
os.system('clear')
print("loadinG modules...")
time.sleep(0.1)
os.system('clear')
print("loading modules...")
time.sleep(0.1)
os.system('clear')
print("loading mOdules...")
time.sleep(0.1)
os.system('clear')
print("loading moDules...")
time.sleep(0.1)
os.system('clear')
print("loading modUles...")
time.sleep(0.1)
os.system('clear')
print("loading moduLes...")
time.sleep(0.1)
os.system('clear')
print("loading modulEs...")
time.sleep(0.1)
os.system('clear')
print("loading moduleS...")
time.sleep(0.1)
os.system('clear')
print("loading modules...")
time.sleep(0.1)
os.system('clear')
print("Loading modules...")
time.sleep(0.1)
os.system('clear')
print("lOading modules...")
time.sleep(0.1)
os.system('clear')
print("loAding modules...")
time.sleep(0.1)
os.system('clear')
print("loaDing modules...")
time.sleep(0.1)
os.system('clear')
print("loadIng modules...")
time.sleep(0.1)
os.system('clear')
print("loadiNg modules...")
time.sleep(0.1)
os.system('clear')
print("loadinG modules...")
time.sleep(0.1)
os.system('clear')
print("loading Modules...")
time.sleep(0.1)
os.system('clear')
print("loading mOdules...")
time.sleep(0.1)
os.system('clear')
print("loading moDules...")
time.sleep(0.1)
os.system('clear')
print("loading modUles...")
time.sleep(0.1)
os.system('clear')
print("loading moduLes...")
time.sleep(0.1)
os.system('clear')
print("loading modulEs...")
time.sleep(0.1)
os.system('clear')
print("loading moduleS...")
time.sleep(0.1)
os.system('clear')
print("loading modules...")
time.sleep(0.1)
os.system('clear')
print('''
       ▪
               ▪
▀▀▀ ▀▀▀▀ ▀ ▀ ▀▀▀ ▀▀▀▀ ▀▀▀ ▀▀▀
▀ 							  ▀
 ▀  ▀ ▀ ▀  ▀▀ ▀ ▀▀ ▀ ▀   ▀   ▀            
 ▀   ▀                ▀     ▀ 
 ▀   ▀    ▪ ▀ ▀▀ ▀▀ ▀▀     ▀
  ▀    ▀     ▀            ▀ 
   ▀    ▀      ▀▀ ▀ ▀ ▀ ▀  ▪ 
    ▀    ▀                     
     ▀    ▀       ▀ ▀ ▀▀▀▪
  ▪    ▀    ▀    ▀      ▀
        ▀    ▀ ▀      ▀ ▪
         ▀    ▀     ▀ 
          ▀      ▀▪ 
            ▀  ▀


   kven: proxy server changes 


	''')
print('what Linux distribution are you using?')
linux = input("> ")
if linux == 'ubuntu':
	os.system('sudo apt install tor')
elif linux == 'Ubuntu': 
	os.system('sudo apt install tor')
elif linux == 'Debian': 
	print('visnce')
elif linux == 'Kali Linux':
	os.system('apt install tor')
elif linux == 'kali linux': 
	os.system('apt install tor')
elif linux == 'Kali': 
	os.system('apt install tor')
elif linux == 'kali': 
	os.system('apt install tor')
elif linux == 'termux':
	os.system('apt install tor')
elif linux == 'Termux': 
	os.system('apt install tor')
else: 
	os.system('apt install tor')

os.system('tor')

def get_proxy (url: str) -> str:
	
    a = requests.get(url)
    filename = "proxies.txt"

    file = open(filename, 'w+')
    file.write(a.text) 
    file.close()

    return filename