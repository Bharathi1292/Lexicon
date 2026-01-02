def length(obj):
    return len(obj)  

text = "This is Python program"
print("Length of the text is: ", length(text))

class Message:
    def __init__(self, msg):
        self.msg = msg

    def __len__(self):
        return len(self.msg)

m = Message("I am learning Python")
print("Length of the text is: ", length(m))

