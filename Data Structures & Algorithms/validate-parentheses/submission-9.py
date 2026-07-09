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
                # Empty Queue
                if not queue:
                    return False

                # Correct Order
                last_opened = queue.pop()
                if last_opened != matchings[char]:
                    return False

        # All closed
        if queue:
            return False

        return True