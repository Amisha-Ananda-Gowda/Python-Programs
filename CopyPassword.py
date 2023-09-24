#Write a program that takes the account name for instance email or blog from command line arguments and copies the acounts password to the clipboard so that the user can paste it into a password field
#works in vs code
import sys
import pyperclip
PASSWORDS={
    'email':'myemailpassword',
    'blog':'myblogpassword',
    'social':'mysocialpassword'
}

if len(sys.argv)<2:
  print('Usage:python password_manager.py[account]-copy accountpassword')
  sys.exit()
account =sys.argv[1]
if account in PASSWORDS:
  pyperclip.copy(PASSWORDS[account])
  print('Password for '+account+' copied to clipboard.')
else:
  print('There is no account named '+account)