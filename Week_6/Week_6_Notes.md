# Week 6

## Overview

In week 6, we cover critical topics in computer science; computer architecture and functions.

We will look at how functions are used in programs. Don't let functions from high school math intimidate you. I think you will find that functions, in the context of computers, are much more intuitive than the abstract f(x) you learned in algebra.

We will begin working on a larger password saver program. The final versions of both the program is due at the end of Week 7. You need to turn in a first draft at the end of this week. This is an opportunity for help getting past any stuck points.  

## Objectives

By the end of this week, you should be able to:

+ Explain the role of registers in the CPU
+ Explain the difference between big endian and little endian
+ Be able to use functions in python programs
+ Be able to manipulate strings in python programs

## Activities and Assignments

+ Week 6: Discussion - Understanding the Scott CPU
+ Week 6: Self-Paced Assignment
+ Week 6: First Draft - Password Saver

## Lesson

### How the CPU Works

<iframe width="560" height="315" src="https://www.youtube.com/embed/cNN_tTXABUA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Endianess

+ Endianess describes the order of the bytes within the memory of the computer
+ A computer can either be "Big Endian" or "Little Endian"

<iframe width="560" height="315" src="https://www.youtube.com/embed/JrNF0KRAlyo" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Functions

+ Python has build in functions like `print()`, `input()`, and `len()`
+ But you can also write your own functions

```python
def hello():
    print('Howdy!')
    print('Howdy!!!')
    print('Hello there.')
hello()
hello()
hello()
```

```
Howdy!
Howdy!!!
Hello there.
Howdy!
Howdy!!!
Hello there.
Howdy!
Howdy!!!
Hello there.
```

+ Functions allow us to avoid duplicating code

#### def Statements with Parameters

+ In the `print()` or `len()` functions, you pass in values, called **arguments**
+ You can also define your own functions that accept arguments

```python
def hello(name):
    print('Hello ' + name)

hello('Alice')
hello('Bob')
```

```
Hello Alice
Hello Bob
```

#### Return Values and return Statements

```python
import random
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'

r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)
```

#### The None Value

+ In Python there is a value called `None`, which represents the absence of a value
+ `None` is the only value of the `NoneType` data type. (Other programming languages might call this value `null`, `nil`, or `undefined`)

#### Keyword Arguments and print()

+ __Keyword arguments__ are identified by the keyword put before them in the function call
+ Keyword arguments are often used for optional parameters

#### Local and Global Scope

+ Parameters and variables that are assigned in a called function are said to exist in that function’s __local scope__
+ Variables that are assigned outside all functions are said to exist in the __global scope__
+ Code in the global scope cannot use any local variables
+ However, a local scope can access global variables
+ Code in a function’s local scope cannot use variables in any other local scope
+ You can use the same name for different variables if they are in different scopes. That is, there can be a local variable named `spam` and a global variable also named `spam`

```python
def spam():
    eggs = 31337
spam()
print(eggs)
```

```
Traceback (most recent call last):
  File "C:/test3784.py", line 4, in <module>
    print(eggs)
NameError: name 'eggs' is not defined
```

```python
def spam():
    eggs = 99
    bacon()
    print(eggs)

  def bacon():
      ham = 101
    eggs = 0

spam()
```

```
99
```

```python
def spam():
    print(eggs)
eggs = 42
spam()
print(eggs)
```

```
42
```

```python
 def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)
```

```
spam
```

There are four rules to tell whether a variable is in a local scope or global scope:

1. If a variable is being used in the global scope (that is, outside of all functions), then it is always a global variable.
2. If there is a global statement for that variable in a function, it is a global variable.
3. Otherwise, if the variable is used in an assignment statement in the function, it is a local variable.
4. But if the variable is not used in an assignment statement, it is a global variable.

### Strings

#### String Literals

+ Typing the string `'That is Alice's cat.'` in Python won't work because the string will end after `Alice`
+ Several ways to solve this problem

#### Double Quotes

+ Strings can begin and end with double quotes

```python
spam = "That is Alice's cat."
```

#### Escape Characters

+ An __escape character__ lets you use characters that are otherwise impossible to put into a string
+ An escape character consists of a backslash `\` followed by the character you want to add to the string.

```python
spam = 'Say hi to Bob\'s mother.'
```

+ Escape characters you can use:

|Escape Character|Print as|
|----------------|--------|
|`\'`|Single quote|
|`\"`|Double quote|
|`\t`|Tab|
|`\n`|Newline (line break)|
|`\\`|Backslash|

```python
print("Hello there!\nHow are you?\nI\'m doing fine.")
```

```
Hello there!
How are you?
I'm doing fine.
```

#### Raw Strings

+ You can place an `r` before the beginning quotation mark of a string to make it a __raw string__
+ A __raw string__ completely ignores all escape characters and prints any backslash that appears in the string

```python
print(r'That is Carol\'s cat.')
```

```
That is Carol\'s cat.
```

#### Multiline Strings with Triple Quotes

+ A __multiline string__ begins and ends with either three single or three double quotes

```python
print('''Dear Alice,
Eve's cat has been arrested for catnapping, cat burglary, and extortion.
Sincerely,
Bob''')
```

```
Dear Alice,
Eve's cat has been arrested for catnapping, cat burglary, and extortion.
Sincerely,
Bob
```

#### Multiline Comments

```python
"""This is a test Python program.
Written by Al Sweigart al@inventwithpython.com
This program was designed for Python 3, not Python 2.
"""
def spam():
"""This is a multiline comment to help
explain what the spam() function does."""
print('Hello!')
```

#### Indexing and Slicing with Strings

+ Strings use indexes and slices the same way lists do

```
' H e l l o w o r l d ! '
0 1 2 3 4 5 6 7 8 9 10 11
```

```python
>>> spam = 'Hello world!'
>>> spam[0]
'H'
>>> spam[4]
'o'
>>> spam[-1]
'!'
>>> spam[0:5]
'Hello'
>>> spam[:5]
'Hello'
>>> spam[6:]
'world!'
```

#### The in and not in Operators with Strings

```python
>>> 'Hello' in 'Hello World'
True
>>> 'Hello' in 'Hello'
True
>>> 'HELLO' in 'Hello World'
False
>>> '' in 'spam'
True
>>> 'cats' not in 'cats and dogs'
False
```

#### The upper(), lower(), isupper(), and islower() String Methods

```python
>>> spam = 'Hello world!'
>>> spam = spam.upper()
>>> spam
'HELLO WORLD!'
>>> spam = spam.lower()
>>> spam
'hello world!'
```

```python
print('How are you?')
feeling = input()
if feeling.lower() == 'great':
print('I feel great too.')
else:
print('I hope the rest of your day is good.')
```

```
How are you?
GREat
I feel great too.
```

```python
>>> spam = 'Hello world!'
>>> spam.islower()
False
>>> spam.isupper()
False
>>>'HELLO'.isupper()
True
>>> 'abc12345'.islower()
True
>>> '12345'.islower()
False
>>> '12345'.isupper()
False
```

```python
>>> 'Hello'.upper()
'HELLO'
>>> 'Hello'.upper().lower()
'hello'
>>> 'Hello'.upper().lower().upper()
'HELLO'
>>> 'HELLO'.lower()
'hello'
>>> 'HELLO'.lower().islower()
True
```

#### The is X String Methods

+ `isalpha()` returns True if the string consists only of letters and is not blank.
+ `isalnum()` returns True if the string consists only of letters and numbers and is not blank.
+ `isdecimal()` returns True if the string consists only of numeric characters and is not blank.
+ `isspace()` returns True if the string consists only of spaces, tabs, and new-lines and is not blank.
+ `istitle()` returns True if the string consists only of words that begin with an uppercase letter followed by only lowercase letters.

```python
>>> 'hello'.isalpha()
True
>>> 'hello123'.isalpha()
False
>>> 'hello123'.isalnum()
True
>>> 'hello'.isalnum()
True
>>> '123'.isdecimal()
True
>>> ' '.isspace()
True
>>> 'This Is Title Case'.istitle()
True
>>> 'This Is Title Case 123'.istitle()
True
>>> 'This Is not Title Case'.istitle()
False
>>> 'This Is NOT Title Case Either'.istitle()
False
```

```python
while True:
print('Enter your age:')
age = input()
if age.isdecimal():
break
print('Please enter a number for your age.')
while True:
print('Select a new password (letters and numbers only):')
password = input()
if password.isalnum():
break
print('Passwords can only have letters and numbers.')
```

```
Enter your age:
forty two
Please enter a number for your age.
Enter your age:
42
Select a new password (letters and numbers only):
secr3t!
Passwords can only have letters and numbers.
Select a new password (letters and numbers only):
secr3t
```

#### The startswith() and endswith() String Methods

+ The `startswith()` and `endswith()` methods return `True` if the string value they are called on begins or ends (respectively) with the string passed to the method; otherwise, they return False

```python
>>> 'Hello world!'.startswith('Hello')
True
>>> 'Hello world!'.endswith('world!')
True
>>> 'abc123'.startswith('abcdef')
False
>>> 'abc123'.endswith('12')
False
>>> 'Hello world!'.startswith('Hello world!')
True
>>> 'Hello world!'.endswith('Hello world!')
True
```

#### The join() and split() String Methods

```python
>>> ', '.join(['cats', 'rats', 'bats'])
'cats, rats, bats'
>>> ' '.join(['My', 'name', 'is', 'Simon'])
'My name is Simon'
>>> 'ABC'.join(['My', 'name', 'is', 'Simon'])
'MyABCnameABCisABCSimon'
```

```python
>>> 'My name is Simon'.split()
['My', 'name', 'is', 'Simon']
```

+ By default `split()` splits on whitespace

```python
>>> 'MyABCnameABCisABCSimon'.split('ABC')
['My', 'name', 'is', 'Simon']
>>> 'My name is Simon'.split('m')
['My na', 'e is Si', 'on']
```

```python
spam = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment".
Please do not drink it.
Sincerely,
Bob'''
spam.split('\n')
```

```
['Dear Alice,', 'How have you been? I am fine.', 'There is a container in the
fridge', 'that is labeled "Milk Experiment".', '', 'Please do not drink it.',
'Sincerely,', 'Bob']
```

#### Justifying Text with rjust(), ljust(), and center()

```python
>>> 'Hello'.rjust(10)
' Hello'
>>> 'Hello'.rjust(20)
' Hello'
>>> 'Hello World'.rjust(20)
' Hello World'
>>> 'Hello'.ljust(10)
'Hello '
```

```python
>>> 'Hello'.rjust(20, '*')
'***************Hello'
>>> 'Hello'.ljust(20, '-')
'Hello---------------'
```

```python
>>> 'Hello'.center(20)
' Hello '
>>> 'Hello'.center(20, '=')
'=======Hello========'
```

```python
def printPicnic(itemsDict, leftWidth, rightWidth):
print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
for k, v in itemsDict.items():
print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)
```

```
---PICNIC ITEMS--
sandwiches.. 4
apples...... 12
cups........ 4
cookies..... 8000
-------PICNIC ITEMS-------
sandwiches.......... 4
apples.............. 12
cups................ 4
cookies............. 8000
```

#### Removing Whitespace with strip(), rstrip(), and lstrip()

```python
>>> spam = ' Hello World '
>>> spam.strip()
'Hello World'
>>> spam.lstrip()
'Hello World '
>>> spam.rstrip()
' Hello World'
```

```python
>>> spam = 'SpamSpamBaconSpamEggsSpamSpam'
>>> spam.strip('ampS')
'BaconSpamEggs'
```

### Pig Latin Example Program

```python
# Name:
# Large Project: Pig Latin
# piglatin.py

"""
Google -> ooglegay
frog -> rogfay
ate -> ateway

Have a nice day
avehay away icenay ayday
"""

vowels = ('a', 'e', 'i', 'o', 'u')




def convert_word(word):
    """Converts an individual word to piglatin
    
    :param word (String) The word to convert
    
    :return (String) the word in piglatin
    
    Helper function that converts one word into Pig-Latin. Remember, our word is
    the function's argument, like 4 is the argument in sqrt(4). We don't need to
    know anything about the sentence from which the word came.
    
    Also, remember that strings are index-able, just like lists and tuples. But,
    they are immutable, like tuples. So when we want to append "ay" or "hay" to
    the end, we can't use append(). But, we can use the string concatenation (+)
    operator to return a new string.
    
    e.g. we can't do "a".append("b"), but we can do "a" + "b".
    For error handling purposes, you should convert each word to lowercase using word.lower()
    """
    
    wordInPigLatin = ""
    ####### YOUR CODE HERE ######

    ####### YOUR CODE HERE ######
    return wordInPigLatin


def convert_sentence(sentence):
    """Convert a sentence to piglatin
    
    Makes use of convert_word() to convert the sentence.
    
    :param sentence (String) The sentence to convert
    
    :return (String) The sentence in piglatin
    """
    new_sentence = ""
    ####### YOUR CODE HERE ######

    ####### YOUR CODE HERE ######
    return new_sentence


# The main program

print('Type in your sentence to be converted to Pig-Latin!')
print("Please don't use punctuation or numbers.")

text = input()  
                  
print
print(convert_sentence(text))
```





