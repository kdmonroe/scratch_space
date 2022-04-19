
#!/usr/bin/python
# -*- coding: utf-8 -*-

# importing the necessary modules
import os
import requests
from bs4 import BeautifulSoup

# Creating a new file to store the zip file links
SAVE_PATH = "/Users/Monroe/Downloads"
USB_PATH = "/Volumes/SANDUSKY/PhillyLidar"
txt_name = 'zipfiles.txt'
zipfiles_fp = os.path.join(SAVE_PATH, txt_name)

BASE_URL = 'https://www.pasda.psu.edu/'
LAS_URL = 'https://www.pasda.psu.edu/download/phillyLiDAR/LAS2018/'

if not os.path.exists(zipfiles_fp):
    newfile = open(zipfiles_fp, 'w')

    # Set variable for page to be opened and url to be concatenated
    page = requests.get(LAS_URL)

    # Use BeautifulSoup to clean up the page
    soup = BeautifulSoup(page.content, features='html.parser')
    soup.prettify()

    # Find all the links on the page that end in .zip and write them into the text file
    for anchor in soup.findAll('a', href=True):
        links = anchor['href']
        if links.endswith('.zip'):
            newfile.write(links + '\n')
    newfile.close()
else:
    print(f"Text file of .zip already exists:\n{zipfiles_fp}")

# Fetching the links for the zip file and downloading the files

# TODO - create a list of .zip files from USB dir
existing_files = []
for root, dirs, files in os.walk(USB_PATH):
    for file in files:
        if file.endswith(".zip"):
            existing_files.append(os.path.join(root, file))

print(f'Found {len(existing_files)} existing .zip files:\n{existing_files}')

os.chdir(USB_PATH)

# TODO - print how many links exist in the text file

count = 0  # increment to count
with open(zipfiles_fp, 'r') as links:
    for link in links:
        if link:
            # TODO - check if file exist prior to downloading
            filename1 = link.split('/')[-1]
            filename = filename1[:-1]
            print(f"\t{count}. File name: {filename}")
            count += 1
print('Total # in text file: ' + str(count))

# link = BASE_URL + link
# print(filename + ' file started to download')
# response = requests.get(link[:-1])

# # Writing the zip file into local file system
# with open(filename, 'wb') as output_file:
#     output_file.write(response.content)
# print(filename + 'file is downloaded')
