"""
match-case is Python's version of a "switch" statement.
It compares ONE value against many possible options (cases).
Introduced in Python 3.10 -> won't work on older versions.

Think of it as a cleaner alternative to long if / elif / else
chains when you are checking the SAME variable again and again.

"""


# BASIC SYNTAX
#   match variable:
#       case value1:
#           # code
#       case value2:
#           # code
#       case _:
#           # default (runs if nothing else matched)
#
# NOTE: Indentation matters, just like if/else.


# Example 1: Simple day checker
day = "Mon"

match day:
    case "Mon":
        print("Start of the week")
    case "Fri":
        print("Almost weekend")
    case _:                      # _  = "wildcard" = default case
        print("Some other day")


# THE UNDERSCORE  ( _ )
# case _:  ->  matches ANYTHING that no other case caught.
# It works like the "else" block. It is optional but useful.


# Example 2: Multiple values in one case  (use  |  = OR)
day = "Sun"

match day:
    case "Sat" | "Sun":          # matches Saturday OR Sunday
        print("It's the weekend!")
    case _:
        print("It's a weekday")

# MATCHING NUMBERS

status = 404

match status:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:
        print("Unknown status")

# if / elif   VS   match-case  (same logic, two styles)

# --- Using if/elif ---
color = "red"
if color == "red":
    print("Stop")
elif color == "green":
    print("Go")
else:
    print("Wait")

# --- Same thing using match-case (cleaner) ---
match color:
    case "red":
        print("Stop")
    case "green":
        print("Go")
    case _:
        print("Wait")

