import module
print(module.sum(10,20))

import module as m
print(m.sum(10,20))

import module
print(module.mul(10,20))


from module import sum

print(sum(10,20))

from module import *

print(mul(10,20))