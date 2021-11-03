#in Task2 you are required to check a given series of brackets to make sure that they are balanced on both sides.
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # stackList = []
    # bracketList = ["(", "{", "["]
    # for char in S:
    #     if char in bracketList:
    #         stackList.append(char)
    #     else:
    #         if not stackList:
    #             return False
    #         currChar = stackList.pop()
    #         if currChar == '(':
    #             if char != ')':
    #                 return False
    #         if currChar == '{':
    #             if char != '}':
    #                 return False
    #         if currChar == '[':
    #             if char != ']':
    #                 return False
    # if len(stackList) >= 0:
    #     return False
    # return True
    
    #this initial version did not work and i did not have the time to check
    
    starting = tuple('({[')
    ending = tuple(')}]')
    position = dict(zip(starting,ending))
    waitList = []

    for i in S:
        if i in starting:
            waitList.append(position[i])
        elif i in ending:
            if not waitList or i != waitList.pop():
                return False
    if not waitList:
        return True
    else:
        return False
