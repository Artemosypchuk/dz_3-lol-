if __name__ == "__main__":
    total()
    escape()
    print_escape()
    print_eat()
import colorama
from colorama import Fore, Back, Style
colorama.init()




def total(*params):
    res = 0
    for item in params:
        res += sum(item)
    return res

def escape(*params):
    res2 = 0
    for item in params:
        res2 += sum(item)
    return res2

def print_eat(result):
    print(Fore.YELLOW+"Поласувавши смачненьким, Змій зрозумів, що разом із Васелиною з’їв ще й усі шашки які вона з’їла!\n Ретельно підрахувавши внього виявилось: "+Fore.RED+str(result)+Fore.YELLOW+" шт. шашок!"+Fore.BLUE+"\n \"Гарно пограли\" "+Fore.YELLOW+"- розсміявся Змій.")


def print_escape(result,result2):
    print(Fore.YELLOW+"Змій не зміг з’їсти Васелину! Проте він з’їв: "+Fore.RED+str(result)+Fore.YELLOW+" шт. шашок загалом!\n","Васелина ж з’їла: "+Fore.RED+str(result2)+Fore.YELLOW+" шт. шашок! Та вирішила зі Змієм більше не грати!")