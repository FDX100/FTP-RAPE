import os
choice = raw_input('to install press (Y) to uninstall press (N) >> ')
run = os.system
if choice =='Y' or choice=='y':
    run('chmod 777 FTP-RAPE.py')
    run('mkdir /usr/share/ftp-rape')
    run('cp FTP-RAPE.py /usr/share/ftp-rape/FTP-RAPE.py')

    cmnd=(' #! /bin/sh \n exec /usr/share/ftp-rape/FTP-RAPE.py "$@"')
    with open('/usr/bin/FTP-RAPE','w')as file:
        file.write(cmnd)
    run('chmod +x /usr/bin/FTP-RAPE & chmod +x /usr/share/ftp-rape/FTP-RAPE.py')
    print('''\n\ncongratulation FTP-RAPE installed successfully \nfrom now just type \x1b[6;30;42m FTP-RAPE\x1b[0m in terminal ''')
if choice=='N' or choice=='n':
    run('rm -r /usr/share/ftp-rape ')
    run('rm /usr/bin/FTP-RAPE ')
    print('[!] now FTP-RAPE has been removed successfully')
