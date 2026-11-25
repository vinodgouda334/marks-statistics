def validate_marks(marks):
    if len(marks) == 0:
        raise ValueError("Marks list cannot be empty")
    for m in marks:
        if m < 0 or m > 100:
            raise ValueError("Marks must be between 0 and 100")
    return marks


def total_marks(marks):
    marks = validate_marks(marks)
    return sum(marks)


def average_marks(marks):
    marks = validate_marks(marks)
    return total_marks(marks) / len(marks)


def highest_marks(marks):
    marks = validate_marks(marks)
    return max(marks)


def lowest_marks(marks):
    marks = validate_marks(marks)
    return min(marks)


# Main program
if __name__ == "__main__":
    print("----- MARKS STATISTICS -----")
    n = int(input("Enter number of subjects: "))
    marks = []
    for i in range(n):
        m = float(input("Enter marks of subject " + str(i + 1) + ": "))
        marks.append(m)
    print("\n----- STATISTICS SUMMARY -----")
    print("Total Marks   :", total_marks(marks))
    print("Average Marks :", round(average_marks(marks), 2))
    print("Highest Marks :", highest_marks(marks))
    print("Lowest Marks  :", lowest_marks(marks))
