
#Restart munionagent.

import os
import time
import sys
import subprocess
from threading import Thread

def subprocess_basic(command):
    procedure = subprocess.Popen(command, stdout=subprocess.PIPE, shell=False)
    processq = procedure.communicate()[0].strip()
    print(processq)


def main_exe():

    print('Troubleshooting WinnowVision box\nRestarting munionagent...')
    print('\nPress ctrl + d')
    subprocess_basic("C:\\Windows\\Sysnative\\bash.exe ; \
    ./fix_general_1.sh ; exit  \
    ")
    input('\nFinished. Press enter')

if __name__ == "__main__":
    main_exe()
