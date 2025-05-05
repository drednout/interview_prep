# Goal: put all the zeros at the end of the list.
# The function below works but it's too slow. Can you make it faster?

# Example In: [1, 0, 2, 3, 0]
# Out [1, 2, 3, 0, 0]

# Can we create one more list or it should be done in place?
# => Let's try to optimize using extra list

# Example 2: [0, 0, 1, 3, 2, 0]
# Out: [1, 3, 2, 0, 0, ]

def solution_with_extra_list(nums):
    out_list = []
    zero_count = 0

    for n in nums:
        if n == 0:
            zero_count += 1
        else:
            out_list.append(n)

    return out_list + [0]*zero_count

def solution_with_extra_list_short(nums):
    orig_len = len(nums)
    nums = [n for n in nums if n != 0]
    return nums + [0] * (orig_len - len(nums))


def solution_with_write_pointer(nums):
    write_pointer = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[write_pointer], nums[i] = nums[i], nums[write_pointer]
            write_pointer += 1

    return nums
