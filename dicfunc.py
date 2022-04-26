d={
    'course':'python',
    'fees':8000,
    'duration':'2months'

}

c=d.get('course')
#c1=d['course']
print(c)

for a in d.keys():
    print(a)

for a in d.values():
    print(a)

for a,b in d.items():
    print(a,b)

del d['fees']
print(d)

d.pop('duration')
print(d)

d=dict(name='python',fees=8000)
print(d)

d={
    'course':'python',
    'fees':8000,
    'duration':'2months'

}
d.update({'fees':100000})
print(d)


d.clear()
print(d)

d={
    'course':'python',
    'fees':8000,
    'duration':'2months'

}

d['desc']="This is python"
print(d)

d['fees']=100000
print(d)






