class Multidict:
    
    def __init__(self, iterable=(), **kwargs):
        self.md = {}
        self.update(iterable, **kwargs)
    
    def update(self, iterable=(), **kwargs):
        if iterable:
            if type(iterable)==dict:
                iterable = iterable.items()
            for key,val in iterable:
                self[key] = val
                
        if kwargs:
            for key,val in kwargs.items():
                self[key]=val
                
    def append(self, iterable=(), **kwargs):
        self.update(iterable, **kwargs)
        
    def __repr__(self):
        return str(self.md)
        
    def __getitem__(self, key): #to get a value by its key
        return self.md[key]

    def generate_item(self, key): #generator to get the next key
        for value in self.md[key]:
            yield value
        
    def __setitem__(self, key, value): #to set a value by its key
        if key in self:
            self.md[key].append(value)
        else:
            self.md[key] = [value]
                
    def __missing__(self, nonexistent_key): #to provide a default value for missing keys
        pass
    
    def __contains__(self, key):
        return key in self.md

    def pop(self, key):
        if key in self:
            temp = key, self[key][0]
            del self[key]
            return temp

    def __delitem__(self, key): #to delete a key-value pair
        if key in self:
            if len(self[key])>1:
                del self[key][0]
            else:
                self.md.pop(key)
                
    def items(self):
        return [(key, item) for key, val in self.md.items() for item in val]

    def keys(self):
        return self.md.keys()
    
    def values(self):
        return [item for val in self.md.values() for item in val]
    
    def clear(self):
        self.md = {}
        
    def __len__(self):
        return len(self.values())
    
    #creates a new Multidict with keys from seq and values set to value.
    #def fromkeys(self, seq, value)
        #return Multidict([(key,value) for key in seq])
        
        
new_d = Multidict([('cat','Nova'),('cat','Zora'),('dog','Nami')])
new_d = Multidict(cat='Nova',dog='Nami')
new_d['cat']='Zora'
new_d.append([('human','Odos')])
new_d.append(human='Odos')
new_d.append(human='Kayla')
print(new_d.items())
print(new_d.values())
print(new_d)
print('pop', new_d.pop('cat'))
print(new_d)
print('pop', new_d.pop('cat'))
print(new_d)
print(len(new_d))

#second = new_d.fromkeys