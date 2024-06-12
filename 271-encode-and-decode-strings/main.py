from typing import List
import re

deli = "🔥"
deli2 = "❓"

class Solution:

    def encode(self, strs: List[str]) -> str:
        start = "{0}{1}{0}".format(deli2, len(strs))
        start += deli.join(strs)
        return start

    def decode(self, s: str) -> List[str]:
        len = int(re.findall(deli2 + "([0-9]+)" + deli2, s)[0])
        s = re.sub(deli2 + "([0-9]+)" + deli2, "", s)
        split = s.split(deli)
        a = []

        print(split)
        for i in range(0, len):
            a.append(split.pop(0))
        return a



q = ["neet","code","love","you"]
s = Solution()
print(s.encode(q))
print(s.decode(s.encode(q)))