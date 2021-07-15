class PairValidator:

    def validate(self, input: str, input2: str):
        if len(input) != len(input2):
            return False

        for i in range(len(input)):
            cur = input[i]

            match = list(filter(lambda c : self.isAdjacent(cur,c),input2))
            if len(match) == 0:
                return False
            else:
                input2 = input2.replace(match[0],'',1)

        return True

    def isAdjacent(self, char1, char2):
        return ord(char1) - ord(char2) in range(-1,2)

    def removeAt(self, s: str, i) -> str:
        return s[:i] + s[i+1:] if i != len(s) else s[:-1]