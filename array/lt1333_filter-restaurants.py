class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        filtered = list(filter(lambda x: x[4] <= maxDistance, filter(lambda x: x[3]<= maxPrice, filter(lambda x: x[2] >= veganFriendly, restaurants))))
        filtered.sort(key = lambda x: (x[1], x[0]), reverse = True)
        ret = list(map(lambda x: x[0],  filtered))
        return ret