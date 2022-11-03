def numbers(n):
    if n == 0:
        print(n)
        return
    print(n)
    return numbers(n - 1)


def power(number, n):
    if n == 0:
        return 1
    return power(number, n - 1) * number


def factorial(n):
    if n == 0:
        return 1
    return factorial(n - 1) * n


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 2) + fib(n - 1)


def reverse(n):
    if len(n) == 1:
        return n
    return n[-1] + reverse(n[:-1])


def remove_duplicates(n):
    if len(n) == 0:
        return n
    if len(n) == 1:
        return n
    if n[len(n) - 2] == n[len(n) - 1]:
        return remove_duplicates(n[:-1])
    return remove_duplicates(n[:-1]) + n[-1]


def prime(n, i=2):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % i == 0:
        return False
    if i * i > n:
        return True
    return prime(n, i + 1)


def generate_parentheses(n, open, close, s, ans):
    if open == n/2 and close == n/2:
        ans.append(s)
        return

    if open < n:
        generate_parentheses(n, open + 1, close, s + "(", ans)

    if close < open:
        generate_parentheses(n, open, close + 1, s + ")", ans)


def balanced_parentheses(n):
    ans = []
    generate_parentheses(n, 0, 0, "", ans)

    for s in ans:
        print(s)


