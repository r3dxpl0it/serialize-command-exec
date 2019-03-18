from core import paramiko

def run_ssh_command(host , port , user ,  key , commands , verbose = True) : 
    import paramiko
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(host , port , username=user, key_filename=key)

    for command in commands : 
        if verbose : 
            print ('[SSH]','Running' , '"'+command+'"' , '===>' ,  user+'@'+host)
        stdin, stdout, stderr = ssh.exec_command(command)
        print (stdout.readlines())

    ssh.close()
