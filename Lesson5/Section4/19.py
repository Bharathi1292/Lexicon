class DictObject:
    def __init__(self, data):

        for key, value in data.items():
            setattr(self, key, value)  

    def __str__(self):
        
        return "\n".join([f"{key}: {value}" for key, value in self.__dict__.items()])

data = {"name": "Bharathi", "age": 33, "city": "Sweden"}
obj = DictObject(data)
print(obj)
