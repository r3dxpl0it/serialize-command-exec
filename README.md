# serialize-command-exec
serialize-command-exec is a tool for running serialize commands on ssh 
#### Usage : 
    python3 SSHC.py --rconfig config.json --mconfig tasks.json
    Required Options:
      --rconfig REMOTECONFIGFILE
                            path to REMOTE HOST config file
      --mconfig MAINCONFIGFILE
                            path to MAIN config file
      -v VERBOSE            Verbosity
      
#### remote host config
    { "SSH" : 
      {
        "SERVER1" : {
          "host": "RHOST",
          "user": "ubuntu",
          "path_to_key": "PATH/TO/KEY",
          "port": 22 
          } , 
         "SERVER2" : {
          "host": "RHOST2",
          "user": "ubuntu",
          "path_to_key": "PATH/TO/KEY2",
          "port": 22 
          } 
      } , 
      "LOCAL" : {}
    }

#### task config

    { 
        "RUN SERVER1 INTERACTIVE" : 
            {
            "action" : "intractive" , 
            "hosts" : ["SERVER1"]
            } , 
        "RUN LS AND DIR ON SERVER1" : 
            {
            "action" : "command" , 
            "hosts" : ["SERVER1"],
            "commands" : 
            ["ls" ,
             "dir"]
            }

    }
#### Contib and Warranty 
1) Contibs Are Extermily Welcome 
2) I Use this a version of this script on daily basis for monitoring and command exec but it comes with no Warranty or ... 

