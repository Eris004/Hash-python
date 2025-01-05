import hashlib

def generate_hash(text, algorithm='sha256'):
    hash_object = hashlib.new(algorithm)
    hash_object.update(text.encode('utf-8'))
    return hash_object.hexdigest()

text = input("Enter text to hash: ")
algorithm = input("Enter hash algorithm (default sha256): ") or "sha256"
print(f"Hash: {generate_hash(text, algorithm)}")
