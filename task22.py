# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18

# 6 12


n = int(input("Введите кол-во элементов первого множества: "))
m = int(input("Введите кол-во элементов второго множества: "))
list_1 = list()
list_2 = list()
set_3 = set()
for i in range(n):
    n_e = input(f"Введите элемент {i+1} первого множества: ")
    list_1.append(int(n_e))
for i in range(m):
    m_e = input(f"Введите элемент {i+1} второго множества: ")
    list_2.append(int(m_e))    
print(list_1, list_2)
for i in list_1:
    if i in list_2:
        set_3.add(i)
print(sorted(set_3))        


