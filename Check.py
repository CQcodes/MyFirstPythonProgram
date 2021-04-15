# validates user input
def IsNumber(input):
    try:
        # Convert it into integer
        val = int(input)
        return True
    except ValueError:
       return False