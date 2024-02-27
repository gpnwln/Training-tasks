n = int(input())
grades = list(map(int, input().split()))

count3 = grades.count(3)
count4 = grades.count(4)
count5 = grades.count(5)

if (count3 < 2)&((count3 + count4) <= 0.25*n):
    print("Red")
else:
    print("Blue")