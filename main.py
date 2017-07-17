# -*- coding: utf-8 -*-

from font_3x5 import letters

chars = [
'💙',
'💛',
]

black = chars[0]
white = chars[1]

notblack = '#'
notwhite = '.'

def print_break(width=5, end='\n'):
    print(white*width, end=end)

def print_text(text, end='\n'):
    print_break(end=end)
    for char in text:
        image = letters[char]
        print_image(image, end=end)
        print_break(end=end)

def print_image(image, end='\n'):
    for line in image:
        line = ''.join(line)
        print(line.replace(notblack, black).replace(notwhite, white), end=end)

print('<meta charset="UTF-8">')
print_text('HELLO WORLD', end='<br>\n')
