class GardenError(Exception):
	pass

class PlantError(GardenError):
	pass

class WaterError(GardenError):
	pass

def water_plant(plant_name: str):
	if (plant_name == plant_name.capitalize()):
		print(f"Watering {plant_name.capitalize()}: [OK]")
	else:
		raise PlantError

def test_watering_system():
	print("=== Garden Watering System ===\n")
	print("Testing valid plants...")
	try:
		plant_name = "Tomato"
		water_plant("Tomato")
		plant_name = "Lettuce"
		water_plant("Lettuce")
		plant_name = "Carrots"
		water_plant("Carrots")
	except:
		print(f"Caught PlantError: Invalid plant name to water: '{plant_name}'")
		print(".. ending tests and returning to main")
	finally:
		print("Closing watering system\n")
	print("Testing invalid plants...")
	try:
		plant_name = "Tomato"
		water_plant("Tomato")
		plant_name = "lettuce"
		water_plant("lettuce")
		plant_name = "Carrots"
		water_plant("Carrots")
	except:
		print(f"Caught PlantError: Invalid plant name to water: '{plant_name}'")
		print(".. ending tests and returning to main")
	finally:
		print("Closing watering system\n")
	print("Cleanup always happens, even with errors!")

test_watering_system()