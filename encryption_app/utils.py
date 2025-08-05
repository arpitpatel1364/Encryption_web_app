import random
import json


def encrypt_to_custom(text, custom_map):
    """Step 1: Plain text to custom codes"""
    try:
        return [custom_map[char] for char in text.lower()]
    except KeyError as e:
        return f"Unsupported character in text: {e}"


def decrypt_from_custom(code_list, custom_map):
    """Step 3: Custom codes to plain text"""
    try:
        reverse_map = {v: k for k, v in custom_map.items()}
        return ''.join(reverse_map[int(code)] for code in code_list)
    except KeyError as e:
        return f"Code not in decrypt map: {e}"
    except:
        return "Invalid input format."


def custom_to_secret_key(custom_codes, channel_id):
    """Step 2: Custom codes to secret key using XOR with channel-specific seed"""
    if isinstance(custom_codes, str):
        return custom_codes  # Return error message if any

    secret_key = []
    seed = 12345 + channel_id  # Channel-specific seed
    random.seed(seed)

    for code in custom_codes:
        xor_value = random.randint(1000, 9999)
        secret_value = code ^ xor_value
        secret_key.append(secret_value)

    return secret_key


def secret_key_to_custom(secret_key, channel_id):
    """Step 2 reverse: Secret key to custom codes using XOR with same seed"""
    try:
        seed = 12345 + channel_id
        random.seed(seed)

        custom_codes = []
        for secret_value in secret_key:
            xor_value = random.randint(1000, 9999)
            original_code = secret_value ^ xor_value
            custom_codes.append(original_code)

        return custom_codes
    except:
        return "Error converting secret key to custom codes"


def full_encrypt(text, channel):
    """Complete encryption: Plain text → Custom codes → Secret key"""
    custom_map = channel.get_custom_map()

    # Step 1: Text to custom codes
    custom_codes = encrypt_to_custom(text, custom_map)
    if isinstance(custom_codes, str):
        return custom_codes

    # Step 2: Custom codes to secret key
    secret_key = custom_to_secret_key(custom_codes, channel.id)
    return secret_key


def full_decrypt(secret_key, channel):
    """Complete decryption: Secret key → Custom codes → Plain text"""
    custom_map = channel.get_custom_map()

    # Step 1: Secret key to custom codes
    custom_codes = secret_key_to_custom(secret_key, channel.id)
    if isinstance(custom_codes, str):
        return custom_codes

    # Step 2: Custom codes to plain text
    plain_text = decrypt_from_custom(custom_codes, custom_map)
    return plain_text


def parse_secret_key_input(user_input):
    """Parse user input for secret key"""
    try:
        cleaned_input = user_input.strip().strip("[]")
        if not cleaned_input:
            return []
        codes = [int(x.strip()) for x in cleaned_input.split(',')]
        return codes
    except:
        return None