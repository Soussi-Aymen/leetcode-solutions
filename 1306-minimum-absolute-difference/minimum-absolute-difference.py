class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        min_abs_diff = float("inf")
        pairs = []
        arr.sort()

        for i in range(1,len(arr)):
            if arr[i] - arr[i - 1] < min_abs_diff:
                min_abs_diff = arr[i] - arr[i - 1]
                pairs = [[arr[i - 1], arr[i]]]
            elif arr[i] - arr[i - 1] == min_abs_diff:
                pairs.append([arr[i - 1], arr[i]])
        
        return pairs