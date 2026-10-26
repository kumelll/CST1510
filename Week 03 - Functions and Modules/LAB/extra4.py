
import statistics as stats

values = list(map(float, input("Enter five numbers separated by spaces: ").split()))

print("Values:", ", ".join(f"{x:g}" for x in values))
print(f"Total = {sum(values):.2f}")
print(f"Mean = {stats.mean(values):.2f}")
print(f"Median = {stats.median(values):.2f}")
print(f"Std Dev = {stats.stdev(values):.2f}")
