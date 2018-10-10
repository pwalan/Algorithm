import itertools


# 数字字符a,b，对k位数字有多少美丽数字（只包含a和b，且数字每位之和也只包含a和b）

class Solution():
    def beautifulNum(self, a, b, k):
        count = 0
        permutations = list(itertools.product([int(a), int(b)], repeat=int(k)))
        for permutation in permutations:
            sum = 0
            for i in permutation:
                sum += i
            isBeautiful = True
            str_sum = str(sum)
            for i in range(len(str_sum)):
                if str_sum[i] != str(a) and str_sum[i] != str(b):
                    isBeautiful = False
                    break
            if isBeautiful:
                count += 1
        return count


if __name__ == '__main__':
    solution = Solution()
    print(solution.beautifulNum(1,2,2))
