import os
import base58
import json
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Read the Base58 encoded private key from the environment variables
base58_encoded_private_key = os.getenv("PRIVATE_KEY")

# Ensure the private key is provided
if base58_encoded_private_key is None:
    raise ValueError("The private key is not set in the .env file")

# Decode the Base58 encoded private key
decoded_private_key = base58.b58decode(base58_encoded_private_key)

# Convert the byte sequence to a list of numbers
private_key_array = list(decoded_private_key)

# Create a JSON object containing the private key
private_key_json = json.dumps(private_key_array, separators=(",", ":"))

# Write the JSON object to a file
with open("id.json", "w") as key_file:
    key_file.write(private_key_json)

print("The private key has been stored as id.json")

# Check if the data is written to the file correctly
with open("id.json", "r") as key_file:
    loaded_private_key_array = json.load(key_file)

if loaded_private_key_array == private_key_array:
    print("Verification successful: The data in id.json matches the original private key.")
else:
    raise ValueError("Verification failed: The data in id.json does not match the original private key.")
