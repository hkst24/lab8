# функция сортировки пузырьком
def BubbleSort(arr):
    if not isinstance(arr, list):
        raise Exception('Not list')
    elif len(arr) == 0:
        raise Exception('Empty list')
    for el in arr:
        if not isinstance(el, int):
            raise Exception('Not int')
        
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# функция выявления палиндрома
def palindrome(string):
    if not isinstance(string, str):
        raise Exception('Not str')
    
    if string == string[::-1]:
        return True
    else:
        return False

# функция нахождения факторила       
def factorial(n):
    if not isinstance(n, int)  or n < 0:
        raise Exception('Not int')
    
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# функция нахождения числа Фибоначчи
def fibonacci(position):
    f = False
    if not isinstance(position, int):
        raise Exception('Not int')
    if  position < 0:
        if position % 2 == 0:
            f = True
        position *= -1
        
    if position == 1:
        return 0
    elif position == 2:
        return 1
    else:
        fib_minus_2 = 0
        fib_minus_1 = 1
        fib_current = 0
        for i in range(2, position + 1):
            fib_current = fib_minus_2 + fib_minus_1
            fib_minus_2 = fib_minus_1
            fib_minus_1 = fib_current
        if f:
            return fib_current * -1
        else:
            return fib_current
        
# функция возведения в степень
def exponent(num, exp):
    if not isinstance(num, float) and not isinstance(num, int):
        raise Exception('Not float')
    if not isinstance(exp, float) and not isinstance(exp, int):
        raise Exception('Not float')
        
    result = pow(num, exp)
    return result

# функция проверки на простое число
def simple(number):
    if not isinstance(number, int):
        raise Exception('Not int')
    
    if number <= 0:
        return False
    for i in range(2, int(pow(abs(number), 0.5)) + 1):
        if int(number) % i == 0:
            return False
    return True
