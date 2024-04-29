class LinkedList:

    #Class Node
    class Node:

        def __init__(self, data) -> None:
            self._data = data
            self._next = None

        @property
        def data(self):

            return self._data
        
        @property
        def next(self):

            return self._next
        
        def __str__(self) -> str:

            return str(self.data)
        
        def set_next(self, node):

            self._next = node

    #Linked List __init__
    def __init__(self, obj = None) -> None:
        
        self._head = None
        self._size = 0
        self.ll_init(obj)
    
    def ll_init(self, obj):

        if obj:
            if isinstance(obj, dict):
                obj = list(obj.keys())
            if isinstance(obj, (list, tuple, set, LinkedList)):
                self.fill(obj)
            else:
                self.push(obj)

    def fill(self, iter):

        for obj in iter:
            self.push(obj)

    @property
    def head(self):

        return self._head    
    
    def __str__(self):

        string = ""
        separator = ", "
        current = self.head
        while current:
            string += str(current) + separator
            current = current.next 
        
        return f"[{string.strip(separator)}]"
    
    def __iter__(self):

        current = self.head
        while current:
            yield current.data
            current = current.next
    
    def __len__(self):

        return self._size 
    
    def __getitem__(self, index):

        if isinstance(index, slice):
            start = index.start or 0
            stop = index.stop or self.__len__()
            step = index.step or 1
            if 0 <= start <= stop <= self.__len__():
                i = start
                ll_slice = []
                while i < stop:
                    ll_slice.append(self[i])
                    i += step
                if not ll_slice:

                    return LinkedList([self[i]])
                
                return LinkedList(ll_slice).reverse()
            
            raise ValueError(f"Index out of range")
        
        i = 0
        current = self.head
        while i < index:
            current = current.next
            i += 1

        return current.data

    def reset(self):

        self._head = None
        
    def reverse(self):

        return LinkedList(self)
    
    def push(self, obj):

        node = self.Node(obj)
        
        if not self.head:
            self._head = node
        else:
            node.set_next(self._head)
            self._head = node
        
        self._size += 1

        return True

    def pop(self, index = 0):

        popped_obj = None
        if self.head:
            if not index:
                popped_obj = self.head.data
                self._head = self.head.next 
            elif index in range(1,self.__len__()):
                i = 0
                new_ll = LinkedList()
                current = self.head
                while i < index:
                    new_ll.push(current)
                    current = current.next
                    i += 1 
                popped_obj = current.data
                current = current.next
                while current:
                    new_ll.push(current)
                    current = current.next
                    i += 1
                self._head = LinkedList(new_ll)._head
            else: 

                raise ValueError("Inserted index is out of range") 
            
            self._size -= 1

            return popped_obj
        
        raise ValueError("LinkedList is empty")   

    def values(self):
        
        values = []

        return [val for val in self]

    def clean(self):
        
        clean_list = []
        for value in self.values():
            if value not in clean_list:
                clean_list.append(value)
        
        return LinkedList(clean_list).reverse()       

    def sort(self):

        return LinkedList(sorted(self.values(), reverse= True))  
    

a = LinkedList([0,1,2, 7,8,3,4,5,6, 6, 3,4,5])
b = LinkedList(a)
print(b)
print(b.sort())



