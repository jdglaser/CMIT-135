# Week 5

## Overview

In week 5, we will be exploring simple data structures in Python, specifically lists. Lists are a structure for holding a series of variables and you will find them to be incredibly useful as we build more complicated programs. 

We will also begin to look at how computers are able to manipulate binary and how memory storage works inside of a computer.

## Objectives

+ Explain how logic gates are used to add binary numbers
+ Understand the difference between Kilobytes, Megabytes, and Mebibytes
+ Explain the different types of memory used in the computer and the reason for each type
+ Use Python lists in programs and understand their use
+ Be familiar with Strings and Tuples

## Activities and Assignments

+ Week 5: Discussion - Memory and Mebibytes
+ Week 5: Assignment - Programming with Lists
+ Week 5: Self-Paced Assignment

## Lesson

### Storage and Memory

+ The __Central Processing Unit (CPU)__ has "registers" that allow it to store the limited amount of data that the CPU is actively working with
+ This data could be intructions or data to be manipulated
+ Because the size of these registers is so limited, other kinds of memory are needed

<iframe width="560" height="315" src="https://www.youtube.com/embed/p3q5zWCw8J4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

__Question__: Which of the following is the fastest?

A. DRAM

B. Hard Drive

C. SRAM

D. SSD

E. CD-ROM

__Answer__: __C__ - SRAM

__Question__: An unopened photo is kept in the ___ of a computer?

A. CPU's cache

B. Hard Drive

C. RAM

D. None of the above

__Answer__: __B.__ - Hard Drive

<iframe width="560" height="315" src="https://www.youtube.com/embed/C_NbeOaUtog" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

__Question__: Which of the following is an example of volatile memory?

A. Hard Drive

B. DRAM

C. SSD

D. CD-ROM

__Answer__: CD-ROM

### Megabytes and Mebibytes

+ Recall that 1 byte = 8 bits

#### Word

+ Older computers originally were designed to do operations 8 bits at a time
+ Modern processors are typically 32-bit or 64-bit
+ The term **"Word"** refers to the chunks of the bits the processor is designed to operate on
    + So usually a "Word" is either 32 or 64 bits in size but it depends on the architecture of the specific machine

#### Kilobyte

+ A **Kilobyte** is approximately 1000 bytes
+ It is aproximately because on most computer hardware, a Kilobyte is 1024 bytes ($2^10=1-24$)

#### Megabyte

+ A **Megabyte** is approximately 1000 Kilobytes
+ Actually about 1024 kilobytes
+ So 1 megabyte is 1,048,576 bytes since 1024 x 1024 = 1048576

#### Gigabyte

+ A **Gigabyte** is approximately 1024 Megabytes

#### Terabyte

+ A **Terabyte** is approximately 1024 Gigabytes

#### Petabyte

+ A **Petabyte** is approximately 1024 Terabytes

### Why approximately? And what is a Kibibyte

+ The term __kilo__ in any context outside of computer science means 1000 not 1024
+ The IEEE proposed that we use new terms that were more precise:
    + __kilobyte (kB)__ -> __kibibyte (KiB)__
    + **megabyte (MB)** -> **mebibyte (MiB)**
    + **gigabyte (GB)** -> **gibibyte (GiB)**
    + **terrabyte (TB)** -> **tebibyte (TiB)**
+ These terms always refer to the base 2 value
+ However, rarely used in practice

### How Binary and Logic Gates Work in a Computer

<iframe width="560" height="315" src="https://www.youtube.com/embed/VBDoT8o4q00" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<br>

__How transistors work:__

<iframe width="560" height="315" src="https://www.youtube.com/embed/WhNyURBiJcU" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### The List Data Type

+ A __list__ is a value that contains multiple values in an ordered sequence
+ Values inside the list are called __items__

```python
>>> [1, 2, 3]
[1, 2, 3]
>>> ['cat', 'bat', 'rat', 'elephant']
['cat', 'bat', 'rat', 'elephant']
>>> ['hello', 3.1415, True, None, 42]
['hello', 3.1415, True, None, 42]
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam
['cat', 'bat', 'rat', 'elephant']
```

### Getting Individual Values in a List with Indexes

<img src="list_selecting.PNG" height="50%" width="50%">

```python
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam[0]
'cat'
>>> spam[1]
'bat'
>>> spam[2]
'rat'
>>> spam[3]
'elephant'
>>> ['cat', 'bat', 'rat', 'elephant'][3]
'elephant'
>>> 'Hello ' + spam[0]
'Hello cat'
>>> 'The ' + spam[1] + ' ate the ' + spam[0] + '.'
'The bat ate the cat.'
```

+ Python will give an index error if you use an index that exceeds the number of values in your list

```python
spam = ['cat', 'bat', 'rat', 'elephant']
spam[10000]
```

```
Traceback (most recent call last):
File "<pyshell#9>", line 1, in <module>
spam[10000]
IndexError: list index out of range
```

+ Lists can also contain other list values

```python
>>>spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
>>> spam[0]
['cat', 'bat']
>>> spam[0][1]
'bat'
>>> spam[1][4]
50
```

+ You can also use negative indexes to select items from the end of the list

```python
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam[-1]
'elephant'
>>> spam[-3]
'bat'
>>> 'The ' + spam[-1] + ' is afraid of the ' + spam[-3] + '.'
'The elephant is afraid of the bat.'
```

### Getting Sublists with Slices

+ Just as an index can get a single value from a list, a __slice__ can get several values from a list, in the form of a new list

+ A slice goes up to, but will not include, the value at the seocnd index

```python
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam[0:4]
['cat', 'bat', 'rat', 'elephant']
>>> spam[1:3]
['bat', 'rat']
>>> spam[0:-1]
['cat', 'bat', 'rat']
```

+ You can leave out one or both of the indexes on either side of the colon in the slice
+ Leaving out the first index is the same as using `0`
+ Leaving out the last index is the same as using the length of the list

```python
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam[:2]
['cat', 'bat']
>>> spam[1:]
['bat', 'rat', 'elephant']
>>> spam[:]
['cat', 'bat', 'rat', 'elephant']
```

### Getting a List’s Length with len()

```python
>>> spam = ['cat', 'dog', 'moose']
>>> len(spam)
3
```

### Changing Values in a List with Indexes

```python
>>>spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam[1] = 'aardvark'
>>> spam
['cat', 'aardvark', 'rat', 'elephant']
>>> spam[2] = spam[1]
>>> spam
['cat', 'aardvark', 'aardvark', 'elephant']
>>> spam[-1] = 12345
>>> spam
['cat', 'aardvark', 'aardvark', 12345]
```

### List Concatenation and List Replication

```python
>>> [1, 2, 3] + ['A', 'B', 'C']
[1, 2, 3, 'A', 'B', 'C']
>>> ['X', 'Y', 'Z'] * 3
['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z']
>>> spam = [1, 2, 3]
>>> spam = spam + ['A', 'B', 'C']
>>> spam
[1, 2, 3, 'A', 'B', 'C']
```

### Removing Values from Lists with del Statements

```python
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> del spam[2]
>>> spam
['cat', 'bat', 'elephant']
>>> del spam[2]
>>> spam
['cat', 'bat']
```

### Working with Lists

+ Rather than create a new variable for many values, it is often more effective to use a list to store values
+ Imagine the following inneficient program:

```python
print('Enter the name of cat 1:')
catName1 = input()
print('Enter the name of cat 2:')
catName2 = input()
print('Enter the name of cat 3:')
catName3 = input()
print('Enter the name of cat 4:')
catName4 = input()
print('Enter the name of cat 5:')
catName5 = input()
print('Enter the name of cat 6:')
catName6 = input()
print('The cat names are:')
print(catName1 + ' ' + catName2 + ' ' + catName3 + ' ' + catName4 + ' ' +
catName5 + ' ' + catName6)
```

+ We can very easily improve the efficiency of this program by using lists:

```python
catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) +
      ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] # list concatenation
print('The cat names are:')
for name in catNames:
    print('  ' + name)
```

### Using for Loops with Lists

```python
for i in [0, 1, 2, 3]:
    print(i)
```

```
0
1
2
3
```

+ A common Python technique is to use `range(len(someList))` with a for loop to iterate over the indexes of a list

```python
supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])
```

```
Index 0 in supplies is: pens
Index 1 in supplies is: staplers
Index 2 in supplies is: flame-throwers
Index 3 in supplies is: binders
```

### The in and not in Operators

```python
>>> 'howdy' in ['hello', 'hi', 'howdy', 'heyas']
True
>>> spam = ['hello', 'hi', 'howdy', 'heyas']
>>> 'cat' in spam
False
>>> 'howdy' not in spam
False
>>>'cat' not in spam
True
```

```python
myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name:')
name = input()
if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')
```

```
Enter a pet name:
Footfoot
I do not have a pet named Footfoot
```

### The Multiple Assignment Trick

+ Instead of doing:

```python
>>> cat = ['fat', 'orange', 'loud']
>>> size = cat[0]
>>> color = cat[1]
>>> disposition = cat[2]
```

+ You could do this:

```python
>>> cat = ['fat', 'orange', 'loud']
>>> size, color, disposition = cat
```

+ Note: The number of variables and the length of the list must be exactly equal or Python will return a `ValueError`:

```python
>>> cat = ['fat', 'orange', 'loud']
>>> size, color, disposition, name = cat
```

```
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    size, color, disposition, name = cat
ValueError: need more than 3 values to unpack
```

+ The multiple assignment trick can also be used to swap the values in two variables:

```python
>>> a, b = 'Alice', 'Bob'
>>> a, b = b, a
>>> print(a)
'Bob'
>>> print(b)
'Alice'
```

### Augmented Assignment Operators

+ __Augmented asignment operators__ are a shortcut:

```python
>>> spam = 42
>>> spam += 1
>>> spam
43
```

| Augmented assignment statement | Equivalent assignment statement |
| ------------------------------ | ------------------------------- |
| `spam += 1`                    | `spam = spam + 1`               |
| `spam -= 1`                    | `spam = spam - 1`               |
| `spam *= 1`                    | `spam = spam * 1`               |
| `spam /= 1`                    | `spam = spam / 1`               |
| `spam %= 1`                    | `spam = spam % 1`               |

+ The `+=` and `*=` operators can also work on strings and lists for concatenation and replication

```python
>>> spam = 'Hello'
>>> spam += ' world!'
>>> spam
'Hello world!'
```

```python
>>> bacon = ['Zophie']
>>> bacon *= 3
>>> bacon
['Zophie', 'Zophie', 'Zophie']
```

### Methods