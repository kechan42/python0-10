import importlib.util
import sys

def pkg_check():
	checknum = 0
	print("REAGENT STATUS: Loading reagents...\n")
	print("Checking dependencies:")
	try:
		import pandas
	except (ImportError, ModuleNotFoundError):
		print("Pandas is not installed in this environment.")
		checknum = -1
	try:
		import numpy
	except (ImportError, ModuleNotFoundError):
		print("Numpy is not installed in this environment.")
		checknum = -1
	if (checknum != -1):
		print(f"[OK] pandas ({pandas.__version__} - Data manipulation ready)")
		print(f"[OK] numpy ({numpy.__version__} - Numerical computation ready)\n")
		print("pip vs Poetry:")
		print("  pip is the default package management system that's easy to use but")
		print("  it is hard to distinguish which packages require which other packages\n")
		print("  Poetry uses pip but also allows for grouped dependency management in")
		print("  the toml file, which makes managing dependencies easier")
		print("  it can also allow for inter-system packages as lock files")
		print("  allow for all installs to be identical")
		print("  it is however harder to use and takes longer to execute")
	else:
		print("\nTo install required dependencies, use 'pip install -r requirments.txt'")
		print("or use 'poetry install'.")

pkg_check()
