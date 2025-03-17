#Evaluates operand values to ensure they are greater than zero

class Validator:
    @staticmethod
    def validate(value, msg):
        if value == 0:
            raise ValueError(msg)