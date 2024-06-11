'''
Problem:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''


'''
Logic:
To figure out if a string of parentheses is valid or not, we will utilize the stack data structure. The stack will be used
to store the opening parentheses. As we iterate through the string, we add the opening parentheses to the stack and when we
encounter a closing parentheses, we will check if the stack is empty, if it is, then we return False as there is a closing 
without a matching opening. If the stack is not empty, we check if the top of the stack pairs with the current parentheses. If
it does, then we pop that off the stack and continue. Once the iteration is done, the result of whether or not our 
string contains valid parentheses is determined by whether or not the stack is empty. If empty, then we know that every
close bracket matched with a open bracket, resulting in True.
'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        Map = {")":"(", "}":"{", "]":"["}

        for char in s:
            if char in Map.values():
                stack.append(char)
            elif char in Map.keys():
                if stack and stack[-1] == Map[char]:
                    stack.pop()
                else:
                    return False
        
        return not stack