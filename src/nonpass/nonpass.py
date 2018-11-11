import paramiko
import scp
import os
import csv

'''
nonpass

1. csv read
2. send to create_pub_key.py source host.
3. send to setting_pub_key.py target host.
'''

GENERATE_PUB_KEY = '/tmp/create_pub_key.py'
SETTING_PUB_KEY = ''

def main():
    with open('C:\\Users\\ayc08\\Documents\\GitHub\\python_study\\src\\nonpass\\sample\\sample.csv', 'r') as f:
        read = csv.DictReader(f)
        for row in read:
            source_host = row.get('source_host')
            print(source_host)

            source_host_fqdn = source_host + '.b.' + source_host[-3:] + '.server'
            print(source_host_fqdn)

            with paramiko.SSHClient() as ssh:
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(hostname=source_host_fqdn, port=22, username="", password="")

                with scp.SCPClient(ssh.get_transport()) as scp:
                    scp.put('','')
                    source_dir = row.get('source_directory') + '/.ssh'

                    stdin, stdout, stderr = ssh.exec_command('python ' + GENERATE_PUB_KEY + ' ' + source_dir)
                    scp.get('','')
                    ssh.exec_command('rm ' + GENERATE_PUB_KEY)

            target_host = row.get('target_host')
            print(target_host)

            target_host_fqdn = target_host + '.b.' + target_host[-3:] + '.server'
            print(target_host_fqdn)

            with paramiko.SSHClient() as ssh:
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(hostname=target_host_fqdn, port=22, username="", password="")

                with scp.SCPClient(ssh.get_transport()) as scp:
                    scp.put('','')
                    target_dir = row.get('target_directory') + '/.ssh'

                    stdin, stdout, stderr = ssh.exec_command('python ' + SETTING_PUB_KEY + ' ' + target_dir)
                    ssh.exec_command('rm ' + SETTING_PUB_KEY)


        



if __name__ == '__main__':
    main()
