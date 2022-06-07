'''
    @Author: Madhavee Kadivar
    @Date: 2022-06-06 21:07:33
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-06-06 21:07:45
    @Title : Queue Implementation
'''
queue = []
def enqueue(ele):
    """ 
        Description: 
            This function is used to enqueue element in queue
        Parameter:
            It takes element as argument
        Return:
            None
    """
    global queue
    queue.append(ele)
    print("\nEnqueued element in queue successfully")
    
def dequeue():
    """ 
        Description: 
            This function is used to dequeue first element from queue
        Parameter:
            None
        Return:
            None
    """
    global queue
    if is_empty():
        print("\nThere is no element to dequeue in queue")
        return 
    
    del_ele = queue.pop(0)
    print("\Dequeued first element from queue successfully")
    return del_ele

def peek():
    """ 
        Description: 
            This function is used to peek first element from queue
        Parameter:
            None
        Return:
            first element
    """
    global queue 
    if is_empty():
        print("\nThere is no element present to peek in queue")
        return   
    return queue[0]

def is_empty():
    """ 
        Description: 
            This function is checking that queue is empty or not
        Parameter:
            None
        Return:
            returns True or False 
    """
    if len(queue) == 0:
        return True
    else: 
        return False
def size():
    """ 
        Description: 
            This function is used to get size of queue
        Parameter:
            None
        Return:
            returns size of queue
    """
    global queue   
    return len(queue)
def print_queue():
    """ 
        Description: 
            This function is printing queue element
        Parameter:
            None
        Return:
            None
    """  
    global queue
    if is_empty():
        print("\nQueue is empty")
        return   
    
    print("\nQueue elements from left to right : ")
    for i in queue:
        print(i,end = " ")
    
if __name__ == "__main__":
    while True:
        print("\n\n1.Enqueue\n2.Dequeue\n3.Peek\n4.Is Empty\n5.Size\n6.Exit")
        choice = input("\nEnter your choice : ")
        if choice == "1":
            num = int(input("\nHow many elements you want to push : "))
            for i in range(num):
                ele = input(f"\nEnter {i+1}th element you want to push : ")
                enqueue(ele)
            print_queue()
        elif choice == "2":
            del_ele = dequeue()
            print(f"\nDequeued element : {del_ele}")
            print_queue()
        elif choice == "3":
            first = peek()
            print(f"\First element of queue is : {first}")           
        elif choice == "4":
            result = is_empty()
            print(f"\nIs queue empty : {result}")
        elif choice == "5":
            s = size()
            print(f"\nSize of queue is : {s}")
        elif choice == "6":
            break
        else:
            print("\n Invalid choice")

    print("\nThank you!!")