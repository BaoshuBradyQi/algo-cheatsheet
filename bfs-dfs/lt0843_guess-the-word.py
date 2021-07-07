"""
kind of like the venn graph, keep finding candidates from a subset
subset would be with the same similarity as the candidate

Time complexity: O(# words * # of guesses)
Space complexity: O(n)
"""
# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        def similarity(w1, w2):
            ret = 0
            for c1, c2 in zip(w1, w2):
                if c1 == c2:
                    ret += 1
            return ret

        word_set = set(wordlist)
        while word_set:
            candi = random.sample(word_set, 1)[0]
            word_set.remove(candi)
            guess = master.guess(candi)
            if guess == 6:
                return candi
            new_set = set()
            for w in word_set:
                if similarity(w, candi) == guess:
                    new_set.add(w)
            word_set = new_set

