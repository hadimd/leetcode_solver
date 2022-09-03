import openai
from openai import Completion
import os

from openai.openai_object import OpenAIObject

openai_key: str = os.getenv('OPENAI_KEY', 'hadi no key')

openai.api_key = openai_key


def solve_leetcode_question(question: str) -> str:
    completion_object: Completion = Completion()
    leetcode_answer_object: OpenAIObject = completion_object.create(
        engine="code-davinci-002",
        prompt=f"""
Please write a Python Solution to the following Leetcode Question:
---
Leetcode Question:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
---        
Python Solution:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums: List[Tuple[int, int]] = sorted(enumerate(nums), key=lambda index_and_num: index_and_num[1])        
        left: int = 0
        right: int = len(sorted_nums) - 1
        
        while sorted_nums[left][1] + sorted_nums[right][1] != target:
            if sorted_nums[left][1] + sorted_nums[right][1] < target:
                left += 1
            else:
                right -= 1
        
        return [sorted_nums[left][0], sorted_nums[right][0]]
---
Leetcode Question:
{question}
---
Python Solution:
        """,
        max_tokens=600
    )
    leetcode_answer: str = leetcode_answer_object["choices"][0]["text"]
    return leetcode_answer