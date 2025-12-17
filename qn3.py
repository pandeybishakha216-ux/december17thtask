# Write a program that uses a for loop to iterate through the list student_names = ["Ram", "Hari", "Sita"] and prints a personalized message for each student in the format 'Hi [Name], your course approval is ready!'. Include the header ' --- Email Greetings Generated ---' before the loop.
student_names = ["Ram", "Hari", "Sita"]
print(" --- Email Greetings Generated ---")
for name in student_names:
    print(f"Hi {name}, your course approval is ready!")
print("-------------------------------")

