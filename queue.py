
from collections import deque

dlist = deque()

try:
    state = True
    while state:
        print("\nThe keys for the operations are:\nadd element          -> 'A/a'\nlast element         -> 'S/s'\ndelete last element  -> 'D/d'\nempty or not         -> 'E/e'\nsize of stack        -> 'W/w'\ntotal                -> 'T/t'\nto quit              -> 'Q/q'")
        print("\n**************************\n")
        
        x = input("Enter the command: ").lower()

        if x == 'a':
            print("\n**************************\n")
            val = int(input("Enter the element to push: "))
            dlist.appendleft(val)
        
        elif x == 's':
            print("The last element in the stack is",dlist[0])
        
        elif x == 'd':
            r = dlist.pop(0)
            print("Element {} is popped".format(r))
        
        elif x == 'e':
            if len(dlist) == 0:
                print("The deque is empty")
            else:
                print("The Deque is not empty")
        
        elif x == 'w':
            print("The size of the stack is",len(dlist))
        
        elif x == 'q':
            print("\n**************************\n")
            print("Exited Successfully")
            print("\n**************************\n")
            state = False
        
        elif x == 't':
            print("__________________________")
            print(dlist)
            print("__________________________")

        else:
            print("Invalid operators")
except KeyboardInterrupt:
    print("Wrong key")
except IndexError as e:
    print(e)
