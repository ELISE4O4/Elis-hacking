#!/user/bin/python3
#pip3 install python-nmap

import nmap
sc = nmap.Port.Scanner()
print("""              _           _ /n
  _ _ _  ___ | |__ ___  _| |__   _ _ /n
 | | | |<_> || / // ._>/ . |\ \/| | |/n
 |__/_/ <___||_\_\\___.\___|/\_\`_. |/n
                                <___'/n""")

def main():
    n = input("1- Network scanner\n2- Vulnerabilities Det>
if n == '1':
   nmap()

if n == '2':
   vuln()

if n == '3':
    os.system('msfconsole')
else :
   print(" Please Enter a number bitween 1 and 3 ")

print("*******Welcome to Network scanner******")
print(" ******Auteur: Elisé Fidegnon ****** "
print("***************************************")
ip = input("\nPlease Enter the Ip adress :")
sc.scan(ip ,'1- 1024')
print(sc.scaninfo())
print(sc[ip]['tcp'].keys())


def vuln():
    print("**Welcom to Vulnerabilities scanne**")
    print("************************************")
    ip = input("\nPlease Enter the Ip adress :")
    print(os.system('nmap -Sv --script=vulscan.nse ' +ip))





if __name__ == "main":
    main()
