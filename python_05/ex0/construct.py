import sys
import os
import site

def in_venv():
	return sys.prefix != sys.base_prefix

if (in_venv() == False):
	print("LABORATORY STATUS: You are working in the open\n")
	print(f"Current Python: {sys.executable}")
	print("Virtual Environment: None detected\n")
	print("WARNING: You are in the global environment!")
	print("Every reagent you install here leaks into the whole system.\n")
	print("To seal the laboratory, run:")
	print("python3 -m venv lab_env")
	print("source lab_env/bin/activate # On Unix")
	print("lab_env\Scripts\\activate # On Windows\n")
	print("Then run this program again.")
else:
	print("LABORATORY STATUS: The laboratory is sealed\n")
	print(f"Current Python: {sys.executable}")
	last = sys.prefix.split('/')
	print(f"Virtual Environment: {last[len(last) - 1]}")
	print(f"Environment Path: {sys.prefix}\n")
	print ("SUCCESS: You are working in an isolated environment!")
	print ("Safe to install reagents without affecting\nthe global system.\n")
	print (f"Reagent installation path:\n{site.getsitepackages()[0]}")
