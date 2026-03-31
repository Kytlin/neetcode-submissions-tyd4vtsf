class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if max(nums) < 0:
            return []
        nums.sort()
        print(nums)

        res = []
        cur_num = 1
        for i, first_num in enumerate(nums):
            if first_num <= 0 and cur_num != first_num:
                cur_num = first_num
                start, end = i+1, len(nums)-1
                while start < end:
                    if nums[start] + nums[end] + first_num > 0:
                        end -= 1
                    elif nums[start] + nums[end] + first_num < 0:
                        start += 1
                    else:
                        if [nums[start], nums[end], first_num] not in res:
                            res.append([nums[start], nums[end], first_num])
                        start += 1
                        end -= 1
            elif cur_num == first_num:
                continue
            else:
                break

        return res