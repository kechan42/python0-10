def garden_operations(operation_number) -> None:
	def test_error_types(error: Exception):
		if (error is ValueError):
			print("Caught ValueError")
		elif (error is ZeroDivisionError):
			print("Caught ZeroDivisionError")
		elif (error is FileNotFoundError):
			print("Caught FileNotFoundError")
		elif (error is TypeError):
			print("Caught TypeError")
		else:
			print("Caught UnknownError")

	while True:
		try:
			if (operation_number == 0):
				print(f"Testing operation {operation_number}...")
				x = int('abc')
			elif (operation_number == 1):
				print(f"Testing operation {operation_number}...")
				x = 42/0
			elif (operation_number == 2):
				print(f"Testing operation {operation_number}...")
				x = open("speak friend and enter")
			elif (operation_number == 3):
				print(f"Testing operation {operation_number}...")
				x = "add me" + 12345678
			else:
				print(f"Testing operation {operation_number}...")
			print("Operation completed successfully")
			return
		except (ValueError):
			test_error_types(ValueError)
		except (ZeroDivisionError):
			test_error_types(ZeroDivisionError)
		except (FileNotFoundError):
			test_error_types(FileNotFoundError)
		except (TypeError):
			test_error_types(TypeError)
		break

garden_operations(0)
garden_operations(1)
garden_operations(2)
garden_operations(3)
garden_operations(4)