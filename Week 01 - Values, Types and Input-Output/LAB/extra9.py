
weekly_saving = 10
weeks = 52
savings = 0

savings += (weekly_saving + 20) * weeks
savings -= (weeks // 2) * 0.50

savings += weekly_saving * weeks * 2
savings -= (weeks * 2 // 2) * 0.50

print(f"Final savings after 3 years: £{savings:.2f}")
