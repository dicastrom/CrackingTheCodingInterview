


'''

Implementation of a basic stack in Python, pop(),push(),peek() and print stack are all implemented
can add string or ints/floats to a stack
keeps track of the largest/smallest element in the stack in an average of O(1) with a worst case of O(N). While the min 
of max element is NOT the one being popped it will be O(1)

To Do:
Fix the min/max elements


'''


class StackNode:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
        self.min_element = None
        self.max_element = None
    def pop(self):
        if(self.size == 0):
            print("Stack is already empty!")
        else:
            self.size-=1
            if(self.size == 0):
                print("Popping ", self.top.data)
                self.top = None
                self.min_element = None
                self.max_element = None
            else:
                if(self.top.data == self.max_element or self.top.data == self.min_element):
                    print("Popping ", self.top.data)
                    self.top = self.top.next
                    self.find_max_min()


                else:
                    print("Popping ", self.top.data)
                    self.top = self.top.next

    def find_max_min(self):
        smallest = self.top.data
        largest = self.top.data
        current = self.top
        while current:
            if(current.data > largest):
                largest=current.data
            if(smallest > current.data):
                smallest = current.data
            current=current.next
        self.min_element=smallest
        self.max_element=largest
    def RepresentsInt(self,s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def RepresentsFloat(self,s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def push(self,item,type_element):
        print("Pushing ",item)
        self.size += 1
        if(type_element == "str"):
            if (self.top is None):
                new_node = StackNode(item)
                self.top = new_node
            else:
                new_node = StackNode(item)
                new_node.next = self.top
                self.top = new_node
        else:
            if (self.RepresentsFloat(item) or self.RepresentsInt(item)):
                if (self.min_element is None and self.max_element is None):
                    self.max_element = item
                    self.min_element = item
                else:
                    if (item > self.max_element):
                        self.max_element = item
                    if (self.min_element > item):
                        self.min_element = item
            if (self.top is None):
                new_node = StackNode(item)
                self.top = new_node
            else:
                new_node = StackNode(item)
                new_node.next = self.top
                self.top = new_node


    def peek(self):
        if(self.size>0):
            print("Top = ",self.top.data)
        else:
            print("Empty stack :( ")
    def print_stack(self):
        current = self.top
        print("--------TOP--------")
        while current:
            print(" "*(9-len(str(current.data))),current.data)
            print("         |        ")
            print("         ▼        ")
            current=current.next
        print("--------Bottom--------")
    def is_empty(self):
        if(self.size == 0):
            print("Stack is empty")
        else:
            print("Stack is NOT empty")

    def get_min_element(self):
        print("Min element in stack is = ", str(self.min_element))

    def get_max_element(self):
        print("Max element in stack is = ",self.max_element)
    def push_helper(self):
        element = input("Enter what you want to push to the stack = ")
        if (self.RepresentsFloat(element) or self.RepresentsInt(element)):
            print("Detected Number! ")
            print("Do you want the element to be pushed as a number y/n ")
            print("Please note: if n, will be pushed as string")
            y_n = input(" y/n = ")
            while (y_n.lower()!= 'y' and y_n.lower()!= 'n'):
                print("Invalid option, try again")
                y_n = input(" y/n = ")
            if(y_n.lower() == 'y'):
                if(self.RepresentsInt(element)):
                    self.push(int(element),"int")

                else:
                    self.push(float(element),"float")
            else:
                self.push(element, "str")

        else:
            self.push(element,"str")


    def Exit(self):
        exit(0)
    def Main(self):
        while (True):
            print("Welcome to the stack demo. This stack implementation was created by Diego Castro.")
            print("Options = ")
            print("1 - Push to stack --- Add an element to the stack")
            print("2 - Peek Top --- Print out all the elements ending with Tail ")
            print("3 - Pop Top --- Removes duplicates from the linked list")
            print("4 - Print Stack --- Delete a specific element from the linked list")
            print("5 - Get Min Element --- Prints the kth to last element of the list, 0 being the last")
            print("6 - Get Max Element --- Determines if a specific string is in the list")
            print("7 - Is Empty --- Determines if a specific string is in the list")
            print("E - Exit ")
            optdict = {"1": self.push_helper, "2": self.peek, "3": self.pop, "4": self.print_stack,
                       "5": self.get_min_element, "6": self.get_max_element,"7":self.is_empty, "E": self.Exit}
            option = input("Pick an option = ")
            while option not in optdict.keys():
                print("Invalid Option try again!")
                option = input("Pick an option =  ")
            optdict[option]()



stack = Stack()
stack.Main()










