def _odd_iter():
    """创建奇数序列"""
    n = 1
    while True:
        n += 2
        yield n


def primes(end_num):
    """埃氏筛法求end_num范围内的素数"""
    if end_num < 2:
        return
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        if n > end_num:
            break
        yield n
        it = filter(lambda x: x % n > 0, it)


if __name__ == '__main__':
    print(list(primes(10)))
