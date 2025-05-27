class Solution(object):
    def nextGreaterElement(self, nums1, nums2):

        # 次に大きい要素を格納する辞書
        next_greater = {}

        # スタック（単調減少）を使って探索
        stack = []

        # nums2を左から順に処理
        for num in nums2:
            # スタックが空でない & 今のnumがスタックトップより大きい → 解決
            while stack and num > stack[-1]:
                smaller = stack.pop()
                next_greater[smaller] = num

            # 今のnumをスタックに積む（次に来る要素で比較される候補）
            stack.append(num)

        # スタックに残ってる要素には、次に大きい要素が存在しない
        while stack:
            next_greater[stack.pop()] = -1

        # nums1に対応する次の大きい要素を辞書から引いて作成
        return [next_greater[num] for num in nums1]