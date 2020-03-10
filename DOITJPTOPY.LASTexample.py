"""
a = 'a:b:c:d'

b = '#'.join(a.split(':'))
print(b)
"""
"""
a = {'A' : 90, 'B' : 80}
print(a.get('C', 70))
"""
"""
주소값에 차이가 있다.
"""
"""
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
sum = 0
for i in A :
    if i > 50 :
        sum += i
print(sum)
"""
"""
def pib(num) :
    print(num)
    if num == 0 : return 0
    if num == 1 : return 1
    return pib(num-2) + pib(num-1)
n = input()
print(pib(int(n)))
"""
user_input = input("숫자를 입력하세요: ")
numbers = user_input.split(",")
total = 0
for n in numbers :
    total += int(n)
print(total)