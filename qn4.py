#write a program that iterates through the list of chapter page counts [45, 30, 50, 40] and (starting the count at 1) to print a message for each chapter in the format: 'Chapter [Number] has [Pages] pages.'. Include the header '--- Book Chapter Summary ---'."
chapter_pages = [45, 30, 50, 40]
print("--- Book Chapter Summary ---")
for index, pages in enumerate(chapter_pages, start=1):
    print(f"Chapter {index} has {pages} pages.")
print("----------------------------")