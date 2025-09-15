class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        if len(brokenLetters) == 0:
            return len(text.split())

        map = dict()
        for char in brokenLetters:
            map[char] = 0

        brokenWords = 0
        wordHasBroken = False

        for char in text:
            if not wordHasBroken and map.get(char,None) != None:
                brokenWords += 1
                wordHasBroken = True
            if char == " ":
                wordHasBroken = False

        return len(text.split())-brokenWords
        