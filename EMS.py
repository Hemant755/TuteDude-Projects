{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "1bf4a633-3330-4e73-af5c-e8b506924487",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Step 0: Initialize the dictionary with sample employee data\n",
    "employees = {101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000}}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "ac206d55-78ef-4afa-b924-6a9a7cd82f8f",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Step 1: Add Employee Functionality\n",
    "def add_employee():\n",
    "    emp_id = int(input(\"Enter Employee ID: \"))\n",
    "    if emp_id in employees:\n",
    "        print(\"Employee ID already exists!\")\n",
    "        return\n",
    "    name = input(\"Enter Name: \")\n",
    "    employees[emp_id] = name\n",
    "    print(\"Employee added successfully!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "2964edac-fd92-4603-a8bc-16de6d74ebc7",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Step 2: View All Employees\n",
    "def view_employees():\n",
    "    if not employees:\n",
    "        print(\"No employees available.\")\n",
    "    else:\n",
    "        print(\"Employee List:\")\n",
    "        for emp_id, name in employees.items():\n",
    "            print(f\"ID: {emp_id}, Name: {name}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "83ad23f3-3204-40b1-8188-047744d078ac",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Step 3: Search for an Employee by ID\n",
    "def search_employee():\n",
    "    emp_id = int(input(\"Enter Employee ID to search: \"))\n",
    "    if emp_id in employees:\n",
    "        print(f\"Employee Found: ID: {emp_id}, Name: {employees[emp_id]}\")\n",
    "    else:\n",
    "        print(\"Employee not found.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "4db4b5d4-d518-4eec-8c06-adda898073fe",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Step 4: Define the Menu System\n",
    "def main_menu():\n",
    "    while True:\n",
    "        print(\"\\n1. Add Employee\\n2. View All Employees\\n3. Search for Employee\\n4. Exit\")\n",
    "        choice = int(input(\"Enter your choice: \"))\n",
    "        if choice == 1:\n",
    "            add_employee()\n",
    "        elif choice == 2:\n",
    "            view_employees()\n",
    "        elif choice == 3:\n",
    "            search_employee()\n",
    "        elif choice == 4:\n",
    "            print(\"Goodbye!\")\n",
    "            break\n",
    "        else:\n",
    "            print(\"Invalid choice, try again.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "4faf56e2-3ec7-418a-8986-ec199fd2e128",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "1. Add Employee\n",
      "2. View All Employees\n",
      "3. Search for Employee\n",
      "4. Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice:  2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Employee List:\n",
      "ID: 101, Name: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000}\n",
      "\n",
      "1. Add Employee\n",
      "2. View All Employees\n",
      "3. Search for Employee\n",
      "4. Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice:  3\n",
      "Enter Employee ID to search:  101\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Employee Found: ID: 101, Name: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000}\n",
      "\n",
      "1. Add Employee\n",
      "2. View All Employees\n",
      "3. Search for Employee\n",
      "4. Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice:  4\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Goodbye!\n"
     ]
    }
   ],
   "source": [
    "# Implementing loop for the main_menu function\n",
    "if __name__ == \"__main__\":\n",
    "    main_menu()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e603df1c-ea49-46f2-9ecf-6c640ebfafe2",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
