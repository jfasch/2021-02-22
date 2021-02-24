import my_toolbox
import sys

if len(sys.argv) != 3:
    print('Gib bitte zwei Zahlen als Commandlineparameter an')
    sys.exit()

lhs = sys.argv[1]
rhs = sys.argv[2]

lhs = int(lhs)
rhs = int(rhs)

max = my_toolbox.maximum(lhs, rhs)
print('Das Maximum ist:', max)
