
def tail(sequence, n):
    if n > 0:
        s = list(sequence)
        if len(s) - n <= 0:
            n = len(s)
        return s[len(s)-n:]
    else:
        return []

print(tail([1,2,3,4,5],3))
print(tail('hello', 2))
print(tail('hello',0))
print(tail('hello',-2))

squares = (n**2 for n in range(10))
print(tail(squares, 3))

nums = [1, 2, 3, 4]
print(tail(nums, -1))
print(tail((), -9))

print("BONUS 2")
nums = (n ** 2 for n in [1, 2, 3, 4])
print(tail(nums, -1), [])  # No looping when negative n given
print(tail(nums, 2), [9, 16])  # Generator consumed at this point
print(list(nums), [])  # The nums generator is now empty
print(tail(nums, 0), [])  # n=0 with empty generator
print(tail(nums, 1), [])  # n=1 with empty generator

print("test_n_larger_than_iterable_Length")
nums = [1, 2, 3, 4]
print(tail(nums, 5), [1, 2, 3, 4])
print(tail([], 10), [])