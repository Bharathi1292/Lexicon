# Global variable
text = "I am Bharathi Dibbidi."

def show_text():
    # Local variable
    message = "I changed my name, Bharathi Makireddy."
    print("Inside the function:", message)

print("Outside the function:", text)
show_text()

print("Outside the function again:", text)
