# LIS 길이 계산하기

def solution(nums):
    n = len(nums)
    dp = [1] * n    # LIS 길이 저장하는 리스트 초기화

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


nums_list = [[1,4,2,3,1,5,7,3], [3,2,1]]
for data in nums_list:
    print(solution(data))
