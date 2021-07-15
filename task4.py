# გვაქვს n სართულიანი კიბე, ერთ მოქმედებაში შეგვიძლია ავიდეთ 1 ან 2 საფეხურით.
# დაწერეთ ფუნქცია რომელიც დაითვლის n სართულზე ასვლის ვარიანტების რაოდენობას.

def paths_on_staircase(n: int, memo = None) -> int:
    if memo is None:
        memo = {}
    if n == 0 or n == 1:
        return n
    elif n in memo:
        return memo[n]

    memo[n] = paths_on_staircase(n - 1, memo) \
            + paths_on_staircase(n - 2, memo)
    return memo[n]


testcases = [0, 1, 2, 4, 5, 10, 100, 200]
for testcase in testcases:
    print(testcase, paths_on_staircase(testcase))
