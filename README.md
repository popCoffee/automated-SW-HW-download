# automated-SW-HW-download
This repository contains the automated program used to build and ensure the download of software onto a linux-based and Nvidia chip for CV processing.

© 2018

### Notes
There are multiple steps to installing this program on Windows. 

### Requirements:
Windows laptop prepared for provisioning (see how to install the provisioning tools below)
A flashed and QA'd hardware box (from the Manufacturer)
2 x ethernet cables
1 x power cable
**Do NOT use a usb to ethernet adapter 

#### Steps:
Connect it all up Run the provisioning script Add the device to the DB Make sure it all works Record the results
#### Connect it all up
Before starting provisioning, the Vision device must be connected to the Winnow network (ideally with an Ethernet cable, not WiFi, for best download speeds), and powered up.
The laptop running the provisioning script must then be connected to the Vision device using the tablet Ethernet port.

#### Tech
- Ubuntu subsystem
- Docker
- Python
- Windows
- Excel-online
#### Configuring a laptop to run the provisioning script
In order to perform the provisioning, the laptop used must be prepared with specific software and configuration files for the devices as below.
1. Please install the necessary programs before provisioning
2. Please download the script used to run the automated provisioning on Windows (you will need permission as the owner is Team Winnow)
3. Please get .ovpn files placed in one of the correct client folders as seen by the image below. The automation.exe file does multiple checks before provisioning and will pull these .ovpn files from the pending folder in a specific client folder.
#### NOTE--
Every Vision device needs a unique .ovpn file to be able to connect to the Winnow VPN. When the provisioning script runs, a file is automatically taken from the local laptop file system and then marked as "used" so it won't accidentally be used on more than one device.
New .ovpn files can be requested from the V. development team ( , if he can't be reached  or person person
).person
#### Running the provisioning script
Once everything is connected, run the executable file automation.exe by double clicking on it;
 put a sticker or tape onto the box and write the last four character of the Device ID 
The automation.exe file will log the details of the new device  except for the box number. in a g-sheet automatically
You need to go to the g-sheet, look up the new row (with the new Device ID), and write the box number in the first column of the row.
NOTE! This logging of device info is really important, since we otherwise don't have any view of which boxes have been provisioned and what .ovpn file was used, etc.

#### Add the device to the Vis DB:
Before the Vision software can finish downloading, the new device must be added to the Vision DB. This is currently a manual step done by the Vision development team.
Inform the database keepers ( , if he can't be reached  or ) that a new device is being added Michael Berryman David Woosnam Mark Haynes and provide the Device ID along with the client name.

#### Make sure it all works

Download of the Vision software will take about 10 minutes. Once done, you will be able to see a number of services (containers) running on the device.
Log into the box and see if docker is still downloading stuff by running Current_containers_running.exe.
_____________

For docker stacks 21 (configuration for closed bins) 22 (configuration for open bins), if the download is completed, expect about 11 containers
running as per the list above (version numbers, dates, up time etc may change).
Between the box being provisioned and updating the database, it is possible the downloader may pause and not download all the images for the containers.
Troubleshoot with Troubleshoot_restart_munionagent.exe or by reseting the box. Then rerun Current_containers_running.exe after 1-2 minutes.
Record the Results:
