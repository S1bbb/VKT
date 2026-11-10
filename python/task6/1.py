h = 5

times = []
gs = []
try:
    with open("input.txt", encoding="utf-8") as f:
        for num, line in enumerate(f, 1):
            line = line.strip()
            if line == "":
                print(f"строка {num}: пустая, пропуск")
                continue
            try:
                t = float(line)
                if t <= 0:
                    raise ZeroDivisionError
                g = 2 * h / t ** 2
            except ValueError:
                print(f"строка {num}: '{line}' не число, пропуск")
                continue
            except ZeroDivisionError:
                print(f"строка {num}: время {line} <= 0, пропуск")
                continue
            times.append(t)
            gs.append(g)
except FileNotFoundError:
    print("Ошибка: файл input.txt не найден")
except PermissionError:
    print("Ошибка: нет доступа к файлу input.txt")
except OSError as e:
    print("Ошибка чтения input.txt:", e)

if len(times) == 0:
    print("Нет корректных измерений")
else:
    n = len(times)
    t_avg = sum(times) / n
    g_avg = sum(gs) / n
    print(f"Измерений: {n}, среднее время: {t_avg:.4f} с, среднее g: {g_avg:.4f} м/с^2")
    try:
        with open("output.txt", "w", encoding="utf-8") as f:
            f.write(f"Количество измерений: {n}\n")
            f.write(f"Среднее время: {t_avg:.4f} с\n")
            f.write(f"Среднее ускорение: {g_avg:.4f} м/с^2\n")
    except OSError as e:
        print("Ошибка: не удалось записать output.txt:", e)
