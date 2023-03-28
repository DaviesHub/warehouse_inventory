# Shoe Inventory Management System

## Description
This is a Python program that allows you to manage a shoe inventory system. You can perform various operations, including viewing all shoes, capturing new shoes, and re-stocking shoes.

## Contents
1. Description
2. Features
3. Package Requirements
4. Installation & Usage
5. Running the Application with Docker
6. Contributions
7. References

## Features
The code simulates a simple inventory management system for shoes in a warehouse. The code provides the following features:

- Creation of a shoe object - This allows the user to capture data about a new shoe product and create a new shoe object, which is appended to the existing list of shoes.

- Viewing all shoes - This feature allows the user to view a table containing all the shoes in the inventory.

- Restocking - This feature allows the user to find the shoe object with the lowest quantity and restock it by adding more shoes to its quantity. The quantity is then updated in the inventory file.

- Updating the inventory file - When new shoes are created or existing shoes are restocked, the changes are also written. to the inventory file.

- Searching for shoe - This feature allows a user to search for a shoe in the database via the product code.

- Value per item - This feature helps the user see the total worth of each item in the database.

- Highest quantity - This function determines the product with the highest quantity and prints this shoe as being for sale.

## Package Requirements
Package requirements for this app can be seen on the env_packages.txt file. Install the required packages by running the
following command on the command line:
'pip install -r env_packages.txt'

## Installation & Usage
To use the script, follow these steps:

1. Clone the repository to your local machine using git clone git clone git@github.com:Username/RepositoryName.git
2. Install the required packages by running pip install -r env_packages.txt in the project directory
3. Run the script using python inventory.py
4. When you run the program, you will see a menu with four options:

View all shoes
Capture a shoe
Re-stock shoes
Search for shoe
Value per item
Get product with highest quantity
Exit
Select one of the options by entering the corresponding letters.

5. If you select "View all shoes", the program will display a table with all the shoes in the inventory.

6. If you select "Capture a shoe", the program will prompt you to enter the details of the new shoe. After entering the details, the program will add the new shoe to the inventory.

7. If you select "Re-stock shoes", the program will find the shoe with the lowest quantity and prompt you to enter the quantity to add. After entering the quantity, the program will update the quantity of the shoe and the inventory file.

8. If you select "Search for shoes", the program will enable you to search for shoes via the product code.

9. If you select "Get product with highest quantity", the program will enable you to see the item with the highest quantity.

10. If you select "Exit", the program will exit.

## Running the Application with Docker
To run the script using Docker, follow these steps:

1. Make sure Docker is installed on your machine
2. Build the Docker image using docker build -t image-name.
3. Run the Docker container using docker run -it image-name

## Contributions
Contributions to this script are welcome. Please fork the repository, make changes, and submit a pull request.

## References
Docker documentation: https://docs.docker.com/
Python documentation: https://docs.python.org/