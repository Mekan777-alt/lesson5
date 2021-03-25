
def odd_nums(nums):

    gen_cis = (el for el in range(0, nums + 1) if el % 2 != 0)
    for el in gen_cis:
        yield el


odd_to_25 = odd_nums(25)
print(next(odd_to_25))
print(next(odd_to_25))
print(next(odd_to_25))
print(next(odd_to_25))
print(next(odd_to_25))
print(next(odd_to_25))
print(next(odd_to_25))
print(next(odd_to_25))
print(next(odd_to_25))
print(next(odd_to_25))
print(next(odd_to_25))
print(next(odd_to_25))
print(next(odd_to_25))
print(next(odd_to_25))
