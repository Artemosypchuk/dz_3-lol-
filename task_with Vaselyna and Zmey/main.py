from secondary import total, escape, print_eat, print_escape
import random
import colorama
from colorama import Fore, Back, Style
colorama.init()

vaselyna_score = []
zmey_score = []
# Let's play =)
print(Fore.BLUE+"\t!!!!-----Wellcome to the WildeGames-----!!!!")
print("\tДесь у видуманій історії....\n\t Васелина та Змій Горинич вирішили пограти в шахи!\n\t Та з незрозумілих причин вони почали їх їсти...\n\t Цікаво що сталося далі? Натисніть на 'Enter'")
input("\t\t\t")


while True:

    first_player = random.randint(0, 24)
    second_player = random.randint(0, 24)
    print(Fore.GREEN+"Васелина з’їла " + str(first_player)+" шт. шашок")
    print(Fore.RED+"Змій Горинич з’їв " +
          str(second_player)+" шт. шашок"+Fore.RESET)

    vaselyna_score.append(first_player)
    zmey_score.append(second_player)
    finish = input(
        'Натисніть "Enter"\n щоб вони з’їли ще шашок введіть\n "eat" щоб Змій з’їв Васелину\n "escape" щоб Васелина втікла: ')
    if finish == "eat":
        zmey_score.extend(vaselyna_score)
        result = total(zmey_score)
        print_eat(result)
        break
    elif finish == "escape":
        result = total(zmey_score)
        result2 = escape(vaselyna_score)
        print_escape(result,result2)
        break
