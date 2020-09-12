# Script to show your public ip
# Author: Samuel Martins <samuel@samuelmartins.com.br>
# MIT License

from requests import get

ip = get('https://api.ipify.org').text
print ('My public IP address is: '+ ip)
