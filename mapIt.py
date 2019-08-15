import webbrowser, sys
link = ('https://www.google.com/maps/place/' + 
'+'.join(sys.argv[1:]))
# numList
# '+'.join(numList[1:])
print(link)

webbrowser.open(link)