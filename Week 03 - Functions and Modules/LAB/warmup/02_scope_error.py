# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

def check(value, limit):
    if value > limit:
        return "OVER LIMIT"  
    else:
        return "OK"

print(check(87, 100))

