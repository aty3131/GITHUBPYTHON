import re
"""
p = re.compile('[a-z]+')
m = p.match("python")
print(m)
m = p.match("3 python")
print(m)
m = p.search("python")
print(m)
m = p.search("3 python")
print(m)
result = p.findall("life is too short")
print(result)
result = p.finditer("life is too short")
print(result)
for r in result: print(r)
"""
"""
p = re.compile('[a-z]+')
m = p.match("python")
print(m.group())
print(m.start())
print(m.end())
print(m.span())
"""
p = re.compile('a.b', re.DOTALL)
m = p.match('a\nb')
print(m)