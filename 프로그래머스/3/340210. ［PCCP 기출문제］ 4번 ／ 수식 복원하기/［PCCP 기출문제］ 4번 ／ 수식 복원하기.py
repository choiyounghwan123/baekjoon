# [PCCP] 수식 복원하기.

def tenToN(n, num):
    if num == 0: return "0"
    answer = ""

    for idx in range(2, -1, -1):
        div = num // (n ** idx)
        if answer or div: answer += str(div)
        num = num % (n ** idx)

    return answer


def solution(expressions):
    hint,answer,answer_format = [],[],[]
    max_format = 0
    for expression in expressions:
        operand1,operator,operand2,_,result = expression.split(" ")

        for i in range(len(operand1)):
            max_format = max(max_format, int(operand1[i]))
        for i in range(len(operand2)):
            max_format = max(max_format, int(operand2[i]))
        if result != 'X':
            hint.append(expression)
            for i in range(len(result)):
                max_format = max(max_format, int(result[i]))
        else:
            answer.append(expression)

    for i in range(max_format+1,10):
        for hint_expression in hint:
            operand1, operator, operand2, _, result = hint_expression.split(" ")
            if operator == "+" and int(operand1, i) + int(operand2, i) != int(result, i):
                break
            elif operator == "-" and int(operand1, i) - int(operand2, i) != int(result, i):
                break
        else:
            answer_format.append(i)
    print(answer_format)
    a = []
    for answer_ in answer:
        b = set()
        operand1, operator, operand2, _, result = answer_.split(" ")
        for i in answer_format:
            print(operand1, int(operand1, i), int(operand2, i))
            if operator == "+":
                b.add(tenToN(i,int(operand1,i) + int(operand2,i)))
            else:
                b.add(tenToN(i,int(operand1,i) - int(operand2,i)))
        if len(b) > 1:
            a.append(f"{operand1} {operator} {operand2} = ?")
        else:
            a.append(f"{operand1} {operator} {operand2} = {list(b)[0].split(' ')[0]}")
    return a


print(solution(["11 + 1 = 12", "12 + 1 = 13", "13 + 1 = X"]
))
