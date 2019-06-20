

#title           :Currernt_containers_running
#description     :automate docker ps for control boxes
#author          :Andrew Kubal
#date            :2018
#version         :1
#usage           :python
#notes           :Winnow
#python_version  :3+
#====================================

import os
import time
import sys
import subprocess

def subprocess_basic(command):
    procedure = subprocess.Popen(command, stdout=subprocess.PIPE, shell=False)
    processq = procedure.communicate()[0].strip()
    print(processq)

def main_exe():

    file_docker = open("docker.txt", 'w+')
    print("Running check for current containers in docker...\nPress ctrl + d")

    result = subprocess.run("C:\\Windows\\Sysnative\\bash.exe ; \
    ./docker_ps_output.sh ;  \
    " , shell=True, stdout=file_docker)
    file_docker.close()

    lines = []
    with open ('docker.txt', 'rt') as provision_text:
        for line in provision_text:
            #print(lines)
            lines.append(line)

    m=0
    flag=0
    count=0
    ## inserted #
    image_listing = [
    'winnowtech/#fluentd',
    'winnowtech/#porter',
    'winnowtech/#wificontrol',
    'winnowtech/#mu-sous-chef',
    'winnowtech/#ifacestat',
    'winnowtech/#mubot2',
    'winnowtech/#munionagent',
    'winnowtech/#expeditor'  ]
    global dockerps
    dockerps = ''
    ps = 'CONTAINER ID'
    for word in lines:
        for word_single in word.replace(':',' ').split():
            if word_single in image_listing:
                count+=1
                image_listing.remove(word_single)
        for letter in word:
            #deviceid scraping
            if letter == ps[m] and m < len(ps)-1:
                m+=1
            if m==len(ps)-1 and flag==0:
                dockerps+=letter
    print(dockerps) #result)

    if len(dockerps.replace(" ", "")) > 885:
        print("This box likely has all the containers running\nCounted %s images" % (str(count)))
    else:
        print("Counted %s image(s)" % (str(count)))
        print("Please check if box has all images. \
        \n\nCheck for the following: \
        \n-is it provisioned\
        \n-is it in the database\
        \n-is it connected to the internet\
        \n-try restarting munionagent\
        ")

if __name__ == "__main__":
    main_exe()
    input("Press enter")
