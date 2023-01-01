# https://leetcode.com/problems/unique-morse-code-words/

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        result = set()
        # full morse table for the 26 letters of the English alphabet
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", 
                 "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",
                 ".--","-..-","-.--","--.."]
        
        for word in words:
            morse_word = ""
            for char in word:
                morse_word += morse[ord(char)-ord('a')]
            result.add(morse_word)
        
        return len(result)
    