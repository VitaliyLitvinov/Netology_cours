sum = 10
memory = [0] * sum
def can(sum):
    """ функция вычисляет возможно ли
    набрать поступившую на вход сумму
    монетами номаналом 5 и 3
    :param sum: int
    :return: bool
    """
    if memory[sum-1]:
        return memory[sum]
    if sum >= 3 and can(sum - 3):
        memory[sum-1] = True
        return True
    if sum >= 5 and can(sum - 5):
        memory[sum-1] = True
        return True
    memory[sum-1] = False
    return False
print(can(10))