#!/usr/bin/env python
# coding: utf-8

# In[30]:


n = 0
while n < 5:
    print(n)
    n= n+ 1


# In[24]:


n = 0
while n < 5:
    print(n)
    n +=1
else:
    print(n, "is not less than 5")


# In[43]:


fruits = ['banana', 'kiwi', 'strawberry', 'apple']
for f in fruits:
    if f == 'apple':
        print(f, 'is really a fruit?')
        break
    print("i like", f)


# In[37]:


num = 30
sum = 0

while num > 0:
    sum +=num
    num -= 1
print('the sum is', sum)


# In[38]:


grade = 55
if grade >=90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")


# In[64]:


marks = {'Andy':88, 'Amy':66, 'James': 90, 'Jules': 55,'Arthur': 77}
for student in marks:
    print(student, "received a", marks[student])


# In[65]:


max_marks = max(marks.values())
print(max_marks)
min_marks = min(marks.values())
print(min_marks)


# In[66]:


total_marks = 0
for value in marks.values():
    total_marks += value
    
average = total_marks/len(marks)

print(average)


# In[68]:


for student in {'Andy':88, 'Amy':66, 'James': 90, 'Jules': 55, 'Arthur': 77}:
    if 'J' in student:
        break
    print(student)


# In[69]:


for student in {'Andy':88, 'Amy':66, 'James': 90, 'Jules': 55, 'Arthur': 77}:
    if 'J' in student:
        continue
    print(student)

