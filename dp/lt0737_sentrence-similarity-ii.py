"""
similar to union find solution
store the parents of each node, and parent for a set of nodes
if two words belong to different set, merge to one of it and update the both dictionaries

time complexity: depends on the input pairs, O(n) for the worst case i guess
space complexity: O(n), for n is number of similar pairs

compare to regular union find, this solution converts depth to breath, better if input has more disjoint sets
"""
class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        pairs = dict()

        vertex_dict = dict()
        for p in similarPairs:
            p_p, p_c = p[0], p[1]
            if p_p not in pairs and p_c not in pairs:
                pairs[p_p] = p_p
                pairs[p_c] = p_p
                vertex_dict[p_p] = set({p_c, p_p})
            elif p_p not in pairs:
                pairs[p_p] = pairs[p_c]
                vertex_dict[pairs[p_c]].add(p_p)
            elif p_c not in pairs:
                pairs[p_c] = pairs[p_p]
                vertex_dict[pairs[p_p]].add(p_c)
            else:
                if pairs[p_p] != pairs[p_c]:
                    p_c_set = vertex_dict[pairs[p_c]]
                    old_pc = pairs[p_c]
                    for v in p_c_set:
                        pairs[v] = pairs[p_p]
                    vertex_dict[pairs[p_p]].update(p_c_set)
                    del vertex_dict[old_pc]

        for s1, s2 in zip(sentence1, sentence2):
            if s1 == s2:
                continue
            else:
                if s1 in pairs and s2 in pairs and pairs[s1] == pairs[s2]:
                    continue
                return False
        return True
