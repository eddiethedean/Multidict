class Multidict(dict):
    """Class that behaves like a dictionary that can hold multiple values for each key"""
    def update(self, iterable=(), **kwargs):
        """add kwargs or tuple iterable"""
        if iterable:
            if type(iterable) == dict:
                iterable = iterable.items()
            for key,val in iterable:
                self[key] = val
        if kwargs:
            for key,val in kwargs.items():
                self[key] = val

    def __init__(self, iterable=(), **kwargs):
        self.update(iterable, **kwargs)
        
    def __setitem__(self, key, value):
        if key in self:
            self[key].append(value)
        else:
            dict.__setitem__(self, key, [value])

    def __delitem__(self, key):
        if len(self[key]) > 1:
            del self[key][0]
        else:
            dict.__delitem__(self, key)
        
    def delete_key(self, key):
        pass
                
    def append(self, multidict):
        """combine another multidict"""
        self.update(multidict.items())
        
    def pop(self, key):
        if len(self[key]) > 1:
            temp = self[key][0]
            del self[key]
            return temp
        return dict.pop(self, key)

    def popitem(self, key=None):
        #if key == None:key = *last key*
        if len(self[key]) > 1:
            temp = key, [self[key][0]]
            del self[key][0]
            return temp
        return dict.popitem(self, key)

    def items(self):
        return [(key, item) for key, val in dict.items(self) for item in val]
    
    def values(self):
        return [item for val in dict.values(self) for item in val]
    
    def get_first(self, key):
        """returns first value for key"""
        return self[key][0]
    
    def get_last(self, key):
        """returns last value for key"""
        return self[key][-1]
        
if __name__=='__main__':
    new_d = Multidict([('cat','Nova'),('cat','Zora'),('dog','Nami')])
    print(new_d)
    new_c = Multidict(cat='Nova',dog='Nami')
    print(new_c)
    