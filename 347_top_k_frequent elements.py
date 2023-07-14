# Time complexity should be O(n*k)
def top_k_frequent(nums, k):
    counts = {}
    answers = []
    # if the length of the input list is one, return that only element as that is the only answer
    if len(nums) == 1:
        return [nums[0]]
    # Get the counts of each number within nums list and store them in hash map with {k,v} = {number: its count}
    for number in nums:
        counts[number] = counts.get(number, 0) + 1
    # Now get the top k numbers that appear in the hash map
    for i in range(k):
        # store all the key value pairs as tuples in list
        inverse = [(value, key) for key, value in counts.items()]
        # get the value of the item that appears the most in count, max returns the largest element
        # in all the tuples so this will return the tuple containing largest value, and then we get
        # the key which is the number or tuple[1]
        print(max(inverse))
        j = max(inverse)[1]
        answers.append(j)
        # Remove that key from the map as we have already included it
        counts.pop(j)
    return answers


# print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))


def top_k_frequent_bucket_sort(nums, k):
    if len(nums) == 1:
        return nums
    buckets = [[] for _ in range(len(nums) + 1)]
    counts = {}
    top = []
    for number in nums:
        counts[number] = counts.get(number, 0) + 1
    for key, v in counts.items():
        buckets[v].append(key)
    # Start at the end of the buckets and go through their values
    for i in range(len(buckets) - 1, 0, -1):
        for j in buckets[i]:
            top.append(j)
            if len(top) == k:
                return top
# O(n) complexity in this case, the bucket values are the frequency of occurrence and the
# values stored are a list of the number that have that occurrence


print(top_k_frequent_bucket_sort([1, 1, 1, 2, 2, 3], 2))
