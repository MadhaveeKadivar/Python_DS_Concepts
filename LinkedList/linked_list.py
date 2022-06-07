'''
    @Author: Madhavee Kadivar
    @Date: 2022-06-06 22:12:41
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-06-07 10:12:57
    @Title : Linked List Implementation
'''

class Node:
    def __init__(self, data):
        """ 
        Description: 
            Constructor and used to initialize data and next variable of node
        Parameter:
            It takes self and any one node data of linkedlist as argument
        Return:
            None
        """
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        """ 
        Description: 
            Constructor and used to initialize head node
        Parameter:
            It takes one self as argument
        Return:
            Nothing
        """
        self.head = None
    def add_first(self,data):
        """ 
        Description: 
            This function is adding node to at first of linked list
        Parameter:
            It takes self and any one node data of linkedlist as argument
        Return:
            returns employee work hours for one day 
        """
        new_node = Node(data)
        if self.head == None:
            self.head=new_node; # If head pointing to none then node is directly pointing to new node
            print(f"\n\"{data}\" is inserted at first of linked list")
            return           
        new_node.next = self.head; # newnode pointing to where head is currently pointing
        self.head = new_node; # head is pointing to new node
        print(f"\n\"{data}\" is inserted at first of linked list")

    def print_list(self):
        """ 
        Description: 
            This function is printing linked list elements
        Parameter:
            It takes one integer as argument
        Return:
            None
        """
        count = 0
        temp = self.head
        if (temp == None): # If head is none that means linked list is empty
            print("\nThe LinledList is Empty")
            return
        print("\nElements of linked list in sequence are : ")
        while (temp):
            print (temp.data,end = " ")
            count += 1
            temp = temp.next

    def append(self,data): 
        """ 
        Description: 
            This function is adding new data at last of linked list
        Parameter:
            It takes self and any one node data of linkedlist as argument
        Return:
            None
        """
        new_node = Node(data) # Creating a new node 
        if (self.head == None):
            self.head=new_node; # If head pointing to null then hode is directly pointing to new node
            print(f"\n\"{data}\" is appended in linked list")
            return
        else:
            temp = self.head; # taking head as temp node
            while (temp.next != None): # Find a last node 
                temp = temp.next # Go to next node till last nast node               
            temp.next = new_node # Add new Node at last
            print(f"\n\"{data}\" is appended in linked list")

    def delete_at_first(self):
        """ 
        Description: 
            This function is used to delete element at first of linked list
        Parameter:
            It takes one self as argument
        Return:
            returns employee work hours for one day 
        """
        if (self.head == None): #Checking that list is empty or not
            print("\nLinked List is already Empty")
            return
        temp = self.head # Creating a temp node having head reference
        print(f"\nNow deleting first element {temp.data} ....")
        self.head = self.head.next # Deleting a first node  

        
    def delete_at_last(self): 
        """ 
        Description: 
            This function is used to delete element at last of linked list
        Parameter:
            It takes one self as argument
        Return:
            returns employee work hours for one day 
        """
        temp = self.head # Creating a temp node having head reference
        if (temp == None): #Checking that list is empty or not
            print("\nLinked List is already Empty")
            return
        if (temp.next == None): # Checking that list having only one node
            print(f"\nNow deleting last element {temp.data} ....")
            return
        while (temp.next.next != None): # Checking that list having atleast 2 nodes
            temp = temp.next; # Go to next node
        print(f"\nNow deleting last element {temp.next.data} ....")
        temp.next = None; # Deleting a last node    

    def search(self,data):
        """ 
        Description: 
            This function is searching element in linked list
        Parameter:
            It takes self and any one node data of linkedlist as argument
        Return:
            returns True or False
        """
        temp = self.head # Creating a temp node having head reference
        if (temp == None): # Checking that list is empty or not
            print("\nLinked List is Empty")
            return False
        
        while(temp != None):
            if (data == temp.data): # Comparing linked list data to check that element is present or not
                print(f"\n{data} is present in linked list")
                return True
            temp = temp.next # moving to next node        
        print(f"\n{data} is not present in linked list")
        return False
    
    def insert_element(self , prev_data ,new_ele):
        """ 
        Description: 
            This function is insertig element after any node in linked list
        Parameter:
            It takes self and any new node data and previous data
        Return:
            None
        """
        temp = self.head # Creating a temp node having head reference
        if (temp == None): #Checking that list is empty or not
            print("\nLinked List is Empty")
            return
        new_node = Node(new_ele) # Creating a new node 
        
        while (temp != None):        
            if (prev_data == temp.data): # Comparing linked list data to check that element is present or not            
                new_node.next = temp.next # pointing new node to next element
                temp.next = new_node # Pointing prev node to new node
                print(f"\n{new_ele} is inserted in linked list after {prev_data}")
                return
            temp = temp.next # Moving to next node

    def delete_element(self, new_ele):
        """ 
        Description: 
            This function is deleting any specific node
        Parameter:
            It takes self and any one node data of linkedlist as argument
        Return:
            None
        """
        temp = self.head # Creating a temp node having head reference
        print("\nWant to delete element is : "+new_ele)
        if (temp == None ): # Checking that list is empty or not        
            print("\nLinked List is Empty")
            return        
        if (temp != None and new_ele == temp.data): # Checking if list has only one value which user wants to delete
            print(f"\n{new_ele} is deleted")
            self.head = temp.next # Changing head reference
            return        
        while (temp != None and new_ele != temp.data):  # Continue moving till find a value which want to dlete        
            prev = temp #Stoting value one by one in prev
            temp = temp.next # Go to next node        
        prev.next = temp.next # Deleting node which want to delete
        print(f"\n{new_ele} is deleted")
        
    def sort_list(self):
        """ 
        Description: 
            This function is sorting linked list
        Parameter:
            It takes one self as argument
        Return:
            None
        """
        temp = self.head
        elements = []
        if (temp == None): # If head is none that means linked list is empty
            return
        while (temp):
            elements.append(temp.data)
            temp = temp.next
        elements.sort()
        for i in range(len(elements)):
            self.delete_at_first()
        for i in elements:
            self.append(i)
        self.print_list()
        
    def add_with_acsending_order(self,data): 
        """ 
        Description: 
            This function is adding data in acsending order in linked list
        Parameter:
            It takes self and any one node data of linkedlist as argument
        Return:
            None 
        """
        new_node = Node(data) # Creating a new node with value by user
        #If Head is null make newnode as head otherwise add the element 
        if(self.head == None):         
            self.head = new_node
        else:
            # If newnode is less than the head data then make new node ad head which is pointing to old head
            if(new_node.data < self.head.data):            
                new_node.next=self.head
                self.head=new_node            
            else:
                temp = self.head # Creating a temp varible and store head it in
                while(temp.next!=None and temp.next.data < data): # If new data is greater than all then move temp at last                
                    temp=temp.next                
                if(temp.next!=None): # If temp is pointing to any node then make add new node after temp                
                    new_node.next = temp.next
                    temp.next=new_node
                else: # If temp is pointing to null then make add new node at last
                    temp.next = new_node
                    new_node.next=None
        print(f"\n{data} is Added in Linked List")
        
if __name__ == "__main__":
    list = LinkedList()
    while True:
        print("\n\n\n1.Add First\n2.Append\n3.Delete at First \n4.Delete at Last\n5.Search Element\n6.Insert Element\n7.Delete Element\n8.Sort\n9.Add with order\n10.Exit")

        choice = input("\nEnter your choice : ")
        
        if choice == "1":
            num = int(input("\nHow many elements you want to add in list : "))
            for i in range(num):
                ele = input(f"\nEnter {i+1}th element : ")
                list.add_first(ele)
            list.print_list()
            
        elif choice == "2":
            num = int(input("How many elements you want to add in list : "))
            for i in range(num):
                ele = input(f"\nEnter {i+1}th element : ")
                list.append(ele)
            list.print_list()
            
        elif choice == "3":
            list.delete_at_first()
            list.print_list()
            
        elif choice == "4":
            list.delete_at_last()
            list.print_list()
            
        elif choice == "5":
            ele = input(f"\nEnter element which you want to search : ")   
            list.search(ele) 
                   
        elif choice == "6":
            prev = input("After which element you want to insert : ")
            ele = input("Enter element you want to insert : ")
            check = list.search(prev)
            if check:
                list.insert_element(prev,ele)
            list.print_list()
            
        elif choice == "7":
            ele = input("Enter element you want to delete : ")
            check = list.search(ele)
            if check:
                list.delete_element(ele)
            list.print_list()
             
        elif choice == "8":
            list.sort_list()
            
        elif choice == "9":
            num = int(input("\nHow many elements you want to add in list : "))
            for i in range(num):
                ele = input(f"\nEnter {i+1}th element : ")
                list.add_with_acsending_order(ele)
            list.print_list()
            
        elif choice == "10":
            break
        else:
            print("\n Invalid choice")

    print("\nThank you!!")