class TempRangeError(Exception):
	pass

def input_temperature(temp_str: str)-> int:
	if (int(temp_str) >= 0 and int(temp_str) <= 40):
		return int(temp_str)
	else:
		raise TempRangeError('TempRangeError: temperature out range of 0 - 40C')

def test_temperature() -> None:
	def test(input):
		try:
			print(f"Input data is '{input}'")
			input_temperature(input)
			print(f"Temperature is now {input}C\n")
		except (TempRangeError):
			print("Caught input_temperature error: temperature out range of 0 - 40C\n")
		except (ValueError):
			print("Caught input_temperature error: invalid literal for int() with base 10: 'abc'\n")

	print("=== Garden Temperature ===\n")
	test("25")
	test("abc")
	test("-50")
	test("100")
	print("All tests completed - program didn't crash!")

test_temperature()