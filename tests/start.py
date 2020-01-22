from start_test import *
import colorama
from colorama import Fore, Back, Style
colorama.init()
# import random


x = 1

qwestion_index = []

result = 0
for question in range(0, 8):
    print(Back.RED+"Question "+str(x) + " : " + Back.RESET+Fore.GREEN +
          test_list[question] + ": "+Back.RED)
    qwestion1 = int(
        input("Введіть номер який відповідає вірному результату-->: "))

    qwestion_index.append(qwestion1)
    x += 1
    if qwestion_index[question] == answer[question]:
        result += 1

if result >= 7:
    print(Fore.YELLOW+"\nНеймовірно!!! ви набрали: " +
          Fore.GREEN+str(result)+Fore.YELLOW+" балів.")
elif result <= 6 and result > 4:
    print(Fore.YELLOW+"\nНе погано! ви можете собою пишатися! Ви набрали: " +
          Fore.GREEN+str(result)+Fore.YELLOW+" балів.")
elif result <= 4 and result > 2:
    print(Fore.YELLOW+"\nВам потрібно ще вчитися. Ви набрали: " +
          Fore.RED+str(result)+Fore.YELLOW+" балів.")
elif result <= 2 and result >= 0:
    print(Fore.YELLOW+"\nПрограмування мабуть не ваше :( Ви набрали: " +
          Fore.RED+str(result)+Fore.YELLOW+" балів.")
