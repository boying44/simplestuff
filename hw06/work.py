print [x for x in range(8)]
print [x*x for x in range(8)]
print [(x, x*x, x*x*x) for x in range(8)]

p = "password1234"

print [x for x in p]
print [x for x in "1234"]

UC_LETTERS="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print [ x for x in p if x in UC_LETTERS ]
print [ 1 for x in p if x in UC_LETTERS ]
print [ 1 if x in UC_LETTERS else 0 for x in p ]

LC_LETTERS="abcdefghijklmnopqrstuvwxyz"
NUMBERS="1234567890"

def validate(pword):
    u = [1 if x in UC_LETTERS else 0 for x in pword]
    l = [1 if x in LC_LETTERS else 0 for x in pword]
    n = [1 if x in NUMBERS else 0 for x in pword]
    return (1 in u)&(1 in l)&(1 in n) 
    
print validate("Password1234")

chars = ".?!&#,;:-_*"

def strength(pword):
    u = [1 if x in UC_LETTERS else 0 for x in pword]
    l = [1 if x in LC_LETTERS else 0 for x in pword]
    n = [1 if x in NUMBERS else 0 for x in pword]

    
print strength("Password1234")
