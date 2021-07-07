"""
bfs solution, edge between two word would be the char transformation
then find the shortest path from source to destination

Time complexity: O(V * len of word * 26), generally equals to O( 26 * sum(length of word))
Space complexity: O(total length of words)
"""
class Solution:
    def ladderLength(self, begin: str, end: str, words: List[str]) -> int:
        words_set= set(words)
        cur = {begin}
        ret = 1
        while cur:
            if end in cur:
                return ret
            new_cur = set()
            words_set -= cur
            for word in cur:
                for idx in range(len(word)):
                    for asc in range(97, 97 + 26):
                        next_w = word[: idx] + chr(asc) + word[idx + 1:]
                        if next_w in words_set:
                            new_cur.add(next_w)
            cur = new_cur
            ret += 1
        return 0
