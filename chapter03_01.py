# Chapther03-1
# 시퀀스 형
# 컨테이너(Container) : 서로 다른 자료형 [list, tuple, collections.deque]
# Flat : 한 개의 자료형[str, bytes, bytearray, array.array, memoryview]
# 가변 : list, bytearray, array.array, memoryview, deque
# 불변 : tuple, str, bytes

# 지능형 리스트(Comprehending List)

# None Comprehending Lists
chars = '!@#$%^&*()_+'
code1 = []

for s in chars:
    code1.append(ord(s))

print('EX1-1 : ', code1)

# Comprehending List (데이터 양이 많을 때 처리속도 약간 우세)
code2 = [ord(s) for s in chars]

print('EX1-2 : ', code2)

code3 = [ord(s) for s in chars if ord(s) > 40]
print('EX1-3 : ', code3)

# Comprehending List, + Map, Filter
code4 = list(map(ord, chars))
code5 = list(filter(lambda x : x > 40, map(ord, chars)))
print('EX1-4 : ', code4)


print('EX1-5 : ', [chr(s) for s in code1])
print('EX1-6 : ', [chr(s) for s in code2])
print('EX1-7 : ', [chr(s) for s in code3])
print('EX1-8 : ', [chr(s) for s in code4])

print()
print()


# Generator

import array

# Generator : 한 번에 한 개의 항목을 생성(메모리 유지X)
tuple_g = (ord(s) for s in chars)
# Array
array_g = array.array('I', (ord(s) for s in chars))

print('EX2-1 : ', tuple_g)
print('EX2-2 : ', next(tuple_g))
print('EX2-3 : ', next(tuple_g))

print('EX2-4 : ', array_g)
print('EX2-4 : ', array_g.tolist())

print()
print()

# Generator 예제
print('EX3-1 : ', ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,11)))

for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,11)):
    print('EX3-2 : ', s)


print()
print()


# 리스트 주의 할 점
marks1 = [['~'] * 3 for n in range(3)]
marks2 = [['~'] * 3] * 3

print('EX4-1 : ', marks1)
print('EX4-2 : ', marks2)

print()

marks1[0][1] = 'X'
marks2[0][1] = 'X'

print('EX4-3 : ', marks1)
print('EX4-4 : ', marks2)

# 증명
print('EX4-5 :', [id(i) for i in marks1])
print('EX4-6 :', [id(i) for i in marks2])


# Tuple Advenced

# Packing & Unpacking

print('EX5-1 :', divmod(100, 9))
print('EX5-2 :', divmod(*(100, 9)))
print('EX5-3 :', *(divmod(100, 9)))

print()

x, y, *rest = range(10)
print('EX5-4 :', x, y, *rest)

x, y, *rest = range(2)
print('EX5-5 :', x, y, *rest)

x, y, *rest = 1,2,3,4,5
print('EX5-6 :', x, y, *rest)

# def test(*args, **args)

print()
print()


# Mutable(가변) vs Immutable(불변)

m = [10, 15, 20] # 리스트
l = (10, 15, 20) # 튜플

print('EX6-1 :', m, l, id(m), id(l))

l = l * 2
m = m * 2

print('EX6-2 :', m, l, id(m), id(l))

# 튜플 > 값을 변경 할 수 없음, 재할당 지원 X
# l[0] = 3

# 리스트 재할당 가능
# m[0] = 10

l *= 2
m *= 2

print('EX6-3 :', m, l, id(m), id(l))


print()
print()

# sort vs sorted
# reverse, key = len, key = str.lower, key = func

f_list = ['oragne', 'apple', 'mango', 'papaya', 'lemon', 'strawberry', 'coconut']

# sorted : 정렬 후 '새로운' 객제 반환

print('EX7-1 :', sorted(f_list)) # 순서
print('EX7-2 :', sorted(f_list, reverse=True)) # 순서반대
print('EX7-3 :', sorted(f_list, key=len)) # 문자의 길이 순서별로
print('EX7-4 :', sorted(f_list, key=lambda x:x[-1])) # 단어 끝글자 순서대로
print('EX7-5 :', sorted(f_list, key=lambda x:x[-1], reverse=True)) 

print('EX7-6 :', f_list) # 원본 변경되지 않음

print()

# sort : 정렬 후 객제 직접 변경
# 반환 값 확인 None

a = f_list.sort()

print('EX7-7 :', f_list.sort(), f_list)
print('EX7-8 :', f_list.sort(reverse=True), f_list)
print('EX7-9 :', f_list.sort(key=len), f_list)
print('EX7-10 :', f_list.sort(key=lambda x:x[-1]), f_list)
print('EX7-11 :', f_list.sort(key=lambda x:x[-1], reverse=True), f_list)