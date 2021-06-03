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
