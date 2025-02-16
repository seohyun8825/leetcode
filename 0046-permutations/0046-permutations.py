class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        prev_list = []

        def dfs(current_list):
            if len(current_list) == 0:
                answer.append(prev_list[:])
                return

            for i in current_list:
                next_list = current_list[:]
                next_list.remove(i)

                prev_list.append(i)
                dfs(next_list)
                prev_list.pop()
        dfs(nums)
        return answer
