#Implementation of a Singly Linked List in python

class Node(object):
    def __init__(self, data=None, next_node=None ):
        self.next_node = next_node
        self.data = data
    def print_data(self):
        print(self.data)
    def return_data(self):
        return self.data
    def get_next(self):
        return self.next_node
    def set_next(self,new_next_node):
        self.next_node=new_next_node
class Linked_List(object):
    def __init__(self,head=None):
        self.head =head
    def insert(self):
        data = input("Enter the data you want to add to the linked list = ")
        new_node=Node(data)
        new_node.set_next(self.head)
        self.head= new_node
    def get_size(self):
        current = self.head
        size= 0
        while current:
            size+=1
            current=current.get_next()
        return size
    def print_all(self):
        current = self.head
        while current:
            print(current.return_data()," -> ", end = " ")
            current=current.get_next()
        print("Tail")
    def search(self):
        data= input("Enter what you want to search for = ")
        current = self.head
        while current:
            if(current.return_data() is data):
                print(data," found in the list!")
                break
            current = current.get_next()
        print(data," not in the list :(")
    def delete(self):
        data = input("Enter what you want to delete from the linked list = ")
        prev = None
        current = self.head
        while current:
            if(current.return_data()==data):
                break
            else:
                prev= current
                current=current.get_next()
        if current is None:
            print("Value not in list")
            return

        if prev is None:
            print(data, " deleted")
            self.head=current.get_next()
        else:
            print(data, " deleted")
            prev.set_next(current.get_next())
    def delete_node(self,data):
        prev = None
        current = self.head
        while current:
            if(current.return_data()==data):
                break
            else:
                prev= current
                current=current.get_next()
        if current is None:
            print("Value not in list")
            return

        if prev is None:
            print(data, " deleted")
            self.head=current.get_next()
        else:
            print(data, " deleted")
            prev.set_next(current.get_next())

    #Actual functions start here before is just implementing the singly linked list
    '''
    What this does is that it stores the data of the nodes in a dict
    and when they are duplicates they are removed by calling delete function
    
    Alternatively, a "better" delete function could be implemented that
    deletes the second occurance of a Node 
    
    '''
    def remove_dups(self):
        current = self.head
        keys = {}
        while current:
            print(current.return_data())
            if current.return_data() not in keys:
                keys[current.return_data()]="1"
                current=current.get_next()
            else:
                print("Deleting ",current.return_data())
                self.delete_node(current.return_data())
                current = current.get_next()


    ##Removes the kth to last element 0 being the last element,1 being the 1st to last, ect
    #Removes it by using a queue that stores only
    def Exit(self):
        exit(0)

    def kth_to_last(self):
        from queue import Queue
        k = int(input("Enter the kth to last index = "))
        q = Queue(maxsize=k+1)
        current = self.head
        num=0
        while current:
            #print(current.return_data(), end=" ")
            if (q.full()):
                   q.get()
                   q.put(current.return_data())
            else:
                q.put(current.return_data())
            num+=1
            current = current.get_next()
        if(num<=k):
            print(k,end="")
            print("th to last index is out of range")
        else:
            if(k==0):
                print("Last element is ",list(q.queue)[0] )
            else:
                print()
                print(k, end="")
                print("th to last element is ")
                print(list(q.queue)[0])
    def Main(self):
            while (True):
                print("Welcome to the linked list problem solver")
                print("Options = ")
                print("1 - Add to linked list --- urlifys a given string")
                print("2 - Print List --- determines if a string is one edit distance away from another string")
                print("3 - Remove Dups --- removes duplicates from a list")
                print("4 - Delete linked list node --- determines if a string could be a palindrome")
                print("5 - Kth to last --- determines if a string is a permutation of another string")
                print("6 - Search for element --- determines if a string is one edit distance away from another string")
                print("E - Exit ")
                optdict = {"5": self.kth_to_last, "3": self.remove_dups, "1": self.insert, "4": self.delete,
                           "2": self.print_all,"6":self.search, "E": self.Exit}
                option = input("Pick an option = ")
                while option not in optdict.keys():
                    print("Invalid Option try again!")
                    option = input("Pick an option =  ")
                optdict[option]()


ll = Linked_List()
ll.Main()
