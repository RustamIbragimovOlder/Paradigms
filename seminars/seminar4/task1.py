# Нормализация данных

# Есть такая операция в статистике - “нормализация”. Это операция принимающая на вход вектор и возвращающая другой вектор. Смысл этой операции в том, чтобы данные из разных шкал загнать в единый диапазон, как правило - от 0 до 1, тогда с данными становится проще работать.
# Ваша задача: Реализовать с использованием функциональной парадигмы процедуру normalization, которая выполняет нормализацию полученного массива по приведенной формуле нормализованного значения элемента, где
# ○ x_norm - нормализованное значение элемента
# ○ x - исходное значение элемента
# ○ x_max, x_min - максимальное и минимальное значение в массиве

def normalize(data):
    min_value = min(data)
    max_value = max(data)

    def normalize_element(x):
        return (x - min_value) / (max_value - min_value)
    
    return list(map(normalize_element, data))

data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(normalize(data))