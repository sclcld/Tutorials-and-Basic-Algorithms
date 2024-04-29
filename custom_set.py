class CustomSet:
   
    def __init__(self, elements=[]):
        
        self._data = {elem : None for elem in elements}


    @property
    def data(self):

        return self._data.keys()


    def isempty(self):

        return not self.data


    def __contains__(self, element):

        return element in self.data


    def issubset(self, other):

        if isinstance(other, CustomSet):

            return all([el in other.data for el in self.data])
        
        #raise TypeError(f"Unsupported type {type(other)}")
    
    def isdisjoint(self, other):

        if isinstance(other, CustomSet):

            return all([el not in other.data for el in self.data])

        #raise TypeError(f"Unsupported type {type(other)}")
    
    def __repr__(self):

        return str(self.data)            

    def __eq__(self, other):

        if isinstance(other, CustomSet):

            return self.data == other.data
    
    def add(self, element):

        self._data[element] = None
    
    def intersection(self, element):

        if isinstance(element,CustomSet):

            return CustomSet(self.data & element.data)


    def __sub__(self, other):
        
        if isinstance(other, CustomSet):

            return CustomSet(self.data - other.data)

    def __add__(self, other):
        
        if isinstance(other, CustomSet):

            return CustomSet(self.data | other.data)


                
            
            

a = {1,2,4}
b={4,5,6}

e = a | b

print(e)