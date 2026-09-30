class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for word in strs:
            output += word + "\n"

        return output

    def decode(self, s: str) -> List[str]:
        output = s[:len(s)].split("\n")
        output.pop()

        return output

        # output = []
        # index = 0

        # while index < len(s):
        #     word = ""
            
        #     while s[index] != "\n":
        #         word += s[index]
        #         index += 1

        #     output.append(word)
        #     index += 1
        
        # return output