from collections import defaultdict

def distributeCandies(candies):
    """
    :type candies: List[int]
    :rtype: int
    """

    # create a hashmap of the type : number of candies
    candy_hash = defaultdict(int)
    for val in candies:
        candies[val] += 1

    # count total number of candies / 2 = share for each
    total_candies = len(candies)
    candies_for_sister = total_candies/2

    # sort the candies from least to greatest
    # count till candies_for_sister
    curr_sister_candies = 0
    for candy in sorted(candy_hash, key=candy_hash.get, reverse=True):

        print candy, candy_hash[w]
    while curr_sister_candies < candies_for_sister:

distributeCandies()
