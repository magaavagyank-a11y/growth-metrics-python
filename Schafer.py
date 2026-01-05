def hello_func(greet,name = "You"):
    return '{},{}'.format(greet, name)
print(hello_func("Hello","John")) 
print(hello_func("Hello")) # Hello,You


def student_info(*args, **kwargs):
    print(args)      # кортеж позиционных аргументов
    print(kwargs)    # словарь именованных аргументов

student_info('Math', 'Art', name='John', age=22)
def greet_user(name, age):
    print(f"hello, {name}! You are {age} years old. Welcome to Growth engineering 🚀")

name = input("What is your name? ")
age = input("How old are you? ")
greet_user(name, age)

