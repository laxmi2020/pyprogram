import json
d={
    'course-name':'python',
    'free':15000

}

f=json.dumps(d)
print(type(f))
print(f)