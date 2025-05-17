from Calck import result

def logger(func):
    def wrapper(expressions):
        result = func(expressions)
        print(f'[LOG] what : {expressions} = {result}')
        return result
    return wrapper

def safe_input(func):
    def wrapper(expressions):
        allowed = set('0123456789+-=*/().')
        if not set(expressions).issubset(allowed):
            raise ValueError('invalid input')
        return func(expressions)
    return wrapper

@logger

def calculate(expressions):
    return eval(expressions)

while True:
    try:
        expr=input('type another:')
        if expr == 'exit':
            break
        print('answer', calculate(expr))
    except Exception as e:
        print('error', e)