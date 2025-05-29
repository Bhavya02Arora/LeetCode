from functools import cmp_to_key
mp = {}

def comp(a, b):
    if a == b:
        return 0

    for i in range(min(len(a), len(b))):

        if mp[a[i]] < mp[b[i]]:
            return -1
        elif mp[a[i]] > mp[b[i]]:
            return 1

    if len(a) < len(b):
        return -1
    else:
        return 1

def printSorted(words, order):
    # Mapping each character
    # to its occurrence position
    for i in range(len(order)):
        mp[order[i]] = i

    # Sorting with custom sort function
    words = sorted(words, key=cmp_to_key(comp))

    # Printing the sorted order of words
    for x in words:
        print(x, end=" ")


# Driver code
words = ["word", "world", "row"]
order = "worldabcefghijkmnpqstuvxyz"

printSorted(words, order)

#############################################################

# Other Approach

def custom_sort(words, order):
    # Create a mapping of each character to its index in the given order
    order_map = {}
    for index in range(len(order)):
        order_map[order[index]] = index

    # Function to compare two words based on the custom order
    def compare(word1, word2):
        min_length = min(len(word1), len(word2))
        for i in range(min_length):
            if word1[i] != word2[i]:
                return order_map[word1[i]] - order_map[word2[i]]
        return len(word1) - len(word2)  # If words are prefixes, shorter word comes first

    # Implementing Bubble Sort (can use other sorting algorithms)
    n = len(words)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if compare(words[j], words[j + 1]) > 0:
                words[j], words[j + 1] = words[j + 1], words[j]  # Swap if out of order

    return words

# Example Usage:
words1 = ["hello", "geeksforgeeks"]
order1 = "hlabcdefgijkmnopqrstuvwxyz"
print(custom_sort(words1, order1))  # Output: ['hello', 'geeksforgeeks']
print(' '.join(custom_sort(words1, order1)))  # Output: hello geeksforgeeks

words2 = ["word", "world", "row"]
order2 = "worldabcefghijkmnpqstuvxyz"
print(custom_sort(words2, order2))  # Output: ['world', 'word', 'row']
print(' '.join(custom_sort(words2, order2)))  # Output: world word row
