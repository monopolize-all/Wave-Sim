import ast
import math


class Equation:

    CONSTANTS_TO_IGNORE = ["x"]

    def __init__(self, string):
        self.constants = []
        self.dependent_variable = ""
        self.expression = ""
        self.f_expression = ""
        self.constants_values = {}
        self.solveable = False
        self.all_constants_present = False

        self.evaluate_string(string)
    
    def evaluate_string(self, string):
        """
        raw_string = "".join([char for char in string if not char.isspace()])

        len_raw_string = len(raw_string)

        print(raw_string)

        self.result = raw_string[0]

        if raw_string[1] != "=":
            raise Exception("2nd character is not '='")

        self.constants = []
        """

        self.dependent_variable, self.expression = string.split("=")

        self.dependent_variable = self.dependent_variable.strip()

        self.expression = self.expression.strip()

        try:
            self.constants = []
            for node in ast.walk(ast.parse(string)):
                if type(node) is ast.Name and node.id not in self.constants:
                    self.constants.append(node.id)
                    

            #self.constants = [node.id for node in ast.walk(ast.parse(string))
                #if type(node) is ast.Name]
            
            self.solveable = True
            
        except:
            self.solveable = False
            return
        
        self.constants.pop(0)  # Remove the dependent variable

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

    def update_constants_values(self, constants_values, all_constants_present = False):
        self.all_constants_present = all_constants_present
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

# y = a * sin(w1*t+k1*x+c1) + b * sin(w2*t+k2*x+c2) + 200
