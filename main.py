# # 20.12.2024   Uyga vazifa
#
# # 1 vazifa
#
# class CantexManager:
#     def __init__(self, file_name):
#         self.file_name = file_name
#     def read_file(self):
#         """Fayldan ma'lumotlarni o'qish."""
#         try:
#             with open(self.file_name, 'r') as file:
#                 return file.readlines()
#         except FileNotFoundError:
#             print(f"Xato: {self.file_name} topilmadi.")
#             return []
#     def write_file(self, data):
#         """Faylga ma'lumot yozish."""
#         with open(self.file_name, 'w') as file:
#             file.writelines(data)
#     def append_file(self, data):
#         """Faylga yangi ma'lumot qo'shish."""
#         with open(self.file_name, 'a') as file:
#             file.write(data + '\n')
# manager = CantexManager("example.txt")
# manager.append_file("Yangi qator qo'shildi.")
# print(manager.read_file())



# ----------------------------------------------------------------------------------------

# 1 vazifa

# from multiprocessing import Process
# import time
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# def calculate(l: list):
#     ygindi = 0
#     index = 0
#     while index < len(l):
#         ygindi += l[index]
#         index += 1
#       time.sleep(1)
#     print(f"Ro'yxatdagi barcha raqamlarning yig'indisi: {ygindi}")
# start = time.time()
# if __name__ == "__main__":
#     process = []
#     for i in range(2):
#
#         pr = Process(target=calculate, args=(numbers,))
#         pr.start()
#         process.append(pr)
#     for pr in process:
#         pr.join()
#
#     print(f"Funksiya ikki martta toliq ishlab chiqgunicha {round(time.time() - start, 2)} vaqt ketdi !")


# ----------------------------------------------------------------------------------------

# 2 vazifa

# from multiprocessing import Process
# import time
# import random
#
# numbers = [1, 2, 3, 4]
# def ab(l: list):
#     random.shuffle(l)
#     time.sleep(1)
#     print(f"Aralashtirilgan royxat: {l}")
# start = time.time()
# if __name__ == "__main__":
#     process = []
#     for i in range(2):
#         pr = Process(target=ab, args=(numbers,))
#         pr.start()
#         process.append(pr)
#     for pr in process:
#         pr.join()
#
#     print(f"Funksiya ikki martta toliq ishlab chiqgunicha {round(time.time() - start, 2)} vaqt ketdi !")


# ----------------------------------------------------------------------------------------

# 3 vazifa

# from multiprocessing import Process
# import time
#
# numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# numbers2 = [3, 82, 2485, 345924, 12, 2, 8]
# def ab(l: list):
#     kotta = max(l)
#     kichik = min(l)
#     print(f"Royxatdagi eng kotta qiymat: {kotta}\n"
#           f"eng kichigi esa: {kichik}")
# start = time.time()
# if __name__ == "__main__":
#     pr1 = Process(target=ab, args=(numbers1,))
#     pr1.start()
#     pr1.join()
#     pr2 = Process(target=ab, args=(numbers2,))
#     pr2.start()
#     pr2.join()
#     print(f"Funksiya ikki martta toliq ishlab chiqgunicha {round(time.time() - start, 2)} vaqt ketdi !")


# ----------------------------------------------------------------------------------------

# # 4 vazifa
#
# from multiprocessing import Process
# import time
# fruits = ["olma", "anor", "banan", "ananas", "behi", "apelsin", "o'rik", "shaftoli"]
# def ab(l: list, a: str):
#     count = 0
#     for i in l:
#         time.sleep(0.1)
#         if i == a:
#             count += 1
#         else:
#             pass
#     if count > 0:
#         print(f"Siz qidirgan meva royxatning {fruits.index(a) + 1} ornida turibdi !")
#     else:
#         print("Kechirasiz siz qidirgan meva bizning royxatdan topilmadi !")
# start = time.time()
# if __name__ == "__main__":
#     a1 = input("Qaysi mevani qidirasiz: ")
#     pr1 = Process(target=ab, args=(fruits, a1, ))
#     pr1.start()
#     pr1.join()
#     a2 = input("Qaysi mevani qidirasiz: ")
#     pr2 = Process(target=ab, args=(fruits, a2,))
#     pr2.start()
#     pr2.join()
#     print(f"Funksiya ikki martta toliq ishlab chiqgunicha {round(time.time() - start, 2)} vaqt ketdi !")


# ----------------------------------------------------------------------------------------

# 5 vazifa

# from multiprocessing import Process
# import time
# def ab(l: list):
#     unique = []
#     for item in l:
#         if item not in unique:
#             unique.append(item)
#     print(f"To'g'irlangan elementlar: {unique}")
# fruits1 = ["olma", "anor", "banan", "ananas", "behi", "apelsin", "o'rik", "shaftoli", "olma", "anor"]
# fruits2 = ["olma", "anor", "banan", "ananas", "behi", "apelsin", "o'rik", "shaftoli", "banan", "apelsin"]
# start = time.time()
# if __name__ == "__main__":
#     pr1 = Process(target=ab, args=(fruits1,))
#     pr1.start()
#     pr1.join()
#     pr2 = Process(target=ab, args=(fruits2,))
#     pr2.start()
#     pr2.join()
#     print(f"Funksiya ikki martta to'liq ishlab chiqgunicha {round(time.time() - start, 2)} soniya vaqt ketdi!")


# ----------------------------------------------------------------------------------------

# 6 vazifa

# from multiprocessing import Process
# import time
# fruits1 = ["olma", "anor"]
# fruits2 = ["olma", "anor", "banana"]
# def ab(l: list):
#     for i in range(len(l)):
#         time.sleep(1)
#         l[i] = l[i][::-1]
#     print(f"Yangi ro'yxat: {l}")
# start = time.time()
# if __name__ == "__main__":
#     pr1 = Process(target=ab, args=(fruits1,))
#     pr1.start()
#     pr1.join()
#     pr2 = Process(target=ab, args=(fruits2,))
#     pr2.start()
#     pr2.join()
#     print(f"Funksiya ikki martta toliq ishlab chiqgunicha {round(time.time() - start, 2)} vaqt ketdi !")


# ----------------------------------------------------------------------------------------

# 7 vazifa

# from multiprocessing import Process
# import time
# fruits1 = ["olma", "anor"]
# fruits2 = ["olma", "anor", "banana"]
# def ab(l: list):
#     max_word = ""
#     for i in l:
#         time.sleep(0.2)
#         if len(i) > len(max_word):
#             max_word = i
#     print(f"Eng uzun so'z: {max_word}")
# start = time.time()
# if __name__ == "__main__":
#     pr1 = Process(target=ab, args=(fruits1,))
#     pr1.start()
#     pr1.join()
#     pr2 = Process(target=ab, args=(fruits2,))
#     pr2.start()
#     pr2.join()
#     print(f"Funksiya ikki martta toliq ishlab chiqgunicha {round(time.time() - start, 2)} vaqt ketdi !")


# ----------------------------------------------------------------------------------------

# 8 vazifa
#
# from multiprocessing import Process
# import time
# fruits1 = ["olma", "anor", "banan", "kivi", "kivi"]
# fruits2 = ["olma", "anor", "apelsin", "apelsin", "shaftoli"]
# def ab(lst: list):
#     duplicates = []
#     values_seen = {}
#     for value in lst:
#         if value in values_seen:
#             values_seen[value] += 1
#         else:
#             values_seen[value] = 1
#     for value, count in values_seen.items():
#         if count > 1:
#             duplicates.append(f'"{value}" ikki martta takrorlangan')
#     print(duplicates)
# start = time.time()
# if __name__ == "__main__":
#     pr1 = Process(target=ab, args=(fruits1,))
#     pr1.start()
#     pr1.join()
#     pr2 = Process(target=ab, args=(fruits2,))
#     pr2.start()
#     pr2.join()
#     print(f"Funksiya ikki martta toliq ishlab chiqgunicha {round(time.time() - start, 2)} vaqt ketdi !")


# ----------------------------------------------------------------------------------------

# 9 vazifa

# from multiprocessing import Process
# import time
# def ab(d: dict):
#     numbers = []
#     for value in d.values():
#         if isinstance(value, (int, float)):
#             numbers.append(value)
#         elif isinstance(value, str):
#             numbers += [float(num) for num in value.split() if num.replace('.', '', 1).isdigit()]
#     print(sorted(numbers))
# data1 = {
#     "a": 42,
#     "b": "hello 12.5 world 100",
#     "c": 3.14,
#     "d": "50 apples",
#     "e": "no numbers here",
#     "f": 7,
# }
# data2 = {
#     "a": 42,
#     "b": "hello 125 world 100",
#     "c": 45493205843,
#     "d": "90 apples",
#     "e": "no numbers here",
#     "f": 7,
# }
# start = time.time()
# if __name__ == "__main__":
#     pr1 = Process(target=ab, args=(data1,))
#     pr1.start()
#     pr1.join()
#     pr2 = Process(target=ab, args=(data2,))
#     pr2.start()
#     pr2.join()
#     print(f"Funksiya ikki martta toliq ishlab chiqgunicha {round(time.time() - start, 2)} vaqt ketdi !")


# ----------------------------------------------------------------------------------------

# 10 vazifa

# from multiprocessing import Process
# import time
# def ab(d: dict):
#     numbers = []
#     for value in d.values():
#         if isinstance(value, (int, float)):
#             numbers.append(value * 2)
#         elif isinstance(value, str):
#             numbers += [float(num) * 2 for num in value.split() if num.replace('.', '', 1).isdigit() ]
#     print(sorted(numbers))
# data1 = {
#     "a": 42,
#     "b": "hello 12.5 world 100",
#     "c": 3.14,
#     "d": "50 apples",
#     "e": "no numbers here",
#     "f": 7,
# }
# data2 = {
#     "a": 42,
#     "b": "hello 125 world 100",
#     "c": 45493205843,
#     "d": "90 apples",
#     "e": "no numbers here",
#     "f": 7,
# }
# start = time.time()
# if __name__ == "__main__":
#     pr1 = Process(target=ab, args=(data1,))
#     pr1.start()
#     pr1.join()
#     pr2 = Process(target=ab, args=(data2,))
#     pr2.start()
#     pr2.join()
#     print(f"Funksiya ikki martta toliq ishlab chiqgunicha {round(time.time() - start, 2)} vaqt ketdi !")


# ----------------------------------------------------------------------------------------

# 11 vazifa

# from multiprocessing import Process
# import time
# def ab(d: dict):
#     max_key = max(d, key=d.get)
#     print(f"Eng katta qiymatga ega bolgan kalit: {max_key}")
# data1 = {
#     "a": 10,
#     "b": 42,
#     "c": 3.14,
#     "d": -5,
#     "e": 100,
# }
# data2 = {
#     "a": -10,
#     "b": -5,
#     "c": -100,
#     "d": -3,
# }
# start = time.time()
# if __name__ == "__main__":
#     pr1 = Process(target=ab, args=(data1,))
#     pr1.start()
#     pr1.join()
#     pr2 = Process(target=ab, args=(data2,))
#     pr2.start()
#     pr2.join()
#     print(f"Funksiya ikki martta toliq ishlab chiqgunicha {round(time.time() - start, 2)} vaqt ketdi !")


# ----------------------------------------------------------------------------------------

# 12 vazifa

# from multiprocessing import Process
# import time
# def ab(d: dict):
#     values = list(d.values())
#     avg_value = sum(values) / len(values)
#     print(f"O'rta qiymat: {avg_value}")
# data1 = {
#     "a": 10,
#     "b": 42,
#     "c": 3.14,
#     "d": -5,
#     "e": 100,
# }
# data2 = {
#     "a": -10,
#     "b": -5,
#     "c": -100,
#     "d": -3,
# }
# start = time.time()
# if __name__ == "__main__":
#     pr1 = Process(target=ab, args=(data1,))
#     pr1.start()
#     pr1.join()
#     pr2 = Process(target=ab, args=(data2,))
#     pr2.start()
#     pr2.join()
#     print(f"Funksiya ikki martta toliq ishlab chiqgunicha {round(time.time() - start, 2)} vaqt ketdi !")


# ----------------------------------------------------------------------------------------

# 13 vazifa
#
# from multiprocessing import Process
# import time
# def ab(d1: dict, d2: dict):
#     merged = d1.copy()
#     for key, value in d2.items():
#         if key in merged:
#             merged[key] += value
#         else:
#             merged[key] = value
#     print(f"JAVOB: {merged}")
# data1 = {
#     "a": 10,
#     "b": 42,
#     "c": 3.14,
#     "d": -5,
#     "e": 100,
# }
# data2 = {
#     "a": -10,
#     "b": -5,
#     "c": -100,
#     "d": -3,
# }
# start = time.time()
# if __name__ == "__main__":
#     pr1 = Process(target=ab, args=(data1, data2))
#     pr1.start()
#     pr1.join()
#
#     print(f"Funksiya ikki martta toliq ishlab chiqgunicha {round(time.time() - start, 2)} vaqt ketdi !")


# ----------------------------------------------------------------------------------------

# 14 vazifa

# from multiprocessing import Process
# import time
# def ab(d: dict):
#     if not d:
#         return None, None
#     uzun = max(d.keys(), key=len)
#     qisqa = min(d.keys(), key=len)
#     print(f"Eng uzun kalit: {uzun}, Eng qisqa: {qisqa}")
# data1 = {
#     "apple": 10,
#     "banana": 20,
#     "kiwi": 30,
#     "pomegranate": 40,
#     "a": 50
# }
# data2 = {
#     "grape": 10,
#     "orange": 20,
#     "pear": 30,
#     "watermelon": 40,
#     "x": 50
# }
# start = time.time()
# if __name__ == "__main__":
#     pr1 = Process(target=ab, args=(data1, ))
#     pr1.start()
#     pr1.join()
#     pr2 = Process(target=ab, args=(data2, ))
#     pr2.start()
#     pr2.join()
#     print(f"Funksiya ikki martta toliq ishlab chiqgunicha {round(time.time() - start, 2)} vaqt ketdi !")


# ----------------------------------------------------------------------------------------

# 15 vazifa

# from multiprocessing import Process
# import time
# def ab(d: dict):
#     for key, value in d.items():
#         if isinstance(value, str) and value.replace('.', '', 1).isdigit():
#             d[key] = float(value) if '.' in value else int(value)
#     print(d)
# data1 = {
#     "a": "42",
#     "b": "3.14",
#     "c": "hello",
#     "d": "100",
#     "e": 58
# }
# data2 = {
#     "x": "84",
#     "y": "2.71",
#     "z": "world",
#     "w": "200",
#     "v": 99
# }
# start = time.time()
# if __name__ == "__main__":
#     pr1 = Process(target=ab, args=(data1, ))
#     pr1.start()
#     pr1.join()
#     pr2 = Process(target=ab, args=(data2, ))
#     pr2.start()
#     pr2.join()
#     print(f"Funksiya ikki martta toliq ishlab chiqgunicha {round(time.time() - start, 2)} vaqt ketdi !")


# ----------------------------------------------------------------------------------------

# 16 vazifa

# from multiprocessing import Process
# import time
# def ab(d: dict):
#     new_dict = {}
#     for key, value in d.items():
#         time.sleep(0.1)
#         if isinstance(value, (int, float)):
#             new_dict[key] = value * 2
#         else:
#             new_dict[key] = value
#     print(new_dict)
# data1 = {
#     "a": 10,
#     "b": 3.14,
#     "c": "hello",
#     "d": 100,
#     "e": [1, 2, 3]
# }
# data2 = {
#     "x": 25,
#     "y": 5.5,
#     "z": "world",
#     "w": 50,
#     "v": [4, 5, 6]
# }
# start = time.time()
# if __name__ == "__main__":
#     pr1 = Process(target=ab, args=(data1, ))
#     pr1.start()
#     pr1.join()
#     pr2 = Process(target=ab, args=(data2, ))
#     pr2.start()
#     pr2.join()
#     print(f"Funksiya ikki martta toliq ishlab chiqgunicha {round(time.time() - start, 2)} vaqt ketdi !")


# ----------------------------------------------------------------------------------------

# 17 vazifa

# from multiprocessing import Process
# import time
# def ab(d: dict):
#     for key, value in d.items():
#         if isinstance(value, str):
#             d[key] = value[::-1]
#     print(d)
# data1 = {
#     "a": "hello",
#     "b": "world",
#     "c": 123,
#     "d": "python",
#     "e": 3.14
# }
# data2 = {
#     "x": "apple",
#     "y": "banana",
#     "z": 456,
#     "w": "grape",
#     "v": 7.89
# }
# start = time.time()
# if __name__ == "__main__":
#     pr1 = Process(target=ab, args=(data1, ))
#     pr1.start()
#     pr1.join()
#     pr2 = Process(target=ab, args=(data2, ))
#     pr2.start()
#     pr2.join()
#     print(f"Funksiya ikki martta toliq ishlab chiqgunicha {round(time.time() - start, 2)} vaqt ketdi !")


#================================================Rustamov Asilbek==========================================================