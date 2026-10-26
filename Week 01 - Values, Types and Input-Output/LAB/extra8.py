
season1_seconds = 10 * (45 * 60 + 35)
other_seasons_seconds = 40 * (35 * 60 + 15)

total_seconds = season1_seconds + other_seasons_seconds

hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print(f"Total time: {hours}h {minutes}m {seconds}s")
