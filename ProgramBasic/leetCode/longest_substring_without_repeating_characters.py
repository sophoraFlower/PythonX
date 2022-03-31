class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        temp_list = []
        temp_dic = {}
        long_str = ""
        if len(s) == 0:
            return 0
        for s_ in s:
            if s_ in temp_list:
                s_index = temp_list.index(s_)
                temp_list = temp_list[s_index+1:]
                temp_list.append(s_)
                long_str = long_str[s_index+1:] + s_
                count = len(temp_list)
            else:
                count += 1
                temp_list.append(s_)
                long_str += s_
            if long_str not in temp_dic:
                temp_dic[long_str] = count
        print(temp_dic.items())
        return sorted(temp_dic.values())[-1]


test = Solution()
for i in ["", "a", "abc", "abcab", "abccasddaavbbsadfajsdfbsb", "dvdf", "ckilbkd"]:
    print(test.lengthOfLongestSubstring(i))


