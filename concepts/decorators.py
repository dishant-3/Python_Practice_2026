## Closures

# def outer_function(msg):
#     def inner_function():
#         print(msg)
#     return inner_function
# hi_func= outer_function('Hi')  ## hi_func is a function variable we can execute
# bye_func= outer_function('Bye')

# hi_func()
# bye_func()


###### Decorators
## A decorator is a function that takes another function as an argument 
## Adds some kind of functionality and returns another function. Without altering the source code

def decorator_function(original_function):
    def wrapper_function(*args,**kwargs):
        print("Wrapper function executed before {}".format(original_function.__name__))
        return original_function(*args,**kwargs)
    return wrapper_function

def display():
    print("Display function ran")
## Underlying logic of decorator function
# decorated_display = decorator_function(display)
# decorated_display()

## General method for calling decorator function

@decorator_function
def display():
    print("Dispaly function ran")

display()

@decorator_function
def display_info(name,age):
    print(f"display_info ran with arguments {name} ,{age}")

display_info('John',25)

# A decorator in Python is a design pattern that allows a function or class to have its behavior extended or modified without directly changing its source code. Decorators essentially wrap the original function in a "wrapper" function that adds the extra functionality. 
# This is made possible because functions in Python are "first-class objects," meaning they can be passed as arguments to other functions, returned by functions, and assigned to variables.
