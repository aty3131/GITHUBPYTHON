"""print("=" * 50)
print("My Program")
print("=" * 50)
"""
"""
print("I eat %s apples" % "five")
"""
"""
print("Error is %d%%." % 97)
"""
"""
print("%-10sjane" % "hi")
"""
"""
number = 10
day = "three"
print("I ate {0} apples. so I was sick for {1} days.".format(number,day))
"""
"""
print("I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3))
"""
"""
print("I ate {0} apples. so I was sick for {day} days.".format(10, day=3))
"""
"""
print("{0:<10}".format("hi"))
print("{0:>10}".format("hi"))
print("{0:^10}".format("hi"))
"""
"""
print("{0:=^10}".format("hi"))
print("{0:!<10}".format("hi"))
print("{0:!>10}".format("hi"))
"""
"""
y = 3.42134234
print("{0:0.4f}".format(y))
print("{0:10.4f}".format(y))
"""
"""
name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')
print(f'나는 내년이면 {age+1}살이 된다.')
d = {'name':'홍길동', 'age':30}
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')
print(f'{"hi":<10}')
print(f'{"hi":^10}')
print(f'{"hi":>10}')
y = 3.42134234
print(f'{y:0.4f}')
print(f'{y:10.4f}')
print(f'{{and}}')
print(f'{"python":!^12}')
print("{0:!^12}".format("python"))
"""
"""
a = "hobby"
print(a.count('b'))
a = "Python is the best choice"
print(a.find('b'))
print(a.find('k'))
print(",".join(a))
a = " hi "
print(a.lstrip())
print(a.rstrip())
print(a.strip())
"""
"""
a = "Life is too short"
print(a.replace("Life", "Your leg"))
print(a.split())
b = "a:b:c:d"
print(b.split(":"))
"""
"""
a = [1, 2, 3]
print(a[0])
b = 'life'
print(b[-1])
"""
"""
a = [1, 2, 3, ['a', 'b', 'c']]
print(a[-1])
print(a[-1][0])

a = [1, 2, 3, 4, 5]
print(a[0:2])
a = "12345"
print(a[0:2])
a = [1, 2, 3, 4, 5]
b = a[:2]
c = a[2:]
print(b, c)

a = [1, 2, 3]
b = [4, 5, 6]
print( a+b )
"""
"""
a = {1: 'a'}
a[2] = 'b'
print(a)
a['name'] = 'pey'
print(a)
a[3] = [1,2,3]
print(a)
del a[1]
print(a)
"""
"""
a = {'name' : 'pey', 'phone' : '0119993323', 'birth' : '1118'}
print(a.keys())
for k in a.keys() :
    print(k)
print(list(a.keys()))
print(a.values())
print(a.items())
a.clear()
print(a)
a = {'name' : 'pey', 'phone' : '0119993323', 'birth' : '1118'}
print(a.get('name'))
print(a.get('foo', 'bar'))
b = {'name' : '홍길동', 'birth' : 1128 , 'age' : 30}
print(b)
"""
"""
s1 = set([1,2,3])
print(s1)
s2 = set("Hello")
print(s2)
"""
"""
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1 & s2)
print(s1 | s2)
print(s1 - s2)
print(s2 - s1)

s1 = set([1, 2, 3])
s1.add(4)
print(s1)
s1 = set([1, 2, 3])
s1.update([4, 5, 6])
print(s1)
s1.remove(2)
print(s1)
"""
"""
print(bool('python'))
[a, b] = ['python', 'life']
print(a)
print(b)
print(type(a), type(b))

grade = { '국어' : 80 , '영어' : 75 , '수학' : 55}
print((grade['국어'] + grade['영어'] + grade['수학'])/3)
pin = "881120-1068234"
yyyymmdd = "19"+pin[0:6]
num = pin[7:]
print(yyyymmdd)
print(num)
"""
"""
a = "a:b:c:d"
b = a.replace(":" , "#")
print(b)
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)

a = ['Life', 'is', 'too', 'short']
result = ' '.join(a)
print(result)

a = (1 ,2, 3)
a = a + (4,)
print(a)
"""
"""
a = { 'A' : 90, 'B' : 80, 'C':70}
result = a.pop('B')
print(a)
print(result)
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)
b = list(aSet)
print(b)
"""
"""
sum = 0
for i in range (1, 101) :
    sum = sum + i
print(sum)
"""
"""
result = 0
i = 1
while i <= 1000 :
    if i % 3 ==0 :
        result +=i
    i += 1
print(result)
"""
"""
A = [70, 60, 55 ,75, 95, 90, 80, 80, 85, 100]
total = 0
for score in A :
    total += score
average = total / 10
print(average)
"""
"""
f = open("C:/doit/복습.txt",'w')
f.close()
"""
"""
f = open("C:/doit/새파일.txt",'w')
for i in range(1, 11) :
    data = "%d번째 줄입니다.\n" %i
    f.write(data)
f.close()
"""
"""
f = open("C:/doit/새파일.txt", 'r')
line = f.readline()
print(line)
f.close()
"""
"""
f = open("C:/doit/새파일.txt",'r')
while True :
    line = f.readline()
    if not line: break
    print(line)
f.close()
"""
"""
f = open("C:/doit/새파일.txt",'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()
"""
"""
f = open("C:/doit/새파일.txt",'r')
data = f.read()
print(data)
f.close()
"""
"""
f = open("C:/doit/새파일.txt",'a')
for i in range(11, 20) :
    data = "%d 번째 줄입니다.\n" % i
    f.write(data)
f.close()
"""
"""
f = open("foo.txt", 'w')
f.write("Life is too short, you need python")
f.close()
"""
"""
with open("foo.txt", "w") as f :
    f.write("Life is too short, you need python")
"""
"""
def avg_numbers(*args) :
    result=0
    for i in args:
        result += i
    return result/len(args)
print(avg_numbers(1, 2))
print(avg_numbers(1,2,3,4,5))
"""
"""
print("you" "need" "python")
print("you"+"need"+"python")
print("you","need","python")
print("".join(["you","need","python"]))
"""
"""
f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt",'r')
print(f2.read())
"""