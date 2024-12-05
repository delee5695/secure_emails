import sys

sys.set_int_max_str_digits(1000000)  # Increase limit as needed


def convert_message_to_int(message):
    """Convert message (str) to a single long integer."""
    converted_message = ""
    for i in message:
        int_letter = "{:03d}".format(
            ord(i)
        )  # Convert single letter to zero-padded ASCII
        converted_message += int_letter
    return int(converted_message)  # Return as integer


def convert_int_to_message(int_message):
    """Convert the long integer back to the original message."""
    # Increase the max string length for integer conversion
    str_message = str(int_message)
    original_message = ""
    for i in range(0, len(str_message), 3):
        original_message += chr(int(str_message[i : i + 3]))

    return original_message


# Example Usage
original_message = "hello" * 1000  # Example of a very long message
int_message = convert_message_to_int(original_message)
decoded_message = convert_int_to_message(int_message)

print("Decoded Message:", decoded_message)
