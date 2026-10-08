class GardenError(Exception):
	pass

class PlantError(GardenError):
	pass

class WaterError(GardenError):
	pass

def water_monitor(water_level: int):
	if (water_level >= 200):
		print("Water is sufficient!")
	else:
		raise WaterError

def sunlight_monitor(sun_level: int):
	if (sun_level >= 10):
		raise PlantError
	else:
		print("Sun is optimal!")

def error_test(error: str) -> None:
	if (error is PlantError):
		try:
				print("Testing PlantError...")
				sunlight_monitor(20)
				print("")
		except PlantError:
			print("Caught PlantError: The tomato plant is wilting!\n")
	elif (error is WaterError):
		try:
				print("Testing WaterError...")
				water_monitor(100)
				print("")
		except WaterError:
			print("Caught PlantError: The tomato plant is wilting!\n")
	else:
		try:
			print("Testing catching all garden errors...")
			sunlight_monitor(20)
			water_monitor(100)
			print("")
		except GardenError:
			print("Caught GardenError\n")

print("=== Custom Garden Errors Demo ===\n")
error_test(PlantError)
error_test(WaterError)
error_test("")
print("All custom error types work correctly!")