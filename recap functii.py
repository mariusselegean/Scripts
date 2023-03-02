def calculator():
    result = 2 * 4 - 5 * 3
    return result

restult_after_call = calculator()
print(restult_after_call)

def calculator(nr1, nr2):
    # nr1 = 5
    # nr2 = 6
    result = 2 * nr1 - 5 * nr2
    return result

restult_after_call = calculator(5, 6) # nr1 = 5 si nr2 = 6
print(restult_after_call)


def raise_power(val1, val2):
    """
    functia ridica un numar val1 la puterea altui numar, val2
    :param val1:
    :param val2:
    :return:
    """
    result = int(val1) ** int(val2) # val transformat in integer
    return result

result = raise_power(input("Enter number..."), input("Raise to?   ")) # input pentru valorile val 1 si val 2
print(result)












