def perform_operation(num1,num2,operation):
    if operation == "add":
        answer = num1 + num2

    elif operation == "subtract":
        answer = num1 - num2
    elif operation == "divide":
        if num2 ==0:
            answer ="Division by zero is not possible"
        else:
            answer = num1 / num2
    else:
        answer = num1 * num2
    return answer