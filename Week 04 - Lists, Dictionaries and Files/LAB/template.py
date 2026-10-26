
"""
RECORD CHECK  -  my version
===========================

Name  : KUMEL SHAIKH
Lane  :  AI 
Date  : 17-10-2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

def check_record(value, limit):
    """Calculate the difference, percentage and status of a record."""
    difference = limit - value
    percent = (value / limit) * 100

    if value > limit:
        status = "OVER LIMIT"
    else:
        status = "OK"

    return difference, percent, status


def print_report(label, value, limit, difference, percent, status):
    """Print the complete report for one record."""
    print(f"Label: {label}")
    print(f"Value: {value}")
    print(f"Limit: {limit}")
    print(f"Difference: {difference}")
    print(f"Percentage: {percent:.2f}%")
    print(f"Status: {status}")
    print("-" * 30)


# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.

def load_records(path):
    """Load records from a file and return a list of dictionaries."""
    records = []

    with open(path, "r") as file:
        for line in file:
            label, value, limit = line.strip().split(",")

            records.append({
                "label": label,
                "value": float(value),
                "limit": float(limit)
            })

    return records


try:
    records = load_records("records_data.txt")
except FileNotFoundError:
    print("Error: records_data.txt was not found.")
    records = []


# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

results = []
over_limit_count = 0

for record in records:
    difference, percent, status = check_record(
        record["value"],
        record["limit"]
    )

    print_report(
        record["label"],
        record["value"],
        record["limit"],
        difference,
        percent,
        status
    )

    results.append((record["label"], status))

    if status == "OVER LIMIT":
        over_limit_count += 1


# Write the results to a new file
with open("results.txt", "w") as file:
    for label, status in results:
        file.write(f"{label},{status}\n")


# Print the final count after the loop
print(f"Total records: {len(records)}")
print(f"Records OVER LIMIT: {over_limit_count}")
print("Results saved to results.txt")


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
