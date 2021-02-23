import sys

if len(sys.argv) != 2:
    print('Du Depp: Programm will genau einen Parameter!')
    sys.exit()

digit = sys.argv[1]

if len(digit) != 1:
    print('Du Depp: Ziffern bestehen aus einem Character, hier haben wir', len(digit), 'Characters')
    sys.exit()

try:
    digit = int(digit)
except ValueError:
    print('Du Depp:', digit, 'ist keine Ziffer')
    sys.exit()

translation = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}

print(translation[digit])
