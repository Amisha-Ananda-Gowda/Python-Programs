import sys
import pyperclip
PASSWORDS={'email':'myemailpassword','blog':'myblogpassword','social':'mysocialmediapassword'}
if len(sys.argv)<2:
  print('Usage:python password_manager.py[account]-copy account password')
  sys.exit()
account=sys.argv[1]
if account in PASSWORDS:
  pyperclip.copy(PASSWORDS[account])
  print('Password for'+account+'copied to clipboard.')
else:
  print('There is no account named'+account)
  