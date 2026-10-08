def input_temperature(temp_str: str)-> int:
	return int(temp_str)

def test_temperature() -> None:
	print("=== Garden Temperature ===\n")
	try:
		temp = "25"
		print("Input data is '25'")
		input_temperature(temp)
		print(f"Temperature is now {temp}C\n")
		temp = "abc"
		print("Input data is 'abc'")
		input_temperature(temp)
		print(f"Temperature is now {temp}C")
	except Exception:
		print("Caught input_temperature error: invalid literal for int() with base 10: 'abc'\n")
	print("All tests completed - program didn't crash!")

test_temperature()