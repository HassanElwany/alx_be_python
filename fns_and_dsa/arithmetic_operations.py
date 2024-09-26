def perform_operation(num1, num2, operation):
    # match operation:
    #     case 'add':
    #         return num1 + num2
    #     case 'subtract':
    #         return num1 - num2
    #     case 'multiply':
    #         return num2 * num1
    #     case 'divide':
    #         try:
    #             return num1 / num2
    #         except ZeroDivisionError():
    #             return f"Can not divide by Zero!"
    #     case _:
    #         return f"something went wrong"
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return f"Invalid divide zero divide"
        else:
            return num1 / num2