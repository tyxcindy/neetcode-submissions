class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        matchings = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        queue = []
        
        for char in s:
            if char in {"(", "{", "["}:
                queue.append(char)
            else:
                # Correct Order
                last_opened = queue.pop() if queue else False
                if not last_opened or last_opened != matchings[char]:
                    return False

        # All closed
        if queue:
            return False

        return True