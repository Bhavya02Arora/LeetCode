from btnode import BTNode
from Trees import traverse

# class Solution:
#     ans = 0
#
#     def dfs(self, root, maximum):
#         if root.val >= maximum:
#             self.ans += 1
#         if root.left != None:
#             self.dfs(root.left, max(maximum, root.val))
#         if root.right != None:
#             self.dfs(root.right, max(maximum, root.val))
#
#
#     def goodNodes(self, root: BTNode) -> int:
#         self.dfs(root, -99999999999999999)
#         return self.ans


# class Solution:
#     ans = 0
#
#     def dfs(self, root, maximum):
#         print("root.val: ",root.val)
#         print("maximum: ",maximum)
#         if root.val >= maximum:
#             self.ans += 1
#         if root.left != None:
#             self.dfs(root.left, max(maximum, root.val))
#         if root.right != None:
#             self.dfs(root.right, max(maximum, root.val))
#
#
#     def goodNodes(self, root: TreeNode) -> int:
#         self.dfs(root, float(-inf))
#         return self.ans
#
# def testTraversals() -> None:
#     """
#     A function to test the traversals over different binary trees.
#     :return: None
#     """
#     # single node
#     traverse(BTNode(10))
#
#     # A parent node (20), with left (10) and right (30) children
#     traverse(BTNode(20, BTNode(10), BTNode(30)))
#
#     # from lecture notes: tree.png
#     traverse(BTNode('A',
#                     BTNode('B',
#                            None,
#                            BTNode('D')),
#                     BTNode('C',
#                            BTNode('E',
#                                   BTNode('G'),
#                                   None),
#                            BTNode('F',
#                                   BTNode('H'),
#                                   BTNode('I')))))


# li = [[],[0],[9]]
# print(li[0])
# print(li[1])
# print(li[2])

nums = [1, 3, 4, 1, 2, 3, 1]


def findMatrix(nums):
        li = [[]]
        flag = False
        i = 0
        for num in nums:
            for j in range(i):
                print(num)
                if num not in li[j]:

                    flag = True
                    li[j].append(num)
            if not flag:
                i += 1
                temp = []
                temp.append(num)
                li.append(temp)
            flag = False
        print(li)


findMatrix(nums)
