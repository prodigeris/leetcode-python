class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = {}
        t_dict = {}
        for cs, ct in zip(s, t):
            s_dict[cs] = s_dict.get(cs, 0) + 1
            t_dict[ct] = t_dict.get(ct, 0) + 1

        return s_dict == t_dict
