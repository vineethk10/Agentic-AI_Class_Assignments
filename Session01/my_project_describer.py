
# Welcome message
print("Welcome to My Project Describer!")

print("Answer 3 questions about your Job Application Tracker project:\n")

# Prompt user for the number of job applications they plan to track - String
num_applications = input("How many job applications will you track? ")

# Convert the string input to an integer
num_applications = int(num_applications)

# Ask user which job platforms they will use for searching and tracking - String
job_platforms = input("What job platforms are you using? ")

# Get users goal - String
main_goal = input("What is your main goal in building this tracker?")

# Display the data type of num_applications to demonstrate that conversion was successful and show type
print(f"Type of 'num_applications': {type(num_applications)}")

# Create a visual separator
print("=" * 150)
# Create first paragraph that combines user inputs
paragraph1= f"My Job Application Tracker will monitor {num_applications} applications across {job_platforms}. I am building this tracker to {main_goal}, allowing me to stay organized and focused in my job search journey."
# Display the first paragraph so user sees their project described in their own words
print(paragraph1)
# Create second paragraph
paragraph2 = f"This project focuses on {job_platforms.upper()} opportunities and ensures I achieve my core objective: {main_goal.title()}."
# Display the second paragraph
print(paragraph2)
# Create another visual separator
print("=" * 150)
