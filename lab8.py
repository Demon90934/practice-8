from random import randint
import datetime
from prettytable import PrettyTable
import sorts


def inp():  # Считывание количества элементов в последовательности
    number = int(input("Введите число элементов последовательности:"))
    return number


def create_sequence():  # Создание последовательности
    list_n = []
    for i in range(0, n+1):
        list_n.append(randint(-5678, 45672))
    return list_n


def out_check():
    my_file = open("output.txt", "w")
    my_file.write(str(sorts.check(sequence)) + "\n")
    my_file.close()
    pass


def sorting_time(s):
    time_1 = datetime.datetime.now()
    sorts.bubble_sorting(s)
    time_bubble = datetime.datetime.now() - time_1

    time_2 = datetime.datetime.now()
    sorts.sorting_choice(s)
    time_choice = datetime.datetime.now() - time_2

    time_3 = datetime.datetime.now()
    sorts.quick_sorting(s)
    time_quick = datetime.datetime.now() - time_3

    time_4 = datetime.datetime.now()
    sorted(s)
    time_sorted = datetime.datetime.now() - time_4
    return time_bubble, time_choice, time_quick, time_sorted


def add_table():
    table_sorts = PrettyTable()
    table_sorts.add_column("Метод сортировки", ["Сортировка пузырьком", "Сортировка выбором", "Быстрая сортировка",
                                                "Встроенная сортировка"])
    table_sorts.add_column("Рандомная посл-ть", [time_bubble_seq, time_choice_seq, time_quick_seq, time_sorted_seq])
    table_sorts.add_column("Отсортированная посл-ть", [time_bubble_s_seq, time_choice_s_seq, time_quick_s_seq,
                                                       time_sorted_s_seq])
    table_sorts.add_column("Отсортированная в обратном порядке посл-ть", [time_bubble_r_seq, time_choice_r_seq,
                                                                          time_quick_r_seq, time_sorted_r_seq])
    return table_sorts


def out():
    my_file = open("output.txt", "a")
    my_file.write("Количество элементов в последовательности: %d" % n + "\n")
    my_file.write(str(sequence) + "\n")
    my_file.write(str(sort_table))
    my_file.close()
    pass


n = inp()
sequence = create_sequence()
out_check()
sort_sequence = sorted(sequence)
reverse_sequence = sorted(sequence, reverse=True)
time_bubble_seq, time_choice_seq, time_quick_seq, time_sorted_seq = sorting_time(sequence)
time_bubble_s_seq, time_choice_s_seq, time_quick_s_seq, time_sorted_s_seq = sorting_time(sort_sequence)
time_bubble_r_seq, time_choice_r_seq, time_quick_r_seq, time_sorted_r_seq = sorting_time(reverse_sequence)
sort_table = add_table()
out()
