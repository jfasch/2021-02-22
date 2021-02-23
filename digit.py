import sys

print('argv:', sys.argv)

digit = sys.argv[1]
print('digit:', digit, 'type:', type(digit))

if digit == '0':
    print('zero')
elif digit == '1':
    print('one')
elif digit == '2':
    print('two')
elif digit == '3':
    print('three')
elif digit == '4':
    print('four')
elif digit == '5':
    print('five')
elif digit == '6':
    print('six')
elif digit == '7':
    print('seven')
elif digit == '8':
    print('eight')
elif digit == '9':
    print('nine')
else:
    print('nix gueltiges!!!!')
