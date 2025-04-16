import math

T = int(input())
for i in range(T):
    A, B = map(int, input().split())     # 최대공배수 공식 = 두수의 곱 / 최대공약수수
    lcm = A * B // math.gcd(A, B)   # LCM(A, B) = A × B / GCD(A, B)
    print(lcm)


