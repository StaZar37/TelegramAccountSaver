
import os

from config import *

# Баннер
def banner(add_info=""):
	os.system("cls")
	print(f"""
{bl}
----------------------------------------
{gr}            Веб-студия
{re}            ╥     ╥         ╥{cy}
{re}            ║ ╔╗ ╔╣ ╥ ╥╥ ╥ ╔╣{cy}
{re}            ╨ ╨╙ ╙╜ ╨ ╙╜ ╨ ╙╜{cy}{bl}
----------------------------------------
{re}{add_info}{cy}
        """, end="")

# Главное меню
def main_menu(add_info=""):

	banner(add_info)

	print(f"""
{re}Помощь{cy} - readme.txt
Выберите модуль

{re}[0]{cy} - Установить зависимости
{re}[1]{cy} - Список аккаунтов
{re}[2]{cy} - Добавить аккаунт
{re}[3]{cy} - Проверять коды подтверждения
""")

	return input(f"{re}#Модуль:{cy} ")

def msg(msg):
	print(f"""

{bl}----------------------------------------

{cy}{msg}

{bl}----------------------------------------""")


def check_codes():
	return ""


# Конец работы
def end_work(add_info=""):
	os.system("cls")
	print(f"""

{bl}----------------------------------------

{re}          РАБОТА ПРЕКРАЩАЕТСЯ
{re}{add_info}
{bl}----------------------------------------""")
	exit()