class Solution:
    def numberGame(self, nums):
        arr = []

        # numsが空になるまで繰り返す
        while nums:
            nums.sort()  # 最小を取りやすくするために毎回ソート

            # Aliceが最小を取る
            alice_pick = nums.pop(0)

            # Bobが次の最小を取る
            bob_pick = nums.pop(0)

            # Bobが先にarrに追加して、次にAlice
            arr.append(bob_pick)
            arr.append(alice_pick)

        return arr