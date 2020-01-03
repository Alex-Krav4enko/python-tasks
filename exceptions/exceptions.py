input_exp = input('Введите выражение: ')

g_funcs = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b
}


def postfix_calc(exp):
    stack = exp.split(' ')
    operator = stack[0]
    try:
        assert len(stack) == 3, 'Вы ввели некорректное выражение'
        assert operator in ['+', '-', '/', '*'], 'Введенный оператор недопустим'
        a = int(stack[1])
        b = int(stack[2])
        res = g_funcs[operator](a, b)
    except (AssertionError, ZeroDivisionError, IndexError, ValueError) as e:
        print(f'Exception: {e.args[0]}')
    except Exception as e:
        print(f'Unexpected error {type(e)}')
    else:
        print(res)


postfix_calc(input_exp)
