# 1. Переменные
a = 14
print(a)
_____
14  
     
b = 'Text'
print(b) 
________
Text 
     
# 2. Действие с переменными
a = 14
c = 3
d = a + c
print(d)
__________
17   
    
print(a +c)
17
a = 18
print(a)
_________
18  
    
e = a
print(e)
________
18          
  
# 3. Типы данных
# Integer
print(type(a))
<class 'int'>
    
# float
a = 1.0
print(type(a))
<class 'float'>
     
# boolean
a = True
print(type(a))
<class 'bool'>
      
# string
a = '7'
print(type(a))
<class 'str'>
     
x = 15
y = 4
z=x+y
print(z)
print(type(z))
19
<class 'int'>
           
x='12'
y='4'
z=x+y
print(z)
print(type(z))
124
<class 'str'>
        
# 4. Списки
a = [1,2,3]
print(type(a))
<class 'list'>
     
b = ['Text', 4, True, 3.14]
print(b)
['Text', 4, True, 3.14]
    
# Нарезка списков
print(a[0])
print(a[1])
1
2
      
# добавление элемента в список
a.append(4)
print(a)
[1, 2, 3, 4]
# Замена элемента списка
a[3] = 5
print(a)
[1, 2, 3, 5]
# все элементы
a[:]
[1, 2, 3, 5]
     
a[2:]
[3, 5]
a[1:3]
[2, 3]
a[:-1]
[1, 2, 3]
a[-1]
5
     
# 5. Словари
country_info = {'name':'Japan', 'capital':'Tokio'}
print(country_info)
{'name': 'Japan', 'capital': 'Tokio'}
print(country_info['name'])
Japan
print(country_info['capital'])
Tokio
country_info['populaion'] = '126.0M'
print(country_info)
{'name': 'Japan', 'capital': 'Tokio', 'populaion': '126.0M'}
country_info['populaion'] = '100M'
print(country_info)
{'name': 'Japan', 'capital': 'Tokio', 'populaion': '100M'}
country_info['regions'] = ['Hokkaido', 'Tohoku', 'Kanto']
print(country_info)
{'name': 'Japan', 'capital': 'Tokio', 'populaion': '100M', 'regions': ['Hokkaido', 'Tohoku', 'Kanto']}
          
# словари полезны для ручного создания таблиц
import pandas as pd
pd.DataFrame({'Name':['t1', 't2', 't3'], 'Price':[100,200,500]})
______________
Name Price
0 t1 100
1 t2 200
2 t3 500
       
# 6. Операторы if, then, else
x = 19
if x < 10:
print('меньше 10')
else:
print('Больше или равно 10')
_____
Больше или равно 10   
     
a = ['t1', 18, 't2', 99.9]
numeric_lst = []
for i in a:
if type(i) != str:
numeric_lst.append(i)
print(numeric_lst)
[18, 99.9]   
    
# 7. Циклы
print(list(range(5)))
[0, 1, 2, 3, 4]
for i in range(5):
print(i)
0
1
2
3
4
    
items = ['a','b', 'c', 'd']
for item in items:
print(item)
a
b
c
d
    
x = 0
lst= []
items = ['a','b', 'c', 'd']
for item in items:
     x += 1
     print(x, item)
     lst.append(x)
print(lst)
1 a
2 b
3 c
4 d
[1, 2, 3, 4]
     
x=0
while x<5:
x +=1
print(x)
1
2
3
4
5
    
# 8. Функции
def areaCircle(radius):
area = 3.14 * (radius ** 2)
return area
areaCircle(2)
12.56
     
def volumeCylinder(radius, height = 3):
return 3.14 * radius**2 * height
volumeCylinder(2)
37.68
volumeCylinder(10,5)
1570.0
     
