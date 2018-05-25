import csv
import random

filename = "input_log.csv"



with open(filename) as csvfile:
    with open("output_log.csv", 'w') as outfile:
        file = csv.DictReader(csvfile, delimiter=";")
        field = file.fieldnames
        writer = csv.DictWriter(outfile, field)
        writer.writeheader()
        last_row = {}
        activity_name = ""


        random_list_of_row=list(file)

        random.shuffle(random_list_of_row)

        i=0

        for row in random_list_of_row[:3079]:
           
            if last_row == {} or (last_row["doctype"] != row["doctype"] or last_row["subprocess"] != row["subprocess"]):
                writer.writerow(row)
                i+=1
                

            last_row = row

            


        print(i)







