best_w = None
best_i = None
try:
    with open("spectrum.txt", encoding="utf-8") as f:
        count = 0
        for num, line in enumerate(f, 1):
            line = line.strip()
            if line == "" or line.startswith("#"):
                continue
            try:
                parts = line.split()
                if len(parts) != 2:
                    raise ValueError
                w = float(parts[0])
                i = float(parts[1])
            except ValueError:
                print(f"строка {num}: '{line}' не удалось разобрать, пропуск")
                continue
            count += 1
            if best_i is None or i > best_i:
                best_w, best_i = w, i
    if count == 0:
        raise ValueError("Нет данных для анализа")
except FileNotFoundError:
    print("Ошибка: файл spectrum.txt не найден")
except PermissionError:
    print("Ошибка: нет доступа к файлу spectrum.txt")
except OSError as e:
    print("Ошибка чтения spectrum.txt:", e)
except ValueError as e:
    print("Ошибка:", e)

if best_i is not None:
    print(f"Максимум: λ = {best_w} нм, I = {best_i}")
    try:
        with open("max_peak.txt", "w", encoding="utf-8") as f:
            f.write(f"Длина волны: {best_w} нм\n")
            f.write(f"Интенсивность: {best_i}\n")
    except OSError as e:
        print("Ошибка: не удалось записать max_peak.txt:", e)
