# #1
# # with open("test.txt", 'r',newline=None) as file:
# #     for line in file:
# #         srt_some= line.strip()
# #         print(srt_some+'!')
#
#
# #2
# with open("input.txt", "r+") as file:
#     conteins = list(map(int, file.read().split()))
#
# with open("output.txt", "w") as new_file:
#     n = 1
#     for el in conteins:
#         n *= el
#     new_file.write(str(n))
import json

# # 3
# from datetime import date, datetime
#
# with open("items.txt", "r") as file:
#     now = datetime.now()
#
#     for line in file:
#         some_lst = line.split()
#         data = datetime.strptime(some_lst[3], "%d.%m.%Y")
#         period = now - data
#         if period.days >= 30 and (float(some_lst[2]) * float(some_lst[1])) > float(1000000):
#             print(f"Название: {some_lst[0]}\n  Количество: {some_lst[1]} кг\n  Цена: {some_lst[2]} руб\n  Дата завоза: {some_lst[3]}\n")

# # 4
# some_lst = []
# questions = []
# count_answer = 0
# with open("answer.txt", "r", encoding="utf-8") as file:
#     for line in file:
#         some_lst.append(line.strip())
#
# with open("questions.txt", "r", encoding="utf-8") as some_file:
#     for line in some_file:
#         questions.append(line.strip())
#
# for ind in range(len(questions)):
#     print(questions[ind])
#     answer = input("Print aswer this question: ")
#     if answer.lower() == some_lst[ind].lower():
#         count_answer += 1
#
# print(f"Число правильных ответов {count_answer}")

# 5
# dct = {
#     21341: ("Masha", 22),
#     44245: ("Alex", 25),
#     76595: ("Lenja", 37),
#     98579: ("Prudnik", 50),
#     74920: ("Philipp", 22)
# }
# with open("js.json","w") as write_file:
#     json.dump(dct,write_file,indent=4)
# print(type(dct[21341]))

# 6
# import csv
#
# with open("js.json", "r") as read_file:
#     data = json.load(read_file)
# print(data)
# with open("user.csv", "w") as file_write:
#     for key in data:
#         csv_some = csv.writer(file_write, delimiter=";")
#         some_lst=['Person', key,*data[key]]
#         csv_some.writerow((some_lst))

# # 7
# def count_duplicates(lst):
#     counts = {}
#     for item in lst:
#         if item in counts:
#             counts[item] += 1
#         else:
#             counts[item] = 1
#
#     return counts
#
#
# duplicates = []
# with open("7.txt", 'r') as file:
#     str_some = file.read().lower()
#     str_some = str_some.split()
#     duplicates = count_duplicates(str_some)
#     for item, count in duplicates.items():
#         if count > 1:
#             print(f"{item} {count}")
#         else:
#             print(f"{item} {1}")

# # 8
# lst = ""
# cont = ''
# alpha = ''
# with open("8.txt", "r") as file:
#     str_some = file.readline()
#     for i in range(len(str_some)):
#         if str_some[i].isalpha():
#             if cont!="":
#                 lst+=alpha*int(cont)
#             alpha = str_some[i]
#             cont = ''
#         else:
#             cont += str_some[i]
#     print(lst)
