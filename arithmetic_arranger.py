def arithmetic_arranger(operations, show_result=False):
    
    # LISTS

    operands_1 = []
    operands_2 = []
    operators = []
    space_1 = []
    space_2 = []
    dashes = []
    results = []
    line_1 = []
    line_2 = []
    problems_space = "    "

    # ERRORS

    if len(operations) > 5:
        return "Error: Too many problems."

    for problem in operations:
        if "+" in problem:
            operators.append("+")
            operands_1.append(problem.split(" + ")[0])
            operands_2.append(problem.split(" + ")[1])
        elif "-" in problem:
            operators.append("-")
            operands_1.append(problem.split(" - ")[0])
            operands_2.append(problem.split(" - ")[1])
        else:
            return "Error: Operator must be '+' or '-'."

    for item in operands_1:
        try:
            int(item) % 1
        except ValueError:
            return "Error: Numbers must only contain digits."
        if len(item) > 4:
            return "Error: Numbers cannot be more than four digits."

    for item in operands_2:
        try:
            int(item) % 1
        except ValueError:
            return "Error: Numbers must only contain digits."
        if len(item) > 4:
            return "Error: Numbers cannot be more than four digits."

    # STRUCTURE
    
        # SPACES, LINES & RESULTS
    for index, operand in enumerate(operands_1):
        if len(operand) >= len(operands_2[index]):
            space_1.append(2 * " ")
            space_2.append(" " * ((len(operand) - len(operands_2[index])) + 1))
        elif len(operand) == 1:
            space_1.append(" " * (len(operands_2[index]) +1))
            space_2.append(" ")
        else:
            space_1.append(" " * len(operands_2[index]))
            space_2.append(" ")
    
        if len(operand) >= len(operands_2[index]):
            dashes.append("-" * (len(operand) + 2))
        else:
            dashes.append("-"  * (len(operands_2[index]) + 2))

        if operators[index] == "+":
            results.append(str(int(operand) + int(operands_2[index])))
        elif operators[index] == "-":
            results.append(str(int(operand) - int(operands_2[index])))

        # CONSTRUCTING LINES
    for index, operand in enumerate(operands_1):
        line_1.append(space_1[index] + operand)
        line_2.append(operators[index] + space_2[index] + operands_2[index])
        while len(line_1[index]) > len(results[index]) or len(line_2[index]) > len(results[index]):
            results[index] = " " + results[index]

    # FINAL LINES & RETURNING

    if show_result == True:
        return problems_space.join(line_1) + "\n" + problems_space.join(line_2) + "\n" + problems_space.join(dashes) + "\n" + problems_space.join(results)
    
    return problems_space.join(line_1) + "\n" + problems_space.join(line_2) + "\n" + problems_space.join(dashes)

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
