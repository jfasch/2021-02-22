lhs = input('lhs bitte ->')
rhs = input('rhs bitte ->')

lhs = int(lhs)
rhs = int(rhs)

if lhs < rhs:
    print(rhs)
elif rhs < lhs:
    print(lhs)
else:
    print('same')
