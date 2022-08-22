# All utility function will be here


def remove_special_chars_from_string(text: str) -> str:
    return "".join(e for e in text if e.isalnum())
