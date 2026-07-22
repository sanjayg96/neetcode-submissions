class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sign_dict = {}

        for string in strs:
            print(string)
            count = [0,] * 26
            for char in string:
                count[ord(char) - ord("a")] += 1
            
            count_tup = tuple(count)
            
            if count_tup in sign_dict:
                sign_dict[count_tup] = sign_dict[count_tup] + [string]
            else:
                sign_dict[count_tup] = [string]

            

        result_list = list(sign_dict.values())

        return result_list

