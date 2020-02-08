from collections import deque
def sminstr(mystring):
    init_index = 0
    a = 'none'
    queue = deque()
    value = 0
    s = 0
    while init_index < len(mystring):
        if mystring[init_index] == '+' or mystring[init_index] == '-':
            if init_index >0 and mystring[init_index-1] != ')' :
                if s == -1:
                    value = value*(-1)  # make value negative before append if needed
                queue.appendleft(value)
                if a != 'none':
                    queue.appendleft(a)
            value = 0
            s = 0
            # save sign to append after next value or brackets:
            a = mystring[init_index]

        # find start and end indices of segment in brackets
        # and make recursive call to it:
        elif mystring[init_index] == '(':

            start = init_index
            num = 1
            while num != 0:
                init_index += 1
                if mystring[init_index] == '(':
                    num += 1
                if mystring[init_index] == ')':
                    num -= 1
            inner_queue = sminstr(mystring[start + 1:init_index])
            # need to reverse because of crazy behavior of extendleft:
            inner_queue.reverse()
            queue.extendleft(inner_queue)
            if a != 'none':
                queue.appendleft(a)  # append sign that was saved before brackets
        else:
            if init_index == 1:  # numbers with sign can occur only in the beginning
                if a == '-':  # it's just a negative number
                    s = -1
                elif a == '+':  # it's just a positive number
                    s = 1
                a = 'none'
            value *= 10
            value += int(mystring[init_index])

        # append last element if it is not a ')' :
        if init_index == len(mystring)-1 and mystring[init_index] != ')':
            if s == -1:
                value = value * (-1)
            queue.appendleft(value)
            if a != 'none':
                queue.appendleft(a)
        init_index += 1
    return queue

