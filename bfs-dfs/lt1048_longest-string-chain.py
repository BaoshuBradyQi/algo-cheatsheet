"""
dfs solution, to memorize the length of word chain for certain word
if child is visited before, directly return the length

Time complexity: O( sum( len(word)),
usually it's |E| + |V|, in this case, |V| is # word, E would be the len of each word

Space complexity: O(n), for n is number of word
"""
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words_set = set(words)
        len_dict = defaultdict(lambda: 0)

        def dfs(word):
            if len_dict[word]:
                return len_dict[word]
            ret = 0
            for idx in range(len(word)):
                child = word[: idx] + word[idx + 1:]
                if child in words_set:
                    len_dict[child] = dfs(child)
                    ret = max(ret, len_dict[child])
            return ret + 1

        for word in words_set:
            len_dict[word] = dfs(word)

        return max(len_dict.values())
