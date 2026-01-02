def length(obj):
    return len(obj)

text = "Python Programming"
print("Length of text:", length(text))

class Message:
    def __init__(self, msg):
        self.msg = msg

    def __len__(self):
        return len(self.msg)

m = Message("Learning Duck Typing")
print("Length of message:", length(m))

number = 10   

print("Trying to get length of number...")
print(length(number))   

#The error occurs at runtime, when the function tries to execute 'len(obj)' on an object that does not implement __len__().
