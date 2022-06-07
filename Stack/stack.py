'''
    @Author: Madhavee Kadivar
    @Date: 2022-06-06 20:03:06
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-06-06 20:03:06
    @Title : Stack Implementation
'''
stack = []
def push(ele):
    """ 
        Description: 
            This function is pushing element on to stack
        Parameter:
            It takes element as argument
        Return:
            None
    """
    global stack
    stack.append(ele)
    print("\nPushed onto stack successfully")
def pop():
    """ 
        Description: 
            This function is used to pop top element from stack
        Parameter:
            None
        Return:
            None
    """
    global stack
    if is_empty():
        print("\nThere is no element present to pop in stack")
        return 
    
    del_ele = stack.pop()
    print("\nPopped top element from stack successfully")
    return del_ele

def peek():
    """ 
        Description: 
            This function is used to peek top element from stack
        Parameter:
            None
        Return:
            top element
    """
    global stack 
    if is_empty():
        print("\nThere is no element present to peek in stack")
        return   
    return stack[-1]

def is_empty():
    """ 
        Description: 
            This function is checking that stack is empty or not
        Parameter:
            None
        Return:
            returns True or False 
    """
    if len(stack) == 0:
        return True
    else: 
        return False
def size():
    """ 
        Description: 
            This function is used to get size of stack
        Parameter:
            None
        Return:
            returns size of stack
    """
    global stack   
    return len(stack)
def print_stack():
    """ 
        Description: 
            This function is printing stack element
        Parameter:
            None
        Return:
            None
    """  
    global stack
    if is_empty():
        print("\nStack is empty")
        return   
    
    print("\nStack elements from top to bottom : ")
    for i in stack[::-1]:
        print(i)
    
if __name__ == "__main__":
    while True:
        print("\n1.push\n2.pop\n3.peek\n4.Is Empty\n5.size\n6.Exit")
        choice = input("\nEnter your choice : ")
        if choice == "1":
            num = int(input("How many elements you want to push : "))
            for i in range(num):
                ele = input(f"\nEnter {i+1}th element you want to push : ")
                push(ele)
            print_stack()
        elif choice == "2":
            pop()
            print_stack()
        elif choice == "3":
            top = peek()
            print(f"\nTop element of stack is : {top}")           
        elif choice == "4":
            result = is_empty()
            print(f"\nIs stack empty : {result}")
        elif choice == "5":
            s = size()
            print(f"\nSize of stack is : {s}")
        elif choice == "6":
            break
        else:
            print("\n Invalid choice")

    print("\nThank you!!")