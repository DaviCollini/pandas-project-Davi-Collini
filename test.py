import pandas as pd
from time import sleep
 
dbms = pd.read_excel("")
indexnumbers = dbms.shape[1]

#add a new row on the any index you want
user_inputs = []
for i in range(indexnumbers):
    user_input = input(f"Enter a value for a column {i+1}: ")
    user_inputs.append(user_input)

new_row = pd.DataFrame([user_inputs], columns=dbms.columns)
index1 = int(input("enter where you want that row: "))
insert_index = index1
newdbms1 = dbms.loc[:insert_index - 1]
newdbms2 = dbms.loc[insert_index:]

dbms = newdbms1._append(new_row, ignore_index=True)
dbms = pd.concat([dbms, newdbms2], ignore_index=True)

sleep(0.5)
print(dbms)
dbms.to_excel("DBMS.xlsx", index=False)