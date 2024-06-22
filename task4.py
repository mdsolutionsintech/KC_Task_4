import os
import subprocess

# Define the users and their groups
users = {
    "Andrew": "System Administrator",
    "Julius": "Legal",
    "Chizi": "Human Resource Manager",
    "Jeniffer": "Sales Manager",
    "Adeola": "Business Strategist",
    "Bach": "CEO",
    "Gozie": "IT intern",
    "Ogochukwu": "Finance Manager"
}

# Define the company directories
directories = [
    "Finance Budgets",
    "Contract Documents",
    "Business Projections",
    "Business Models",
    "Employee Data",
    "Company Vision and Mission Statement",
    "Server Configuration Script"
]

# Function to create a user and assign them to a group (for Windows)
def create_user(username, group):
    try:
        subprocess.run(['net', 'user', username, '/add'], check=True)
        subprocess.run(['net', 'localgroup', group, username, '/add'], check=True)
        print(f"User {username} created and added to group {group}.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to create user {username}: {e}")

# Function to create directories
def create_directories(directories):
    for directory in directories:
        try:
            os.makedirs(directory, exist_ok=True)
            print(f"Directory {directory} created.")
        except OSError as e:
            print(f"Failed to create directory {directory}: {e}")

# Function to create a file in a given directory if it exists
def create_file_in_directory(file_name, directory):
    if directory in directories:
        try:
            with open(os.path.join(directory, file_name), 'w') as file:
                file.write("")  # Create an empty file
            print(f"File {file_name} created in {directory}.")
        except IOError as e:
            print(f"Failed to create file {file_name} in {directory}: {e}")
    else:
        print(f"Directory {directory} is not a valid company directory.")

# Main function to create users and directories
def main():
    # Create users
    for user, group in users.items():
        create_user(user, group)

    # Create directories
    create_directories(directories)

    # Create file based on user input
    file_name = input("Enter the name of the file to create: ")
    directory = input("Enter the directory to create the file in: ")
    create_file_in_directory(file_name, directory)

if __name__ == "__main__":
    main()
