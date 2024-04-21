class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_orders = set()
        for num in nums:
            if num not in unique_orders:
                unique_orders.add(num)
        nums[:] = sorted(unique_orders)
        return len(nums)