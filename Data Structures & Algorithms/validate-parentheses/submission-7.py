class Solution:
    def isValid(self, s: str) -> bool:
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
                if not queue:
                    return False
                last_opened = queue.pop() if queue else False
                if last_opened != matchings[char]:
                    return False

        # All closed
        if queue:
            return False

        return True