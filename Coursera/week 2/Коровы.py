a = int(input())
c = a % 10
if 10 < a < 20 or c == 0 or 9 >= c >= 5:
    print(a, "korov")
elif c == 1:
    print(a, "korova")
else:
    print(a, "korovy")
