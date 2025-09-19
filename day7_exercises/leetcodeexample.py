class Solution(object):
    def firstuniqchar(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq={}
        for char in s:
            freq[char]=freq.get(char,0)+1

        for i,char in enumerate(s,start=0):
            if freq[char]==1:
                return i
        return -1
# Run tests
sol = Solution()
print(sol.firstuniqchar("loveleetcode"))  # 2
print(sol.firstuniqchar("leetcode"))      # 0
print(sol.firstuniqchar("aabb"))          # -1