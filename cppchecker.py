# -*- coding: utf-8 -*-
__author__ = 'Larissa Raimee Gomes'
__date__ = '2024-06'
__copyright__ = 'Copyright (c) Larissa Raimee 2024 All Rights Reserved.'

import os
import subprocess
import platform

def cppcheck_checker(file, output_file):
    # Run cppcheck on the specified file and capture the output and errors
    result = subprocess.Popen(["cppcheck", file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = result.communicate()

    # Write file header in HTML
    output_file.write("<h2>Issues found in: {}</h2>\n".format(file))

    # If there are errors, write them to the output file in a formatted way
    if error:
        output_file.write("<pre>{}</pre>\n".format(error.decode("utf-8")))
    else:
        output_file.write("<p>No issues found.</p>\n")
        if output:
            output_file.write("<pre>{}</pre>\n".format(output.decode("utf-8")))

# Function to recursively check all files in a folder
def folders(folder, output_file):
    for item in os.listdir(folder):
        item_path = os.path.join(folder, item)
        # If it's a directory, recursively check its contents
        if os.path.isdir(item_path):
            folders(item_path, output_file)
        # If it's a file with a C/C++ extension, run the cppcheck_checker on it
        elif os.path.isfile(item_path) and item.lower().endswith(('.cpp', '.cc', '.c', '.h', '.hpp', '.cxx', '.hh', '.hxx', '.h++', '.cppm', '.ixx')):
            cppcheck_checker(item_path, output_file)

# Function to remove pycache directories on Linux
def remove_pycache_linux():
    result = subprocess.Popen(["find", ".", "-type", "d", "-name", "__pycache__"], stdout=subprocess.PIPE)
    output, _ = result.communicate()
    pycache_directories = output.splitlines()
    for directory in pycache_directories:
        subprocess.Popen(["rm", "-rf", directory])

# Function to remove pycache on Windows
def remove_pycache_windows():
    subprocess.Popen(["powershell", "-Command", 
    "Get-ChildItem -Path . -Recurse -Directory -Filter '__pycache__' | Remove-Item -Recurse -Force"])

# Set the path for the output HTML file
current_folder = os.path.dirname(os.path.abspath(__file__))
output_file_path = os.path.join(current_folder, "output.html")

# Open the output file and write the HTML structure
with open(output_file_path, "w", encoding="utf-8") as output_file:
    output_file.write("<html><head><title>Cppcheck Results</title></head><body>\n")
    output_file.write("<h1>Cppcheck Analysis Report</h1>\n")

    folders(current_folder, output_file)

    output_file.write("</body></html>")

print("The HTML report was written to the file: {}".format(output_file_path))

# Remove __pycache__ directories based on the current OS
if platform.system() == "Linux":
    remove_pycache_linux()
elif platform.system() == "Windows":
    remove_pycache_windows()