def make_uppercase(func):
    def wrapper():
        result = func()          
        return result.upper()    
    return wrapper

@make_uppercase
def get_message():
    return "wlcome to the python programming world"

print(get_message())
