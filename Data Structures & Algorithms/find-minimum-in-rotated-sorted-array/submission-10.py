class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1 or (nums[0] < nums[-1] and nums[0] < nums[1]):
            return nums[0]
        if nums[-1] < nums[-2] and nums[-1] < nums[0]:
            return nums[-1]
        
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right-left) // 2
            if nums[mid] < nums[mid-1] and nums[mid] < nums[mid+1]:
                return nums[mid]
            if nums[left] < nums[mid]:
                left = mid
            else: # left ptr has not jump past the min element
                right = mid
        return nums[left]