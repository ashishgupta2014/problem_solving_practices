from fastcache import lru_cache

@lru_cache(maxsize=None)
def func(a,b,c):
    print('fun_input=>', a,b, c)
    if a==1 or a==2:
        return a+1, b+1, c+1
    if a==2 and c==1:
        return a+2, b+2, c+2
print(func(a=1,b=0,c=1))  # 2 1 2

print(func(a=2,b=0,c=1))  # 4 2 3

print(func(a=2,b=0,c=1))

print(func(a=2,b=3,c=1))

print(func(a=1,b=0,c=1))