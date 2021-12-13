from typing import List


def get_two_sum_indexes(nums: List[int], target: int) -> List[int] | None:
    """
    Returns the list of two indexes of the two
    numbers such the add up to target
    """
    checked_nums = {}

    for index, value in enumerate(nums):
        check = target - value

        if check in checked_nums:
            return [ checked_nums[check], index]

        checked_nums[value] = index
