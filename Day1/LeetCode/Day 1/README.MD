# 📅 Day 1: Two Sum & Core Logic Building

## 🚀 Challenge Overview

Today marks the beginning of my 90-Day AI/ML Engineering Journey. I'm starting with a powerful logic-building problem: **Two Sum** — one of the most frequently asked interview questions at companies like Google, Amazon, and Meta.

## 🎯 Problem Statement

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

* You may assume that each input has exactly one solution.
* You cannot use the same element twice.

## ✅ Concepts Covered

* Arrays (Lists in Python)
* Hash Maps (Dictionaries)
* Single-pass Search
* Complementary Value Logic
* Time Complexity Optimization (O(n) vs O(n^2))
* Python's `enumerate()` and `dict` usage

## 🧠 Key Learning

Instead of using nested loops (O(n^2)), we used a hash map to track seen numbers and solve the problem in **O(n)** time. This same logic appears in:

* Feature matching
* Recommendation systems
* Real-time fraud detection
* AI systems that need fast lookups

## 📁 Files

* `day1_two_sum.py`: Full Python code with detailed comments and test cases

## 🧪 Sample Test Case

```python
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: Because nums[0] + nums[1] == 9
```

## 🛠️ Code Summary

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in numbers_map:
                return [numbers_map[complement], i]
            numbers_map[num] = i
        return []
```

## 🧩 What's Next (Day 2 Preview)

* Continue with LeetCode logic: "Best Time to Buy and Sell Stock"
* Deepen Linear Algebra with vector operations
* Intro to gradients (foundation for neural networks)

---

Stay consistent. Think like a system. Build like a pro.

🧠 Learn. 🔨 Build. 🚀 Repeat.
