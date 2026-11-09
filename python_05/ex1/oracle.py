import os
from dotenv import dotenv_values


os.environ["MATRIX_MODE"] = "production"
os.environ["DATABASE_URL"] = "Disconnected"
os.environ["API_KEY"] = "N/A"
os.environ["LOG_LEVEL"] = "USER"
os.environ["ZION_ENDPOINT"] = "Offline"

print("\nORACLE STATUS: Consulting the configuration...\n")
config = dotenv_values(".env")
if (not config):
    print("Configuration is not loaded.")
    print("Mode: " + os.environ["MATRIX_MODE"])
    print("Database: " + os.environ["DATABASE_URL"])
    print("API Access: " + os.environ["API_KEY"])
    print("Log Level: " + os.environ["LOG_LEVEL"])
    print("Remote Network: " + os.environ["ZION_ENDPOINT"])
else:
    print("Configuration loaded:")
    for element in config:
        print(f"{element}: {config[element]}")

print("\nConfiguration security check: ")
try:
    with open(".gitignore", 'r') as f:
        content = f.read()
        if (content != ".env"):
            print("[WARNING] .env file not found in .gitignore")
        else:
            print("[OK] .env file properly ignored by git")
        f.close()

except:
    print("File Error")
