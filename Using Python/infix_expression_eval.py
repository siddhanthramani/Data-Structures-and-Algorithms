from stack import Stack

# we create a dict to get the precedence weights of operators in O(1) time
precedence_dict = {
    "(": 0,
    ")": 0,
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2
}

# returns the precedence of the operator from the precedence dict only if the operator exists


def precedence(charact):
    try:
        return precedence_dict[charact]
    except:
        print('precedence test', charact)

# does the actual operation given two inputs and the operator


def operate_math(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b

# this function is called every time we run into an operator


def operate(val_op, operator_stack, operand_stack):
    # if the operator is the lower curly brace, we push it in and return
    if val_op == "(":
        operator_stack.push(val_op)
        return
    # if the operator is else,
    else:
        # gets the top operator of the operator_stack
        topOp = operator_stack.top()

        # till the precedence of the new op < the old op, we execute
        while precedence(val_op) <= precedence(topOp):
            print('removing top op')
            # we remove the top value, operate on operands and push the new operand back in
            topOp = operator_stack.pop()
            # to check if operator is NOT ')'
            if topOp in ["+", "-", "*", "/"]:
                top_val = operand_stack.pop()
                next_val = operand_stack.pop()

                # does the math
                fin_val = operate_math(next_val, top_val, topOp)
                # pushing back new value
                operand_stack.push(fin_val)
            elif topOp == '(':
                # this implies that the ( == ) in the previous while loop
                # hence we return after NOT pushing )  and popping (
                # if this was indeed the outermost (, the evaluation of expression is over
                return

            # gets the top operator of the operator_stack
            topOp = operator_stack.top()

        # pushing the new operator only after it obeys the precedence condition
        operator_stack.push(val_op)


def eval_exp(expression):
    exp_list = expression.split(' ')
    operator_stack = Stack()
    operand_stack = Stack()

    # the most external ( brakcet.
    operator_stack.push('(')

    # traversing each value in the expression assuming the expression is written with spaces
    for i in range(len(exp_list)):
        # gets the value of the operator or operand
        val_op = exp_list[i]

        # checks if value is operator or operand
        # precedence_dict thus plays dual role, for checking for key and getting precedence
        if val_op in precedence_dict:
            # if operator, we perform the operate function
            operate(val_op, operator_stack, operand_stack)
        else:
            # if operand, we push the float value to operand stack
            # we push float because we have to convert each value only once to float
            # and it becomes easy to do the math during retrieval
            operand_stack.push(float(val_op))
            #print("operand val", val_op)

        # for our reference, to check if the operator and operand stack are being written to
        # properly
        print("operator_stack")
        operator_stack.printStack()
        print("operand_stack")
        operand_stack.printStack()

    # this is the ending right curly bracket of expression
    operate(')', operator_stack, operand_stack)
    print("Answer   is ")
    # the final value of stack is returned
    return operand_stack.pop()


def main():
    expression = input("Enter a infix expresssion : ")
    print(eval(expression))
    print(eval_exp(expression))
    # print(precedence_dict[expression])


if __name__ == "__main__":
    main()
