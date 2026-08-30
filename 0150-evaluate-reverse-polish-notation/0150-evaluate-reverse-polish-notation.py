class Solution:
    def evalRPN(self, tokens):
        stack = []

        for token in tokens:

            # Number
            if token not in "+-*/":
                stack.append(int(token))
                continue

            # Operator
            b = stack.pop()
            a = stack.pop()

            if token == "+":
                stack.append(a + b)

            elif token == "-":
                stack.append(a - b)

            elif token == "*":
                stack.append(a * b)

            else:
                # Division: truncate toward zero
                result = abs(a) // abs(b)

                if (a < 0) != (b < 0):
                    result = -result

                stack.append(result)

        return stack[-1]