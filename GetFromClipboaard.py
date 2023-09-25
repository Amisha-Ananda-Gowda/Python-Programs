import pyperclip
text=pyperclip.paste()
print(text)
lines=text.split('\n')
for i in range(len(lines)):
    lines[i]="* "+lines[i]
text='\n'.join(lines)
pyperclip.copy(text)
print("Modified text has been copied to the clipboard")
print(text)
