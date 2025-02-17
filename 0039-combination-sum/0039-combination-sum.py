
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        results = []


        def dfs(index, path, target_numb):
            if target_numb== 0:
                results.append(path)
                return
            if target_numb <0:
                return
            for i in range (index, len(candidates)):
                dfs(i, path+[candidates[i]], target_numb-candidates[i])

        dfs(0, [], target)
        return results

