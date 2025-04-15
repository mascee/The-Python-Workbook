# This program capitalizes letters correctly.

def capitalize(text):
    result = list(text)

    # Capitalize the first non-space character
    pos = 0
    while pos < len(result) and result[pos] == ' ':
        pos += 1
    if pos < len(result):
        result[pos] = result[pos].upper()

    # Capitalize the first non-space character after '.', '!', or '?'
    pos = 0
    while pos < len(result):
        if result[pos] in '.!?':
            next_pos = pos + 1
            # Skip any spaces
            while next_pos < len(result) and result[next_pos] == ' ':
                next_pos += 1
            if next_pos < len(result):
                result[next_pos] = result[next_pos].upper()
            pos = next_pos
        else:
            pos += 1

    # Capitalize standalone "i"
    pos = 1
    while pos < len(result) - 1:
        if result[pos - 1] == " " and result[pos] == "i" and result[pos + 1] in [" ", ".", "!", "?", "'"]:
            result[pos] = "I"
        pos += 1

    return ''.join(result)

def main():
    text = input("Enter some text: ")
    capitalized = capitalize(text)
    print(f"Here is the corrected version: {capitalized}")

main()