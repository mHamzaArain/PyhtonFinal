import webbrowser, sys, pyperclip

sys.argv # ['mapit.py', '870', 'Valecia', 'St.']

# If command line agr passed
if len(sys.argv) > 1:       
    address = ' '.join(sys.argv[1:])      #  ['870', 'Valecia', 'St.']    -> 870 Valencia St.

# If address copy to clipboard
else:
    address = pyperclip.paste()

webbrowser.open(f'https://www.google.com/maps/placr