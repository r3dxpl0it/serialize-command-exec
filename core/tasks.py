
from core.utils import *
from core import *
import time 

def run_tasks() : 
    config_file  , tasks_file = read_files()
    
    for task in tasks_file.keys() : 
        if tasks_file[task]['action'] == 'command' : 
            for host in tasks_file[task]['hosts'] : 
                if host in list(config_file["SSH"].keys()) : 
                    run_ssh_command(config_file['SSH'][host]['host'] ,
                        config_file['SSH'][host]['port'] ,
                        config_file['SSH'][host]['user'] ,
                        config_file['SSH'][host]['path_to_key'] ,
                        tasks_file[task]['commands'] ,
                        verbose= True)
                elif host == 'LOCAL' : 
                    for command in tasks_file[task]['commands'] : 
                        print ('[LOCAL]','Running' , '"'+command+'"')
                        os.system(command)

        elif tasks_file[task]['action'] == 'intractive' : 
            try : 
                for host in tasks_file[task]['hosts'] : 
                    if host in list(config_file["SSH"].keys()) : 
                        sshClient = paramiko.SSHClient()
                        sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                        sshClient.connect(config_file['SSH'][host]['host'], username=config_file['SSH'][host]['user'], key_filename = config_file['SSH'][host]['path_to_key'])
                        channel = sshClient.get_transport().open_session()
                        channel.get_pty()
                        channel.invoke_shell()

                        while True:
                            command = input('$')
                            if command == 'exit':
                                break

                            channel.send(command + "\n")

                            while True:
                                if channel.recv_ready():
                                    output = channel.recv(1024)
                                    print (output)
                                else:
                                    
                                    if not(channel.recv_ready()):
                                        break

                        sshClient.close()
            except KeyboardInterrupt : 
                print( 'Exiting Intractive')


