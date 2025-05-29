from typing import List


class Solution:
	def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
		n = len(products)
		products.sort()  # Sorting to ensure lexicographical order
		l, r = 0, n - 1
		result = []

		for i in range(len(searchWord)):
			# Move `l` forward if the current product does not match the search prefix
			while l <= r and (i >= len(products[l]) or products[l][i] != searchWord[i]):
				l += 1

			# Move `r` backward if the current product does not match the search prefix
			while l <= r and (i >= len(products[r]) or products[r][i] != searchWord[i]):
				r -= 1

			# Add top 3 lexicographically smallest products from the remaining range
			result.append(products[l:min(l + 3, r + 1)])

		return result


products = ["bags","baggage","banner","box","cloths"]
searchWord = "bags"
s = Solution()
print(s.suggestedProducts(products, searchWord))
