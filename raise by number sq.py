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