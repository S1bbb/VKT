x, y = map(float, input().split())
if x * x + y * y <= 5 * 5:
    print("Точка принадлежит кругу")
else:
    print("Точка вне круга")
