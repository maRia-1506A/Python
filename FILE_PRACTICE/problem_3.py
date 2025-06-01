'''
Write a program to generate multiplication tables from 2 to 20 and write it to the different files. 
Place these files in a folder for a 13 – year old.
'''


def multiplication_tables(n):
    # Start with an empty string to collect lines
    table = ""

    # create multiplication table
    for i in range(1, 11):
        line = f"{n} x {i} = {n*i}\n"
        table += line  # Add each line to the table string

    # This opens (or creates) a file named something like table_2.txt inside the tables folder, in write mode ("w").
    with open(f"Tables/table_{n}.txt", "w") as f:
        f.write(table)


for i in range(2, 21):
    multiplication_tables(i)
