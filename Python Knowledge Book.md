Python is case sensitive and indented

Python

print()
Case sensitive and spacing is very important

Operators
+, *, -, /
Exponentiation **
% Modulo  
^ carat Bitwise XOR 
// Integer division

Variable name, assignment operator (=), variable

x=y is not equal to y=x

Variable names = No reserved names or identifiers
Typical ones, all lower case letters and under_score letters
Writing variable names that are descriptive

Keywords: 

False
class
Finally
is
return
None
continue
for
lambda
try
True
Def
from
nonlocal
while
and
del
global
not
with
as
elif
if
or
yield
assert
else
import
pass
break
except
in 
Raise
Variables
In Python, Numbers are of 4 types:
Integer.
Floating Point or Real Numbers.
Complex Numbers.
Boolean.
Integers and Floats
There are two Python data types that could be used for numeric values:
int - for integer values
float - for decimal or floating point values
https://www.python.org/dev/peps/pep-0008/
https://softwareengineering.stackexchange.com/questions/148677/why-is-80-characters-the-standard-limit-for-code-width
https://atom.io/packages/linter-python-pep8


79 - 99 characters line

In general, there are two types of errors to look out for
Exceptions
Syntax
https://docs.python.org/3/tutorial/errors.html

Booleans, Comparison Operators, and Logical Operators
The bool data type holds one of the values True or False, which are often encoded as 1 or 0, respectively.
There are 6 comparison operators that are common to see in order to obtain a boolvalue:
Comparison Operators
Symbol Use Case
Bool
Operation
5 < 3
False
Less Than
5 > 3
True
Greater Than
3 <= 3
True
Less Than or Equal To
3 >= 5
False
Greater Than or Equal To
3 == 5
False
Equal To
3 != 5
True
Not Equal To
And there are three logical operators you need to be familiar with:
Logical Use
Bool
Operation
5 < 3 and 5 == 5
False
and - Evaluates if all provided statements are True
5 < 3 or 5 == 5
True
or - Evaluates if at least one of many statements is True
not 5 < 3
True
not - Flips the Bool Value

Strings
Strings in Python are shown as the variable type str. You can define a string with either double quotes " or single quotes '. If the string you are creating actually has one of these two values in it, then you need to be careful to assure your code doesn't give an error.
len(udacity) -> Built in function

TypeError: object of type 'int' has no len(), which alludes to the fact that len only works on a "sequence (such as a string, bytes, tuple, list, or range) or a collection (such as a dictionary, set, or frozen set),


Built-in functions:

https://docs.python.org/2/library/functions.html#len

int
string
float
str()

String Methods
In this video you were introduced to methods. Methods are like some of the functions you have already seen:
len("this")
type(12)
print("Hello world")
These three above are functions - notice they use parentheses, and accept one or more arguments. Functions will be studied in much more detail in a later lesson!
A method in Python behaves similarly to a function. Methods actually are functions that are called using dot notation. For example, lower() is a string method that can be used like this, on a string called "sample string": sample_string.lower().
Methods are specific to the data type for a particular variable. So there are some built-in methods that are available for all strings, different methods that are available for all integers, etc.
Below is an image that shows some methods that are possible with any string.

Each of these methods accepts the string itself as the first argument of the method. However, they also could receive additional arguments, that are passed inside the parentheses. Let's look at the output for a few examples.
>>> my_string.islower()
True
>>> my_string.count('a')
2
>>> my_string.find('a')
3


You can see that the count and find methods both take another argument. However, the .islower() method does not accept another argument.
No professional has all the methods memorized, which is why understanding how to use documentation and find answers is so important. Gaining a strong grasp of the foundations of programming will allow you to use those foundations to use documentation to build so much more than someone who tries to memorize all the built-in methods in Python.
One important string method: format()
We will be using the format() string method a good bit in our future work in Python, and you will find it very valuable in your coding, especially with your printstatements.
We can best illustrate how to use format() by looking at some examples:
# Example 1
print("Mohammed has {} balloons".format(27))


Mohammed has 27 balloons


# Example 2
animal = "dog"
action = "bite"
print("Does your {} {}?".format(animal, action))


Does your dog bite?


# Example 3
maria_string = "Maria loves {} and {}"
print(maria_string.format("math","statistics"))


Maria loves math and statistics
Notice how in each example, the number of pairs of curly braces {} you use inside the string is the same as the number of replacements you want to make using the values inside format().
More advanced students can learn more about the formal syntax for using the format() string method here.
Python Container - List contains other data types

Lists!
Data structures are containers that organize and group data types together in different ways. A list is one of the most common and basic data structures in Python.
You saw here that you can create a list with square brackets. Lists can contain any mix and match of the data types you have seen so far.
list_of_random_things = [1, 3.4, 'a string', True]


This is a list of 4 elements. All ordered containers (like lists) are indexed in python using a starting index of 0. Therefore, to pull the first value from the above list, we can write:
>>> list_of_random_things[0]
1


It might seem like you can pull the last element with the following code, but this actually won't work:
>>> list_of_random_things[len(list_of_random_things)] 
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-34-f88b03e5c60e> in <module>()
----> 1 lst[len(lst)]

IndexError: list index out of range


However, you can retrieve the last element by reducing the index by 1. Therefore, you can do the following:
>>> list_of_random_things[len(list_of_random_things) - 1] 
True


Alternatively, you can index from the end of a list by using negative values, where -1 is the last element, -2 is the second to last element and so on.
>>> list_of_random_things[-1] 
True
>>> list_of_random_things[-2] 
a string


Slice and Dice with Lists
You saw that we can pull more than one value from a list at a time by using slicing. When using slicing, it is important to remember that the lower index is inclusiveand the upper index is exclusive.
Therefore, this:
>>> list_of_random_things = [1, 3.4, 'a string', True]
>>> list_of_random_things[1:2]
[3.4]


will only return 3.4 in a list. Notice this is still different than just indexing a single element, because you get a list back with this indexing. The colon tells us to go from the starting value on the left of the colon up to, but not including, the element on the right.
If you know that you want to start at the beginning, of the list you can also leave out this value.
>>> list_of_random_things[:2]
[1, 3.4]


or to return all of the elements to the end of the list, we can leave off a final element.
>>> list_of_random_things[1:]
[3.4, 'a string', True]


This type of indexing works exactly the same on strings, where the returned value will be a string.
Are you in OR not in?
You saw that we can also use in and not in to return a bool of whether an element exists within our list, or if one string is a substring of another.
>>> 'this' in 'this is a string'
True
>>> 'in' in 'this is a string'
True
>>> 'isa' in 'this is a string'
False
>>> 5 not in [1, 2, 3, 4, 6]
True
>>> 5 in [1, 2, 3, 4, 6]
False
Lists - Lower bound inclusive but upper bound exclusive

Length of a string is the number of characters whereas the length of the list is the number of elements it holds.

Python has 0 indexing

Mutability and Order
Mutability is about whether or not we can change an object once it has been created. If an object (like a list or string) can be changed (like a list can), then it is called mutable. However, if an object cannot be changed with creating a completely new object (like strings), then the object is considered immutable.
>>> my_lst = [1, 2, 3, 4, 5]
>>> my_lst[0] = 'one'
>>> print(my_lst)
['one', 2, 3, 4, 5]


As shown above, you are able to replace 1 with 'one' in the above list. This is because lists are mutable.
However, the following does not work:
>>> greeting = "Hello there"
>>> greeting[0] = 'M'


This is because strings are immutable. This means to change this string, you will need to create a completely new string.
There are two things to keep in mind for each of the data types you are using:
Are they mutable?
Are they ordered?
Order is about whether the position of an element in the object can be used to access the element. Both strings and lists are ordered. We can use the order to access parts of a list and string.
However, you will see some data types in the next sections that will be unordered. For each of the upcoming data structures you see, it is useful to understand how you index, are they mutable, and are they ordered. Knowing this about the data structure is really useful!
Additionally, you will see how these each have different methods, so why you would use one data structure vs. another is largely dependent on these properties, and what you can easily do with it!
Mutability and Order

List Manipulation using indexing

Tuples
A tuple is another useful container. It's a data type for immutable ordered sequences of elements. They are often used to store related pieces of information. Consider this example involving latitude and longitude:
location = (13.4125, 103.866667)
print("Latitude:", location[0])
print("Longitude:", location[1])


Tuples are similar to lists in that they store an ordered collection of objects which can be accessed by their indices. Unlike lists, however, tuples are immutable - you can't add and remove items from tuples, or sort them in place.
Tuples can also be used to assign multiple variables in a compact way.
dimensions = 52, 40, 100
length, width, height = dimensions
print("The dimensions are {} x {} x {}".format(length, width, height))


The parentheses are optional when defining tuples, and programmers frequently omit them if parentheses don't clarify the code.
In the second line, three variables are assigned from the content of the tuple dimensions. This is called tuple unpacking. You can use tuple unpacking to assign the information from a tuple into multiple variables without having to access them one by one and make multiple assignment statements.
If we won't need to use dimensions directly, we could shorten those two lines of code into a single line that assigns three variables in one go!
length, width, height = 52, 40, 100
print("The dimensions are {} x {} x {}".format(length, width, height))


Have questions? Head to the forums for discussion with the Udacity Community.



Sets
A set is a data type for mutable unordered collections of unique elements. One application of a set is to quickly remove duplicates from a list.
numbers = [1, 2, 6, 3, 1, 1, 6]
unique_nums = set(numbers)
print(unique_nums)


This would output:
{1, 2, 3, 6}


Sets support the in operator the same as lists do. You can add elements to sets using the add method, and remove elements using the pop method, similar to lists. Although, when you pop an element from a set, a random element is removed. Remember that sets, unlike lists, are unordered so there is no "last element".
fruit = {"apple", "banana", "orange", "grapefruit"}  # define a set

print("watermelon" in fruit)  # check for element

fruit.add("watermelon")  # add an element
print(fruit)

print(fruit.pop())  # remove a random element
print(fruit)


This outputs:
False
{'grapefruit', 'orange', 'watermelon', 'banana', 'apple'}
grapefruit
{'orange', 'watermelon', 'banana', 'apple'}


Other operations you can perform with sets include those of mathematical sets. Methods like union, intersection, and difference are easy to perform with sets, and are much faster than such operators with other containers.
 
Methods are functions that belong to an object. The object is always the first argument to a method.


Debugging Code
Everyone gets "bugs," or unexpected errors, in their code, and this is a normal and expected part of software development. We all say at one time or another, "Why isn't this computer doing what I want it to do?!"

So an important part of coding is "debugging" your code, to remove these bugs. This can often take a long time, and cause you frustration, but developing effective coding habits and mental calmness will help you address these issues. With determined persistence, you can prevail over these bugs!

Here are some tips on successful debugging that we'll discuss in more detail below:

Understand common error messages you might receive and what to do about them.
Search for your error message, using the Web community.
Use print statements.

Understanding Common Error Messages
There are many different error messages that you can receive in Python, and learning how to interpret what they're telling you can be very helpful. Here are some common ones for starters:

"ZeroDivisionError: division by zero." This is an error message that you saw earlier in this lesson. What did this error message indicate to us? You can look back in the Quiz: Arithmetic Operators section to review it if needed.
"SyntaxError: unexpected EOF while parsing" Take a look at the two lines of code below. Executing these lines produces this syntax error message - do you see why?
greeting = "hello"
print(greeting.upper
This message is often produced when you have accidentally left out something, like a parenthesis. The message is saying it has unexpectedly reached the end of file ("EOF") and it still didn't find that right parenthesis. This can easily happen with code syntax involving pairs, like beginning and ending quotes also.
"TypeError: len() takes exactly one argument (0 given)" This kind of message could be given for many functions, like len in this case, if I accidentally do not include the required number of arguments when I'm calling a function, as below. This message tells me how many arguments the function requires (one in this case), compared with how many I gave it (0). I meant to use len(chars) to count the number of characters in this long word, but I forgot the argument.
chars = "supercalifragilisticexpialidocious"
len()
There are other kinds of error messages that you'll certainly begin experiencing soon in your Python work. Learning what they mean and how to address them will help you debug your code. You might keep an ongoing page of notes on them.

Search for Your Error Message
Software developers like to share their problems and solutions with each other on the web, so using Google search, or searching in StackOverflow, or searching in Udacity's Knowledge forum are all good ways to get ideas on how to address a particular error message you're getting.

Copy and paste the error message into your web browser search tab, or in Knowledge, and see what others suggest about what might be causing it.
You can copy and paste the whole error message, with or without quotes around it.
Or you can search using just key words from the error message or situation you're facing, along with some other helpful words that describe your context, like Python and Mac.
Use Print Statements to Help Debugging
Adding print statements temporarily into your code can help you see which code lines have been executed before the error occurs, and see the values of any variables that might be important. This approach to debugging can also be helpful even if you're not receiving an error message, but things just aren't working the way you want.
