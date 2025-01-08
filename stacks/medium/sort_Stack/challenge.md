# Sort Stack

Category: Stacks \
Difficulty: Medium 🟦

## Challenge Description

Write a function that takes in an array of integers representing a stack, recursively sorts the stack in place (i.e. doesn't create a brand-new array), and returns it. 

The array must be treated as a stack. Therefore, you're only allowed to:

* Pop elements from the top of the stack by removing elements from the end of the array using the built-in `.pop()` method
* Push elements to the top of the stack by appending elements to the end of the array using the built-in `.append()` method.
* Peek at the element on top by accessing the last element in the stack.

You're'e not allowed to perform any other operations on the input array, including accessing elements (except for the last one), moving elements, etc. You're also not allowed to use any other data structures and your solution must be recursive

## Sample

#### Sample Input
`stack = [-5, 2, -2, 4, 3, 1]`

#### Sample Output

`[5, -2, 1, 2, 3, 4]`

## Starting Code

```
def sortStack(stack):
    # Write your code here.
    return []
```