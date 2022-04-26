course={
    'php':{'duration':'3months','fees':15000},
    'java':{'duration':'2months','fees':10000},
    'python':{'duration':'2months','fees':12000},
}

print(course)

print(course['php'])
course['java']['fees']=3000
print(course['php']['fees'])

for k,v in course.items():
    #print(k, v)
    print(k,v['duration'],v['fees'])
