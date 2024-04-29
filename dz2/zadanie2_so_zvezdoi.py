set1 = {6, 31, 14, 25, 19, 3, 55}
set2 = {30, 22, 6, 79, 25}
set3 = {9, 1, 22, 19, 30}
union1 = set1 | set2
print(f"Объединение 1 и 2 массивов: {union1}")
union2 = union1 | set3
print(f"Объединение полученного множества с 3 массивом: {union2}")
diff_1 = (set1 & set2)
diff_2 = (set2 & set3)
diff_3 = (set3 & set1)
diff_union = diff_1 | diff_2 | diff_3
print(f"Список из элементов, которые не вошли в множества: {diff_union}")
final_diff = union2 - diff_union
print(f"Разница всех элементов множества и списка: {final_diff}")