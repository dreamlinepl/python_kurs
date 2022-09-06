# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 11:12:54 2022

@author: Marcin
"""

from collections import Counter
#%%
target = ['yes', 'no', 'no', None, 'yes', 'yes', 'no', 'yes']
print (Counter(target))
#%%

poll_1 = {'yes': 140, 'no': 120, None: 12}
poll_2 = {'yes': 113, 'no': 132, None: 9}

cnt = Counter (poll_1)
cnt2 = Counter (poll_2)
print (cnt+ cnt2)

#%%

poll_1 = {'yes': 140, 'no': 120, None: 12}
poll_2 = {'yes': 113, 'no': 132, None: 9}
poll_3 = {'yes': 16, 'no': 14}

cnt  = Counter (poll_1)
cnt  += Counter (poll_2)
cnt  += Counter (poll_3)

print (cnt["yes"])

#%%

text = 'python programming - introduction'
cnt = (Counter(text))

print (cnt.most_common(3))

#%%

from collections import Counter
import re
# =============================================================================
# Wykorzystując moduł wbudowany re dokonaj podziału podanego tekstu na wyrazy/tokeny. 
# Dokonaj standaryzacji wyrazów (wszystkie małe litery). 
# Następnie zbuduj obiekt Counter pozwalający wyznaczyć trzy najczęściej pojawiające się wyrazy w tekście. 
# W odpowiedzi wydrukuj te wyrazy wraz z liczbą wystąpień.
# =============================================================================


text = """"Python is fast enough for our site and allows us to produce maintainable features in record times,
with a minimum of developers," said Cuong Do, Software Architect, YouTube.com.

"Python plays a key role in our production pipeline. Without it a project the size of Star Wars:
Episode II would have been very difficult to pull off. From crowd rendering to batch processing to compositing,
Python binds all things together," said Tommy Burnette, Senior Technical Director, Industrial Light & Magic."""

text = text.lower()
print (text)
pattern =r'\w+'
cnt = Counter (re.findall(pattern, text))
print (cnt.most_common(3))

#%%
from collections import Counter
import re


fnames = [
    '001_image.png', '002_image.png', '003_image.jpg', '004_image.png',
    '005_image.png', '006_image.png', '007_image.jpg', '008_image.png', 
    '009_image.jpg', '010_image.jpg', '011_image.jpg', '012_image.png', 
    '013_image.jpg', '014_image.jpg', '015_image.jpg', '016_image.png', 
    '017_image.jpg', '018_image.jpg', '019_image.png', '020_image.png', 
    '021_image.jpg', '022_image.jpg', '023_image.png', '024_image.png', 
    '025_image.jpg', '026_image.png', '027_image.png', '028_image.jpg', 
    '029_image.png', '030_image.png'
    ]

extensions = [re.findall(r'.\w+',fname)[1] for fname in fnames]

print (Counter (extensions))

#%%
from collections import ChainMap


stocks_1 = {'CDR': 400, 'PLW': 490}
stocks_2 = {'PLW': 500, 'TEN': 550, 'BBT': 30}

stocks = ChainMap(stocks_1, stocks_2)
print(stocks)
print(stocks['PLW'])
#%%

techs = {'Apple': 370, 'Samsung': 1100, 'Microsoft':201}
finance = {'Citigroup': 51, 'Allianz': 180}
gaming = {'Sony': 76, 'Nintendo': 470, 'EA': 135}

stocks = ChainMap(techs, finance, gaming)
print (stocks)
stocks['Microsoft'] = 210
print (stocks)
print (techs)

#%%

from collections import ChainMap


techs = {'Apple': 370, 'Samsung': 1100, 'Microsoft': 201}
finance = {'Citigroup': 51, 'Allianz': 180}
gaming = {'Sony': 76, 'Nintendo': 470, 'EA': 135}

stocks = ChainMap(techs, finance, gaming)

keys = stocks.keys()
print (sorted(keys))


#%%
from collections import ChainMap


default_settings = {'mode': 'eco', 'power_level': 7}
user_settings = {'mode': 'sport', 'power_level': 10}

settings = ChainMap(user_settings, default_settings)
print(settings['mode'])

default_settings = {'mode': 'eco', 'power_level': 7}
user_settings = {}

settings = ChainMap(user_settings, default_settings)
print(settings['mode'])

#%%

from collections import namedtuple

class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

point1 = Point(3, 4)
point2 = Point(-2,6)
print (point1.x)



Point = namedtuple(typename='Point', field_names=['x', 'y'])

pt1 = Point(3, 4)
pt2 = Point(-2, 6)

print(pt1)
print(pt2)
#%%

from collections import namedtuple


Point = namedtuple(typename='Point', field_names=['x', 'y'])

pt1 = Point(3, 4)
pt2 = Point(-2, 6)
pt3 = Point((pt2.x+pt1.x)/2,(pt2.y+pt1.y)/2)

print (pt3.y)

#%%


from collections import namedtuple


Student = namedtuple(typename='Student', field_names=['name', 'age', 'specialization'])

students = [
    Student('Mike', 21, 'physics'),
    Student('Kate', 20, 'mathematics'),
    Student('Bob', 21, 'information technology')
    ]

for student in students:
    print(f'{student.name:5}: {student.age}: {student.specialization}')
    
#%%


from collections import namedtuple


Student = namedtuple(typename='Student', field_names=['name', 'age', 'specialization'])

students = [
    Student('Mike', 21, 'physics'),
    Student('Mark', 22, 'biology'),
    Student('Kate', 20, 'mathematics'),
    Student('Bob', 21, 'information technology')
    ]

students.sort(key=lambda student: student.age)
print (students)



#%%

from collections import namedtuple


Student = namedtuple(typename='Student', field_names=['name', 'age', 'specialization'])

st1 = {'name': 'Kate', 'age': 20, 'specialization': 'mathematics'}
st2 = {'name': 'Mike', 'age': 21, 'specialization': 'physics'}
st3 = {'name': 'Bob', 'age': 21, 'specialization': 'information technology'}

students = [st1, st2, st3]
students_tuple =[Student(student['name'], student['age'], student['specialization']) for student in students]

students_tuple2 = [Student(**st1), Student(**st2), Student(**st3)]
                          
for student in students_tuple:
     print(student)
     
for student in students_tuple2:
     print(student)
     
#%%
from collections import namedtuple
import re
students = []
lines = []
st = {}
Student = namedtuple(typename='Student', field_names=['name', 'age', 'specialization'])
with open ('students.txt', 'r') as file:
    lines = file.readlines()
pattern1= r"\w+"
new = []
for line in lines:
    new.append(re.findall(pattern1, line))
    

print (students)


# students_tuple =[Student(student['name'], student['age'], student['specialization']) for student in students]

#%%

from collections import namedtuple


Student = namedtuple(typename='Student', field_names=['name', 'age', 'specialization'])

students = []
with open('students.txt', 'r') as file:
    lines = [eval(line.strip()) for line in file.readlines()]
    
print (lines[0])

Student (**lines[0])

#%%
# quotations = {}
# print(quotations.get('source', 'NYSE'))
# print(quotations)
# print (quotations.setdefault('source','NYSE'))
quotations = {}
quotations.setdefault('source', 'NYSE')
print(quotations)
quotations.setdefault('source', 'LSE')
print(quotations)
print(quotations['source'])

#%%

data = [
    ('technology', 'Apple'),
    ('gaming', 'Techland'),
    ('finance', 'Berkshire Hathaway'),
    ('gaming', 'EA'),
    ('technology', 'Facebook'),
    ('gaming', 'CD Projekt'),
    ('finance', 'Allianz')
    ]


data_dict = {}
for sector, company in data:
    data_dict.setdefault(sector, []).append(company)
    
print (data_dict)

#%%
from collections import defaultdict

data = [
    ('technology', 'Apple'),
    ('gaming', 'Techland'),
    ('finance', 'Berkshire Hathaway'),
    ('gaming', 'EA'),
    ('technology', 'Facebook'),
    ('gaming', 'CD Projekt'),
    ('finance', 'Allianz')
    ]

def_dict = defaultdict(list)
for sector, company in data:
    def_dict[sector].append(company)
    
print (def_dict)

#%%

from collections import defaultdict

data = [
    ('technology', 'Facebook'),        
    ('technology', 'Apple'),
    ('gaming', 'Techland'),
    ('finance', 'Berkshire Hathaway'),
    ('gaming', 'EA'),
    ('gaming', 'EA'),    
    ('technology', 'Facebook'),
    ('gaming', 'CD Projekt'),
    ('finance', 'Allianz')
    ]

# def_dict = defaultdict(list)
# for sector, company in data:
#     if not company in def_dict[sector]:
#         def_dict[sector].append(company)
        
# print (def_dict)


def_dict = defaultdict(set)
for sector, company in data:
    def_dict[sector].add(company)

print (def_dict)
#%%
from collections import defaultdict

transactions = [
    ('001', 100),
    ('003', 10),
    ('002', 80),
    ('001', 90),
    ('002', 46),
    ('001', 43),
    ('003', 23),
]

def_dict = defaultdict(int)

for user_id, amount in transactions:
    def_dict[user_id]+= amount

print (def_dict)

#%%
from collections import deque
      
daynames = deque (['Tue.', 'Wed.', 'Thu.', 'Fri.', 'Sat.'])

daynames.append('Sun.')
daynames.appendleft('Mon.')
print (daynames)

#%%
from collections import deque
daynames = deque(['Mon.', 'Tue.', 'Wed.', 'Thu.', 'Fri.', 'Sat.', 'Sun.'])

daynames.rotate(1)

print (daynames)

#%%
from collections import deque
daynames = deque(['Mon.', 'Tue.', 'Wed.', 'Thu.', 'Fri.', 'Sat.', 'Sun.'])

daynames.rotate(-3)
print (daynames)
print(daynames.pop())

#%%
from collections import deque
wishlist = deque()

def add_user(user_id):
    if user_id == 'None':
        wishlist.clear()
    else:
        wishlist.append(user_id)
    print (wishlist)

add_user('003' )
add_user('001' )
add_user('004' )
add_user('None' )
add_user('002' )
add_user('005')

#%%

from collections import deque
wishlist = deque([],maxlen=3)

def add_user(user_id):
    wishlist.append(user_id)
    print (wishlist)

user_ids = ['003','001','004','006','002','005']
for user in user_ids:
    add_user(user)

#%%

from collections import deque
wishlist = deque([])

def add_user(user_id):
    wishlist.append(user_id)
    print (wishlist)

user_ids = ['003','001','004','002','005']
for user in user_ids:
    add_user(user) 
add_users=['007', '009', '010']

wishlist.extend(add_users)
print (wishlist)
#%%



