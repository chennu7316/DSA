class Solution(object):
    def removeDuplicateLetters(self, s,i=0,ans='',fre=[False]*26):
        """
        :type s: str
        :rtype: str
        """
        if(i==len(s)):
            return ans
        if(fre[ord(s[i])-ord('a')]==False):
            ans=ans+s[i];
            fre[ord(s[i])-ord('a')]=True
        return self.removeDuplicateLetters(s,i+1,ans,fre)
