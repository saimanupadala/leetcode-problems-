class Solution:
    def frequencySort(self, s: str) -> str:
        count = {}

    
        for ch in s:
            count[ch] = count.get(ch, 0) + 1

       
        chars = sorted(count, key=count.get, reverse=True)

      
        result = ""

        for ch in chars:
            result += ch * count[ch]

        return result