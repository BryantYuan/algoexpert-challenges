# Sort Stack Solution

## Idea

First of all how would you do this in real-life?

Imagine you have a box full of books with numbers on them. What would be easier: Emptying out all the books, and then
putting them back one by one or by going through the books one by one swapping.

Obviously emptying the box first right? Anyway if we swap the books how are we going to do that in recursive? I mean
sure you can do that but that just defeats the purpose of recursion.

Now, that you have emptied the box, we can start placing the books back using another recursive function.

## Logic

Now some of you might be wondering how on earth are we going to implement this!? Well here's the logic:

1. We will empty the stack by pooping.
2. Every round we pop the last value then call the same function
3. When we have popped every value and come back (remember, its recursion, so you come back), we call the insert function
4. In the insert function, it takes the current stack and the \ current value.
5. If the stack is empty or the last value of the stack is smaller than my current value, push the current value into
   the stack
6. If not take out the last value of the stack (call it bigger_value) and call the insert function again.
7. Once you come back, push the bigger_value you popped earlier back in

## An Example

Ok, that might have been hard to get. Let's go with the example of `stack = [-5, 2, -2, 4, 3, 1]`

1. Pop 1, call sortStack func again
2. Pop 3, call sortStack func again
3. Pop 4, call sortStack func again
4. Pop -2, call sortStack func again
5. Pop 2, call sortStack func again
6. Pop -5, call sortStack func again
7. Now we can't call anything. We pass to the insert func
8. Our current stack is `[]`, our current value is -5.
9. Since our stack is empty, we add -5 to it.
10. Now we return
11. We are now back at step 5 where we popped 2. We also call the insert func
12. We pass in `[-5]` (from last round), and 2 (our current value)
13. Since 2 is bigger than `stack[-1]` (last val) we push in 2.
14. Our stack is now `[5, 2]`
15. Return
16. We are now at step 4, we call insert func.
17. Our stack is `[5, -2]`, current val is -2.
18. Aha! -2 is smaller than 2. We pop 2 and call it bigger_value
19. We call insert func recursivly
20. Ah, now the stack is `[-5]`. -2 > -5 so we push -2 and return
21. Our stack is now `[-5, -2]`. Dont worry we haven'r forggoten about our bigger_value. We now push it back in to make the stack, `[-5, -2, 2]`
22. We continue in this manner

## Actual Solution

Enough chat, if you still don't understand, read the code:

```
def sortStack(array: list) -> list:
    if len(array) <= 1:
        return array

    cur_value = array.pop()

    sortStack(array)

    insertInSortedOrder(array, cur_value)

    return array


def insertInSortedOrder(stack: list, value: int) -> None:
    if not stack or stack[-1] <= value:
        stack.append(value)
        return

    bigger_value = stack.pop()
    insertInSortedOrder(stack, value)
    stack.append(bigger_value)
```

## Code Explanation.

None Yet