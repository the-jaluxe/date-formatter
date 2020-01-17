# Date Formatter
Python console app that displays the current date based on the chosen country's format.

## Purpose

Want to know how the date format changes based on a given country? Simply, run this python application to see how it changes based on the supported countries. Each country has their own specific date format whether it be the month or day first that is determined in the ISO 8601 format.

## How It Works

The application recives a string of text from standard input from the user and checks if it is a non-case senstitive country one of the given arrays:

`endianessB = ["Bhutan", "China", "Koreas", "Canada", "Taiwan", "Hungary", "Iran", "Japan", "Lithuania", "Mongolia"]`

`endianessL = ["Asia", "Australia", "New Zealand", "Latin America", "North Africa", "India", "Indonesia", "Bangladesh", "Russia"]`

`endianessM = ["United States", "Philippines", "Marshall Islands"]`

The user can type "?" to see a list of supported countries. Each of the countries in the arrays have the same date format. **Big-endian** or `endianessB` has the format as **YEAR-MONTH-DAY**. **Little-endian** or `endianessL` has the format as **DAY-MONTH-YEAR**. **Middle-endian** or `endianessM` has the format as **MONTH-DAY-YEAR**.

Once the user enters a valid country, the program displays the current time using Python's built-in datetime package in the format of the user's country. 

Additionally, it also counts the number of ambiguous days with other date formats. For example, `endianessL` can have a date as 9-12-2020 or December 9, 2020 whereas `endianessM`interprets that same date as September 12, 2020 which is an ambiguous day. We see that `endianessB` has no ambiguous days because it starts with the year which is a reason why everyone should switch to that date format.

## Technologies Used

- Python
- Packages: datetime
- Data Strucutres: array
- Object-Oriented Design with resusuable functions
- User-friendly prompts and no input breaks the code
- Fundamentals such as loops, comparisons, and standard output
