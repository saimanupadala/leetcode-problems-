class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code = [
            ".-","-...","-.-.","-..",".","..-.","--.","....","..",
            ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
            "...","-","..-","...-",".--","-..-","-.--","--.."
        ]
        
        seen = set()
        
        for word in words:
            # Map each character to its Morse code using ASCII offset ord(c) - ord('a')
            transformation = "".join(morse_code[ord(char) - ord('a')] for char in word)
            seen.add(transformation)
            
        return len(seen)