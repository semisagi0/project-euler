sympyの整数論系関数のドキュメント。

[https://docs.sympy.org/latest/modules/ntheory.html](https://docs.sympy.org/latest/modules/ntheory.html)

### 素因数分解
```
import sympy
assert(sympy.factorint(1000000007*1000000009) == {1000000007: 1, 1000000009: 1})
```

### 約数列挙
```
import sympy
assert(sympy.divisors(24) == [1, 2, 3, 4, 6, 8, 12, 24])
```

### n番目の素数
```
import sympy
assert(sympy.prime(1) == 2)
assert(sympy.prime(2) == 3)
assert(sympy.prime(3) == 5)
```

### `[a,b)`に属する素数
```
import sympy
assert(list(sympy.primerange(3, 11)) == [3, 5, 7])
```


