import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    address = '+'.join(sys.argv[1:])    
else:
    address = pyperclip.paste()

link = ('https://www.google.com/maps/place/' + address)
webbrowser.open(link)
print(link)


