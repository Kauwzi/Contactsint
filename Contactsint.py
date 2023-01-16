import requests
from bs4 import BeautifulSoup

# Read the list of websites from a text file
with open("websites.txt") as f:
    websites = f.readlines()
websites = [x.strip() for x in websites]  # remove newline characters

for url in websites:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    # Find all the elements on the page with the class "contact"
    contacts = soup.find_all(class_="contact")

    # Iterate through the contact elements and print their text
    for contact in contacts:
        print(contact.get_text())

    # Find all the phone number elements on the page
    phone_numbers = soup.find_all(class_="phone")

    # Iterate through the phone number elements and print their text
    for phone_number in phone_numbers:
        print(phone_number.get_text())

    # Find all the email address elements on the page
    email_addresses = soup.find_all(class_="email")

    # Iterate through the email address elements and print their text
    for email_address in email_addresses:
        print(email_address.get_text())