#!/bin/bash
# Print out everything setting
# set -x
loginToVisionBox() {
  # Take the ssh psswrd and pass it to the ssh command, ssh in quietly (no warnings) to port 22222 with user root to device and ($@) run every parameter to the function
  sshpass -p "***redacted***" ssh -q -p ##### root@192.168.90.1 "$@"
}

loginToVisionBox << !
  echo ""
  echo "Checking VPN files"
  cd /mnt/boot/openvpn/
  echo ""
  [ -f *.ovpn ] && echo 'VPN file found. Exit: 01whj3487 ' || echo 'VPN file does not exist'
  echo ""
  [ -f *.placeholder ] && echo 'Placeholder file found. Exit: 01pgo9087 ' || echo 'Placeholder file does not exist'
!
