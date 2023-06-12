

from config import *
from function import *
from subprocess import Popen

try:
	from telethon.sync import TelegramClient, events
except:
	import os
	os.system(ir)
	exit()

import threading
import os

try:

	def start(add_info=""):
		mode = main_menu(add_info)
		mode_handler(mode)


	def mode_handler(mode):
		if mode == "0":
			requirements()
		elif mode == "1":
			acc_list()
		elif mode == "2":
			add_acc()
		elif mode == "3":
			check_codes()
		else:
			mode = main_menu(add_info="Ошибка в аргументе!")
			mode_handler(mode)


	def menu(items=False):
		msg = ''
		if items:
			pass

		msg = msg + f"""

{re}[-]{cy} - Главное меню
		"""
		print(msg)

		input_info = input(f"{re}Действие:{cy} ")
		if input_info == '-':
			mode = main_menu()
			mode_handler(mode)
		else:
			return input_info


	def requirements():
		os.system("cls")
		msg("Началась загрузка зависимостей...")

		os.system(ir)

		msg("Загрузка зависимостей окончена!")

		import time
		time.sleep(2)
		start()


	def acc_list():
		accs = os.listdir("accs")
		os.system("cls")

		if not bool(accs):
			print("Аккаунтов нету!", end="")
			menu()
			return

		count = len(accs)

		msg(f"Количество аккаунтов: {count}")

		for acc in accs:
			print(f"{gr}{acc}{cy}")

		menu()


	def add_acc():
		try:
			os.system("cls")
			msg("Введите данные")
			print("\n")
			phone    = input(f"{re}phone: {cy}")

			phone = phone.replace(" ", "")
			phone = phone.replace("(", "")
			phone = phone.replace(")", "")
			phone = phone.replace("+", "")

			os.mkdir(f"accs/{phone}")

			client = TelegramClient(f"accs/{phone}/{phone}.session", api_id, api_hash)

			client.connect()
			if not client.is_user_authorized():
				client.send_code_request(phone)
				client.sign_in(phone, input(f"{re}Код для входа: {cy}"))

			client.disconnect()

			start("Аккаунт добавлен!")
		except Exception as e:
			if debug:
				print(e)
			elif not debug:
				end_work("Возникла какая-то ошибка...")


	def catch_codes(): # отлов кодов для входа
		accs = os.listdir("accs")

		if bool(accs):
			for acc in accs:
				threading.Thread(target=Popen, args=(["python", "catch.py", f"{acc}"],)).start()


	def check_codes(): # поиск кодов для входа внутри скрипта и отображение их
		catch_codes()
		import time

		banner(f"{gr}Проверка кодов...{cy}")
		print()

		while True:
			codes = os.listdir("codes")
			
			if bool(codes):
				for code in codes:
					data  = open(f"codes/{code}", "r", encoding="utf8").read()
					phone = data.split(":")[0]
					code_ = data.split(":")[1]
					data  = f"{gr}Аккаунт: {phone} {cy}Код: {code_}"
					print(data)
					os.remove(f"codes/{code}")

			time.sleep(3)


	start()

except KeyboardInterrupt as e:
	end_work()

except Exception as e:
	if debug:
		print(e)