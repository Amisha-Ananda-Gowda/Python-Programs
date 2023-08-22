#Write a program that will get the text from the clipboard, add a star and space to the beginning of each line, and then paste this new text to the clipboard
import pyperclip

# Get the text from the clipboard
text = pyperclip.paste()

print(text)

# Add a star and space to the beginning of each line
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

# Join the modified lines and copy them to the clipboard
text = '\n'.join(lines)
pyperclip.copy(text)

print('Modified text has been copied to the clipboard')

print(text)