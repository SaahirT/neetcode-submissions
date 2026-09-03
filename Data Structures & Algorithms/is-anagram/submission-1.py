class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # gets the counts of each letter in the first word
        counts = {}
        for char in s:
            if char not in counts:
                counts[char] = 1
            else:
                counts[char] += 1

        
        for char in t:
            # if a letter in the second word isn't in counts, then anagram is false
            if char not in counts:
                return False
            # otherwise subtract an occurrence of that letter from counts
            else:
                counts[char] -= 1

        for key in counts:
            if counts[key] != 0:
                return False

        return True

        