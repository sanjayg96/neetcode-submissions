class Solution:
    def isValid(self, s: str) -> bool:
        closing = set([")", "]", "}"])
        opening = set(["(", "[", "{"])
        track = []

        if s[0] in closing:
            return False
        
        for i in range(len(s)):
            c = s[i]
            if c in opening:
                track.append(c)
            elif (c in closing) and (len(track) != 0):
                if c == ")" and track[-1] == "(":
                    track.pop()
                elif c == "]" and track[-1] == "[":
                    track.pop()
                elif c == "}" and track[-1] == "{":
                    track.pop()
                else:
                    return False
            elif (c in closing) and (len(track) == 0):
                return False
        
        if len(track) == 0:
            return True
        else:
            return False