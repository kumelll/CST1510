
"""
RECORD CHECK  -  my version
===========================

Name  : KUMEL SHAIKH
Lane  :  AI
Date  : 09-10-2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
"""

# =================================================================== FUNCTIONS
# 1. Write a function called status_of(percent) that returns "OVER LIMIT"
#    (100% or more), "WARNING" (90% or more), or "OK" (anything else).
#
#    Typical and above: also write check(value, limit) that returns the
#    difference and the percentage as two values - do not print anything
#    inside it, only calculate and return.
#
#    Excellent: also write print_report(label, value, limit, difference,
#    percent, status) that does ALL of the printing below - nothing outside
#    it should contain a print() of its own, except the final count after
#    the loop ends.
#
#    Give each function a one-line docstring saying what it does.

def status_of(percent):
    """Return the status based on the percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


def check(value, limit):
    """Calculate and return the difference and percentage."""
    difference = limit - value
    percent = (value / limit) * 100
    return difference, percent


def print_report(label, value, limit, difference, percent, status):
    """Print the complete bordered record report."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"{'Rows loaded':<12}: {value:>8.2f}")
    print(f"{'Rows expected':<12}: {limit:>8.2f}")
    print(f"{'Difference':<12}: {difference:>8.2f}")
    print(f"{'Percent':<12}: {percent:>8.2f} %")
    print(f"{'Status':<12}: {status:>8}")
    print("=" * 34)


# ==================================================================== INPUT
# 2. Ask for your three values.
#
#    - the first is TEXT (dataset name) -> no conversion needed
#    - the second is a NUMBER (rows loaded) -> use float()
#    - the third is a NUMBER (rows expected) -> use float()
#
#    Excellent: repeat the input section inside a loop.
#    Type "quit" as the dataset name to stop entering records.

over_limit_count = 0

while True:
    label = input("Enter dataset name (or quit to stop): ")

    # Stop the loop if the user enters quit.
    if label.lower() == "quit":
        break

    value = float(input("Enter rows loaded: "))
    limit = float(input("Enter rows expected: "))


    # ================================================================== PROCESS
    # 3. Work out the difference, percentage, and status.
    #
    #    Call check() to calculate the difference and percentage.
    #    Call status_of() to get the status.
    #    Do not repeat calculations in different places.

    if limit == 0:
        print("Error: Cannot calculate percentage when rows expected is 0.")
        print("Please enter this record again.")
        continue

    difference, percent = check(value, limit)
    status = status_of(percent)


    # =================================================================== OUTPUT
    # 4. Print the report.
    #
    #    Excellent: call print_report() to print the complete report.
    #    Count how many records return "OVER LIMIT".
    #    Print the final count once, after the loop ends.

    print_report(label, value, limit, difference, percent, status)

    if status == "OVER LIMIT":
        over_limit_count += 1


# Print the total number of records that were over the limit.
print()
print("=" * 34)
print(f"Records OVER LIMIT: {over_limit_count}")
print("=" * 34)


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers.
#    [ ] Run it with a total of 0 and note the error.
#    [ ] Check every function does one job.
#    [ ] Check that calculation functions return values instead of printing.
#    [ ] Check that print_report() handles all report printing.
