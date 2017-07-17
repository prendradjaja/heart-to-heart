import numpy

letters = {}

letters['A'] = """
 #
# #
###
# #
# #
"""

letters['B'] = """
##
# #
##
# #
##
"""

letters['C'] = """
 ##
#
#
#
 ##
"""

letters['D'] = """
##
# #
# #
# #
##
"""

letters['E'] = """
###
#
##
#
###
"""

letters['F'] = """
###
#
##
#
#
"""

letters['G'] = """
 ##
#
# #
# #
 ##
"""

letters['H'] = """
# #
# #
###
# #
# #
"""

letters['I'] = """
###
 #
 #
 #
###
"""

letters['J'] = """
 ##
  #
  #
# #
 #
"""

letters['K'] = """
# #
# #
##
# #
# #
"""

letters['L'] = """
#
#
#
#
###
"""

letters['M'] = """
# #
###
###
# #
# #
"""

letters['N'] = """
###
# #
# #
# #
# #
"""

letters['O'] = """
 #
# #
# #
# #
 #
"""

letters['P'] = """
##
# #
##
#
#
"""

letters['Q'] = """
 #
# #
# #
 ##
  #
"""

letters['R'] = """
##
# #
##
# #
# #
"""

letters['S'] = """
 ##
#
 #
  #
##
"""

letters['T'] = """
###
 #
 #
 #
 #
"""

letters['U'] = """
# #
# #
# #
# #
###
"""

letters['V'] = """
# #
# #
# #
# #
 #
"""

letters['W'] = """
# #
# #
###
###
# #
"""

letters['X'] = """
# #
# #
 #
# #
# #
"""

letters['Y'] = """
# #
# #
 #
 #
 #
"""

letters['Z'] = """
###
  #
 #
#
###
"""

letters[' '] = """





"""

CHAR_WIDTH = 3

def fix(letter):
    lines = letter.split('\n')[1:6]
    lines = [line.ljust(CHAR_WIDTH) for line in lines]
    lines = [line.replace(' ', '.') for line in lines]
    lines = [list(line) for line in lines]
    return numpy.rot90(lines, k=3)

for each in letters:
    letters[each] = fix(letters[each])
