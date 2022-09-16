""" 
Клиент для подключения и выполнения команды по ssh
---------------------------------------------------------------------
Пример выполнения
Ресурс - http://blackbox.smashthestack.org:85/ 

Username: level1
Password: 
Enter server IP: blackbox.smashthestack.org
Enter port or <CR>: 2225
Enter command or <CR>: 
--- Output ---
uid=1002(level1) gid=1005(gamers) groups=1002(level1),1005(gamers
---------------------------------------------------------------------
"""
import paramiko

def ssh_command(ip, port, user, passwd, cmd):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port=port, username=user, password=passwd)
    _, stdout, stderr = client.exec_command(cmd)
    output = stdout.readlines() + stderr.readlines()
    if output:
        print('--- Output ---')
        for line in output:
            print(line.strip())

if __name__ == '__main__':
    import getpass
    # user = getpass.getuser()
    user = input('Username: ')
    password = getpass.getpass()
    ip = input('Enter server IP: ') or 'example.com'
    port = input('Enter port or <CR>: ') or 2225
    cmd = input('Enter command or <CR>: ') or 'ls'
    ssh_command(ip, port, user, password, cmd)
