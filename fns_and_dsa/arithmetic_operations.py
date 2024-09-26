def perform_operation(num1, num2, operation):
    match operation:
        case 'add':
            return num1 + num2
        case 'subtract':
            return num1 - num2
        case 'multiply':
            return num2 * num1
        case 'divide':
            try:
                return num1 / num2
            except ZeroDivisionError():
                return f"Can not divide by Zero!"
        case _:
            return f"something went wrong"