"""
    Functions and scope
"""


# Without parameters and without return
def hi() -> None:
    print("Hi, im a function")


hi()
###############################################################


# With parameters but without return
def hi_with_name(nombre: str) -> None:  # nombre es un parámetro
    print(f"Hi, {nombre}")


hi_with_name("Emmanuel")  # Emmanuel es un argumento
###############################################################


# With parameters and with return
def sumar(a: int, b: int) -> int:
    return a + b


suma = sumar(2, 3)
print(suma)
###############################################################


# Inner functions abd optional parameters
def function1() -> None:
    print("Function 1")

    def function2(
        string: str = "lol",
    ):  # Function inside a function with optional parameter
        print(
            f"Function 2: {string.upper()}"
        )  # Built-in functions by the Python language (print, upper, etc.)

    function2("Hello World")
    function2()


function1()
###############################################################

# Lambda functions
# lambda parameters: return
sumar = lambda a, b: a + b
print(sumar(2, 3))

###############################################################

# Variable scope
var = 10


def function3() -> None:
    global var  # Global variable, not recommended
    var = 40  # Local variable


function3()

print(var)


def function4() -> None:
    var = 20  # Local variable
    print(var)


function4()
print(var)
###############################################################


# Challenge
def challenge(text1: str, text2: str) -> int:
    times_number_is_printed: int = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{text1}{text2}")
        elif i % 3 == 0:
            print(text1)
        elif i % 5 == 0:
            print(text2)
        else:
            print(i)
            times_number_is_printed += 1
    return times_number_is_printed


print(f"Result is => {challenge("Fizz", "Buzz")}")
###############################################################
