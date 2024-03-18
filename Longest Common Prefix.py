class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        L_G_P = strs[0]
        min_length = float("inf")
        for i in strs:
            #for j in i:
            length = min(len(L_G_P), len(i))
            while L_G_P[0:length] != i[0:length] :
                length -= 1
                if length == 0:
                    return ""
            min_length = min(min_length, length)
        return L_G_P[0:min_length]
