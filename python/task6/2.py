t0 = None
r0 = None
alphas = []
try:
    with open("data.csv", encoding="utf-8") as f:
        for num, line in enumerate(f, 1):
            line = line.strip()
            if line == "":
                continue
            try:
                parts = line.split(",")
                if len(parts) != 2:
                    raise ValueError
                t = float(parts[0])
                r = float(parts[1])
            except ValueError:
                if num == 1:
                    print("строка 1: заголовок, пропуск")
                else:
                    print(f"строка {num}: '{line}' неверный формат, пропуск")
                continue
            if t0 is None:
                t0, r0 = t, r
                print(f"опорная точка: T0 = {t0}, R0 = {r0}")
                continue
            try:
                alphas.append((r - r0) / (r0 * (t - t0)))
            except ZeroDivisionError:
                print(f"строка {num}: T = T0 или R0 = 0, деление на ноль, пропуск")
except FileNotFoundError:
    print("Ошибка: файл data.csv не найден")
except OSError as e:
    print("Ошибка чтения data.csv:", e)

if len(alphas) == 0:
    print("Не удалось вычислить ни одного α")
else:
    n = len(alphas)
    a = sum(alphas) / n
    print(f"Точек: {n}, среднее α = {a:.6f} 1/°C")
    try:
        with open("result.txt", "w", encoding="utf-8") as f:
            f.write(f"Среднее alpha: {a:.6f} 1/°C\n")
            f.write(f"Использовано точек: {n}\n")
    except OSError as e:
        print("Ошибка: не удалось записать result.txt:", e)
