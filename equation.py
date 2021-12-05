import ast, math


class Equation:

    CONSTANTS_TO_IGNORE = ["x", "y"]

    def __init__(self, string, error_msg_func):
        self.constants = []
        self.expression = ""
        self.f_expression = ""
        self.constants_values = {}

        self.error_message_func = error_msg_func

        self.evaluate_string(string)
    
    def evaluate_string(self, expression):

        self.expression = expression.strip()

        if "=" in self.expression:
            self.error_message_func("Expression cannot have '=' symbol.")
            return

        try:
            self.error_message_func()
            self.constants = []
            for node in ast.walk(ast.parse(self.expression)):
                if type(node) is ast.Name and node.id not in self.constants:
                    self.constants.append(node.id)
            
        except:
            self.error_message_func("Invalid expression.")
            return

        index = 0
        while index < len(self.constants):
            if hasattr(math, self.constants[index]) or self.constants[index] in self.CONSTANTS_TO_IGNORE:
                self.constants.pop(index)

            else:
                index += 1

        f_string_l = list(self.expression)

        start_index = 0

        while start_index < len(f_string_l):
            
            if f_string_l[start_index].isalpha():
                stop_index = start_index

                while stop_index < len(f_string_l) and f_string_l[stop_index].isalnum():
                    stop_index += 1

                constant_name = "".join(f_string_l[start_index: stop_index])
                if hasattr(math, constant_name):
                    f_string_l.insert(start_index, "math.")
                else:
                    f_string_l.insert(start_index, "{")
                    f_string_l.insert(stop_index + 1, "}")

                start_index = stop_index + 2

            else:
                start_index += 1

        self.f_expression = "".join(f_string_l).lstrip()
        
    def get_constants(self):
        return self.constants

    def update_constants_values(self, constants_values, ):
        self.constants_values = constants_values

    def solve(self, **variables):

        # Adding constant values from self.constants_values for variable names not in variables
        for key, val in self.constants_values.items():
            if key not in variables:
                variables[key] = val

        eval_string = self.f_expression.format(**variables)

        #print(self.f_expression, eval_string, sep = "\t:\t")

        try:
            val = eval(eval_string)
        
        except:
            return False

        if type(val) not in [int, float]:
            return False

        return val
