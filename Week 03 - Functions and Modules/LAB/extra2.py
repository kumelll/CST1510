
def compress_string(text):
    """Compress repeated characters."""
    compressed = ""
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            compressed += text[i - 1] + str(count)
            count = 1

    if text:
        compressed += text[-1] + str(count)

    if len(compressed) >= len(text):
        return text

    return compressed


print(compress_string("aaabbbbcccddeee"))
print(compress_string("Hello"))
