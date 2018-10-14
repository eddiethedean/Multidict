class Multidict:
    """Class that behaves like a dictionary that can hold multiple values for each key"""
    def __init__(self, iterable=(), **kwargs):
        self.md = {}
        self.update(iterable, **kwargs)
        
    def __repr__(self):
        return str(self.md)
        
    def __getitem__(self, key): #to get a value by its key
        return self.md[key]
        
    def __setitem__(self, key, value): #to set a value by its key
        if key in self:
            self.md[key].append(value)
        else:
            self.md[key] = [value]
            
    def __delitem__(self, key): #to delete a key-value pair
        if key in self:
            if len(self[key])>1:
                del self[key][0]
            else:
                self.md.pop(key)
    
    def delete_key(self, key):
        self.md.pop(key)
                
    def __missing__(self, nonexistent_key): #to provide a default value for missing keys
        return -1
    
    def __contains__(self, key):
        return key in self.md
    
    def __len__(self):
        """len() returns number of different values"""
        return len(self.values())
    
    def update(self, iterable=(), **kwargs):
        """add kwargs or tuple iterable"""
        if iterable:
            if type(iterable)==dict:
                iterable = iterable.items()
            for key,val in iterable:
                self[key] = val
                
        if kwargs:
            for key,val in kwargs.items():
                self[key]=val
                
    def append(self, multidict):
        """combine another multidict"""
        self.update(multidict.items())
        
    def pop(self, key):
        if key in self:
            temp = key, self[key][0]
            del self[key]
            return temp
        
    def pop_key(self, key):
        if key in self:
            temp = key, self[key]
            self.md.pop(key)
            return temp

    def items(self):
        return [(key, item) for key, val in self.md.items() for item in val]

    def keys(self):
        return self.md.keys()
    
    def values(self):
        return [item for val in self.md.values() for item in val]
    
    def clear(self):
        self.md = {}
    
    def get_first(self, key):
        """returns first value for key"""
        return self[key][0]
    
    def get_last(self, key):
        """returns last value for key"""
        return self[key][-1]
    
    def count(self, key):
        """returns number of values for key"""
        return len(self[key])
        
if __name__=='__main__':
    new_d = Multidict([('cat','Nova'),('cat','Zora'),('dog','Nami')])
    new_d = Multidict(cat='Nova',dog='Nami')
    new_d['cat']='Zora'
    new_d.update([('human','Odos')])
    new_d.update(human='Odos')
    new_d.update(human='Kayla')
    print(new_d.items())
    print(new_d.values())
    print(new_d)
    print('pop', new_d.pop('cat'))
    print(new_d)
    print('pop', new_d.pop('cat'))
    print(new_d)
    print(len(new_d))

    sec_d = Multidict(ape='bob', lizard='godzilla')
    new_d.append(sec_d)
    print(new_d)
    print(new_d.get_first('human'))