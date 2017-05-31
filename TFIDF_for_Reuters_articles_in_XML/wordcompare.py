import sys

def todict(s):
    d = {}
    lines = s.strip().split('\n')
    for line in lines:
        pair = line.split(" ")
        value = pair[1]
        if value[0]=='.':
            value = '0'+value
        d[pair[0]] = value
    return d

f1 = sys.argv[1]
f2 = sys.argv[2]

s1 = open(f1).read()
s2 = open(f2).read()

d1 = todict(s1)
d2 = todict(s2)

if d1 != d2:
    print "%s %s differ" % (f1,f2)
    print d1
    print d2