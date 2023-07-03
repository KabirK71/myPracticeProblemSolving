# The problem here is form leet code.
# Input is in a list of integers and you have to find 2 numbers from this list that add up to the target value.
# The output should be the indexes of the 2 numbers.

# I solved it ny brute force. O(n^2)
# A better method will be using hashmap. O(n). However takes more space.
# Hashmap makes the searching from O(n) to 0(1). Resulting in overall time complexity to be 0(n).


def twoSum(nums: List[int], target: int) -> List[int]:
    hashmap = {}  # declaring a dictionary to make a hasmap.
    for i in range(len(nums)):
        # inputing each number into the hashmap as the key and its index as value
        hashmap[nums[i]] = i

    for i in range(len(nums)):
        # complement is basically the second number needed to form the pairof numbers that add up to target.
        complement = target - nums[i]
        # checking if the complement exists in the hashmap for that number and if it isnt the same number.
        if complement in hashmap and hashmap[complement] != i:
            # if yes return the number and its complement to make the pair.
            return [i, hashmap[complement]]
