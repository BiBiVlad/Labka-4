num = input()
nums = num.split()
nums = list(map(int, nums))
n = len(nums)
def is_monotonic(nums):
    i = 1
    counter = 0
    for i in range(1,n):
        if min(nums) == nums[0]:
            if nums[i] >= nums[i-1]:
                continue
            else:
                counter += 1
        elif max(nums) == nums[0]:
            if nums[i] <= nums[i-1]:
                continue
            else:
                counter += 1
        else:
            print("False")
    if counter == 0:
        print("True")
    else:
        print("False")
    return ""

print(is_monotonic(nums))