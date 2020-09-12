import smtplib
from requests import get

def getIPExterno():
   ip = get('https://api.ipify.org').text
   return(ip)

ip = getIPExterno()
 
# start talking to the SMTP server for Gmail
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.ehlo()
# now login as my gmail user
username='XXXXXXXXX' # change to the correct value
password='XXXXXXXXX' # change to the correct value
s.login(username,password)
# the email objects 
replyto='XXXXXXXXX@gmail.com' # where a reply to will go - change to the correct value
sendto=['XXXXXXXXX@gmail.com'] # list to send to - change to the correct value
sendtoShow='XXXXXXXXX@gmail.com' # what shows on the email as send to - change to the correct value
subject='SCRIPT - MY PUBLIC IP' # subject line
content="\nMy Current Public IP is: "+ip+"\n"# content 
# compose the email. probably should use the email python module
mailtext='From: '+replyto+'\nTo: '+sendtoShow+'\n'
mailtext=mailtext+'Subject:'+subject+'\n'+content
# send the email
s.sendmail(replyto, sendto, mailtext)
# we're done
rslt=s.quit()
# print the result
print('Sendmail result=' + str(rslt[1]))