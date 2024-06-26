import pywhatkit
import csv

# Define the path to your CSV file
csv_file_path = 'contacts.csv'
message_file_path = 'message.txt'

# Step 1: Open the file in read mode
message = ""
with open(message_file_path, 'r') as file:
    # Step 2: Read the entire file content into a string
    message = file.read()

# Open the CSV file and read its contents
numbers = []
with open(csv_file_path, mode='r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        numbers.append(row)

for number in numbers:

    phone_number = str(number[0])
    print(phone_number)
    text = message
    waiting_time_to_send = 8
    close_tab = True
    waiting_time_to_close = 8

    pywhatkit.sendwhats_image(phone_number, "picture.jpeg", text,waiting_time_to_send 
                                  , close_tab, waiting_time_to_close)
