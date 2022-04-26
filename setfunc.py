l=[10,20,30,40]
s=set(l)

print(s)

s.remove(20)
print(s)

s.discard(30)
print(s)

s.pop()
print(s)

s.clear()
print(s)

s.add(60)
print(s)

l=[10,80,90]
s={10,20,30,40,50}
s.update(l)
print(s)