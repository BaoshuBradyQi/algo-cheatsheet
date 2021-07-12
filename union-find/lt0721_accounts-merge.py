"""
classic union find solution, append existing trees to current tree

to improve, compress path, instead of traverse through entire path over and over again

Time complexity: O(n), plus a sort, so worst case could be O(nlogn)
Space complexity: O(n)

"""
class Solution:
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        acc_dict = dict()
        merged = defaultdict(lambda: set())
        def find_root(val):
            while val in acc_dict and acc_dict[val] != val:
                val = acc_dict[val]
            return val
        for idx, acc in enumerate(accounts):
            name, root = acc[0], acc[1]
            root_acc = find_root((name, root))
            for i in range(1, len(acc)):
                acc_dict[find_root((name, acc[i]))] = root_acc

        for acc in acc_dict:
            merged[find_root(acc)].add(acc[1])

        return [ [key[0]] + sorted(value) for key, value in merged.items()]
