import ast


class Equation:

    def __init__(self, string, func_get_constants_values):
        self.constants = []
        self.eval_eq_string = ""
        self.func_get_constants_values = func_get_constants_values

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

        eval_eq_string = string.split("=")[1]

        self.constants = [node.id for node in ast.walk(ast.parse(string))
            if type(node) is ast.Name]

        self.constants.pop(0)  # Remove the dependent variable

        f_string_l = list(eval_eq_string)

        start_index = 0

        while start_index < len(f_string_l):
            
            if f_string_l[start_index].isalpha():
                stop_index = start_index

                while stop_index < len(f_string_l) and f_string_l[stop_index].isalpha():
                    stop_index += 1

                f_string_l.insert(start_index, "{")
                f_string_l.insert(stop_index + 1, "}")

                start_index = stop_index + 2

            else:
                start_index += 1

        self.f_eval_eq_string = "".join(f_string_l).lstrip()
        
    def get_constants(self):
        return self.constants

    def solve(self, **variables):
        kwargs = dict(zip(self.constants, self.func_get_constants_values()))
        kwargs.update(variables)

        eval_string = self.f_eval_eq_string.format(**kwargs)

        print(self.f_eval_eq_string, eval_string, sep = "\n")

        return eval(eval_string)
