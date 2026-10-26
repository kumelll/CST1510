
from pathlib import Path

path = Path(input("Enter a file or directory path: "))

print(f"Absolute path: {path.resolve()}")
print(f"Parent: {path.resolve().parent}")
print(f"Name: {path.name}")
print(f"Stem: {path.stem}")
print(f"Suffix: {path.suffix}")
