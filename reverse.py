class Solution(object):

    def swap(self, s, l, r):
        temp = s[r]
        s[r] = s[l]
        s[l] = temp

    def reverseString(self, s):
        l = 0
        r = len(s) - 1
        while r > l:
            self.swap(s, l, r)
            l += 1
            r -= 1


s = list(input("Enter the string to be reversed:"))

sol = Solution()
sol.reverseString(s)


print("Reversed string is", ''.join(s))
