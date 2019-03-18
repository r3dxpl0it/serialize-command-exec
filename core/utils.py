from core import platform , argparse
import os 
import json


def check_ver() : 
        if not int(platform.python_version()[0]) >= 3 : 
                print("Version not Satisfiable ! Try With Python > 3 ")
                raise SystemExit

def cli_parser() : 

        parser = argparse.ArgumentParser(prog = './client.py' , 
                   usage = './client.py --config <path/to/config>')

        req_commands = parser.add_argument_group('Required Options')
        req_commands.add_argument('--rconfig',  help='path to REMOTE HOST config file', dest='remoteconfigfile' , required = True)
        req_commands.add_argument('--mconfig',  help='path to MAIN config file', dest='mainconfigfile' , required = True)
        req_commands.add_argument('-v',  help='Verbosity', dest='verbose' , type = bool , default = False)

        args = parser.parse_args()         
        return args.remoteconfigfile , args.mainconfigfile , args.verbose

def read_files() : 
        remote , conf , verb = cli_parser()
        

        if os.path.isfile(remote) and os.path.isfile(conf) : 
                try : 
                        file1 = open(remote , 'r')
                        file2 = open(conf , 'r')
                        remote_file = json.load(file1)
                        conf_file = json.load(file2)
                        if verb : 
                                print (remote_file , conf_file)
                        return remote_file , conf_file

                except json.decoder.JSONDecodeError as e : 
                        print ('[Error in Parsing Json Config]', e)
                        quit()
        else :
                print('FileNotFound')
                raise FileNotFoundError
def check() : 
        check_ver()
         
