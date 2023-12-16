## Linked List ##

list_ex = [34, 67, 89, 90]

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_List:

    def __init__(self):

        self.head = None
    
    def insert_at_beggining(self, data):

        node = Node(data=data)
        if self.head is None:
            self.head = node
            return 
        else:
            node.next = self.head
            self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data=data)
            return 
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data=data)

    def insert_list(self, data_list):
        for data in data_list:
            self.insert_at_end(data=data)
    
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count = count + 1
            itr = itr.next
        print(count)

    def insert_at (self, data, idx_no):
        itr = self.head 
        count = 0
        while itr:
            count = count + 1
            if count == idx_no - 1:
                node = Node(data=data)
                itr.next = node
                break
            itr = itr.next

    def print_all(self):
        if self.head is None:
            print("Linked List is Blank !")
        itr = self.head 
        ll_str = ""

        while itr:
            ll_str += str(itr.data) +' --> '
            itr = itr.next
        print(ll_str)

if __name__ == '__main__':

    linked_list = Linked_List()
    linked_list.insert_at_beggining(data=56)
    linked_list.insert_at_beggining(data=32)
    linked_list.insert_at_end (data=120)
    linked_list.insert_at_beggining (data=767)
    linked_list.insert_list(list_ex)
    linked_list.insert_at (data=4656, idx_no=3)
    linked_list.insert_at (data=89, idx_no=4)
    linked_list.get_length()
    linked_list.print_all()