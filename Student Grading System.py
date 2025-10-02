class GradingSystem:
    def __init__(self):
        self.grades = []

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            print("Invalid grade ignored!")

    def calculate(self):
        if not self.grades:
            print("No valid grades entered!")
            return

        average = sum(self.grades) / len(self.grades)
        point_grade = ((100 - average) + 10) / 10

        if average < 50:
            remarks = "Dropped"
        elif average < 75:
            remarks = "Failed"
        elif 75 <= average <= 79:
            remarks = "Passed – Satisfactory"
        elif 80 <= average <= 84:
            remarks = "Passed – Good"
        elif 85 <= average <= 89:
            remarks = "Passed – Average"
        elif 90 <= average <= 99:
            remarks = "Passed – Very Good"
        elif average == 100:
            remarks = "Passed – Excellent"
        else:
            remarks = "Invalid"

        print("\nGrades entered:", self.grades)
        print(f"Average Grade: {average:.2f}")
        print(f"Point Grade: {point_grade:.2f}")
        print("Remarks:", remarks)

# Example usage
gs = GradingSystem()
while True:
    g = float(input("Enter grade (-1 to stop): "))
    if g == -1:
        break
    gs.add_grade(g)

gs.calculate()
