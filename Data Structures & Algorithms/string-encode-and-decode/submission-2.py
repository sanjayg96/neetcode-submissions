class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for strings in strs:
            encoded += "|#|" + strings

        return encoded

    def decode(self, s: str) -> List[str]:
        decoded_val = s.split("|#|")[1:]
        return decoded_val
