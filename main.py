import pandas as pd
from IPython.display import display
from time import sleep
r1 = r2 = r3= ""
dbms = pd.read_excel("DBMS.xlsx")

print(dbms.head(5))
sleep(0.5)
print("Hello, this is my project on Pandas, let's se if i can help you")
sleep(1)
while True:
    sleep(0.5)

    r1 = int(input('''ENTER A NUMBER TO SEE THE SECTIONS: 
[0] EXIT THE PROGRAM 
[1] SEE ALL SPREADSHEET 
[2] ADD NEW ROW WHERE DO YOU WANT
[3] ADD NEW ROW
[4] SEE OPTIONS TYPE 
[5] DROP THE LAST ROW
[6] DROP ROW WHERE DO YOU WANT
[7] DROP THE LAST COLUMN
[8] ENTER TO SEARCH ON A ROW
[9] SEE ONLY THE RESULT SEARCH YOU WANT
[10] EDIT A ROW
[11] SORT OPTIONS
ENTER A OPTION: '''))

    if r1 == 0:
        print("ENDING THE PROGRAM !")
        sleep(1)
        break

    if r1 == 1:
        print(dbms)

    if r1 == 2:
        index1 = int(input("enter where you want that row: "))
        N1 = int(input("Enter a serial number: "))
        N2 = input("Enter a name: ")
        N3 = int(input("Enter the numbers of unit : "))
        N4 = input("Enter DBMS state and city: ")
        N5 = input("Enter type of DBMS: ")
        N6 = input("Enter creation date: ")
        new_row = ({
            " Serial number": [N1],
            "Name": [N2],
            "Unit(s)": [N3],
            "DBMS place": [N4],
            "Type": [N5],
            "Creation date": [N6]})
        insert_index = index1
        newdbms1 = dbms.loc[:insert_index - 1]
        newdbms2 = dbms.loc[insert_index:]
        
    
        dbms = newdbms1._append(new_row, ignore_index=True)
        dbms = pd.concat([dbms, newdbms2], ignore_index=True)
        sleep(0.5)
        print(dbms)
        dbms.to_excel("DBMS.xlsx", index=False)

    if r1 == 3:
            '''to add new row'''
            n1 = int(input("Enter a serial number: "))
            n2 = input("Enter a name: ")
            n3 = int(input("Enter the numbers of unit : "))
            n4 = input("Enter DBMS state and city: ")
            n5 = input("Enter type of DBMS: ")
            n6 = input("Enter creation date: ")
            new_row = ({
                " Serial number": [n1],
                "Name": [n2],
                "Unit(s)": [n3],
                "DBMS place": [n4],
                "Type": [n5],
                "Creation date": [n6]})
            dbms = dbms._append(new_row, ignore_index=True)
            sleep(0.5)
            print(dbms)
            dbms.to_excel("DBMS.xlsx", index=False)


    if r1 == 4:
        while True:
            sleep(0.5)
            r2 = int(input('''
[0] TO GO BACK
[1] SEE NoSQ LINES 
[2] SEE distributed SQL LINES
[3] SEE THE OTHER LINES: '''))
            if r2 == 0:
                break
            if r2 == 1:
                print(dbms.loc[dbms['Type'] == "NoSQL"])
            if r2 == 2:
                print(dbms.loc[dbms['Type'] == "distributed SQL"])

            if r2 == 3:
                dbms_filtered = dbms[~dbms['Type'].isin(
                    ['distributed SQL', 'NoSQL'])]
                print(dbms_filtered)

    '''the drops, [5]drop the last row,[7] drop the last column [6] drop any row'''
    if r1 == 5:
        dbms = dbms.drop(dbms.index[-1])
        sleep(0.5)
        print(dbms)
    if r1 == 6:
        index_to_drop = int(input("enter a row you want to drop: "))
        dbms = dbms.drop(index_to_drop)
        print(dbms)

    if r1 == 7:
        dbms = dbms.drop(dbms.columns[-1], axis=1)
        sleep(0.5)
        print(dbms)

    if r1 == 8:
        while True:
            filter1 = input(
                "Enter a name to see results ('break' to go back): ")
            sleep(0.5)
            if filter1 == 'break':
                break
            filter2 = dbms[dbms.astype(str).apply(
                lambda column: column.str.contains(filter1, case=False, na=False)).any(axis=1)]
            if not filter2.empty:
                print(filter2)
            else:
                print("No results found.")

    if r1 == 9:
        while True:
            search_term = input(
                "enter a number, word or anything you want to search('break' to go back): ")
            search_results = []
            for index, row in dbms.iterrows():
                for column in dbms.columns:
                    cell_value = str(row[column])
                    if search_term in cell_value:
                        search_results.append((cell_value, index, column))
            if search_term == "break":
                break
            if search_results:
                for value, index, column in search_results:
                    print(
                        f"Value: {value}  |  Row: {index}  |  Column: {column}")
            else:
                print("No results found.")

    if r1 == 10:
        row_index = int(input("Enter the index of row to edit: "))
        if row_index < len(dbms):
            n1 = int(input("Enter a serial number: "))
            n2 = input("Enter a name: ")
            n3 = int(input("Enter the numbers of unit : "))
            n4 = input("Enter DBMS state and city: ")
            n5 = input("Enter type of DBMS: ")
            n6 = input("Enter creation date: ")

            dbms.at[row_index, " Serial number"] = n1
            dbms.at[row_index, "Name"] = n2
            dbms.at[row_index, "Unit(s)"] = n3
            dbms.at[row_index, "DBMS place"] = n4
            dbms.at[row_index, "Type"] = n5
            dbms.at[row_index, "Creation date"] = n6
        else:
            sleep(1)
            print("row index not found")
    sleep(1)
    print(dbms)
    dbms.to_excel("DBMS.xlsx", index=False)


    if r1 == 11:
        while True:
            r3 = int(input('''[0] TO GO BACK
[1] SORT "NAME" ALPHABETICALLY
[2] SORT "PLACE" ALPHABETICALLY
[3] SORT SERIAL NUMBER CRESCENT
[4] SORT SERIAL NUMBER DECRESCENT
[5] SORT THE UNIT'S CRESCENT
'''))
            if r3 == 0:
                break
            if r3 == 1:
                print(dbms.sort_values("Name"))
            if r3 == 2:
                print(dbms.sort_values("DBMS place"))
            if r3 == 3:
                dbms[" Serial number"] = dbms[" Serial number"].astype(int)
                print(dbms.sort_values(by=" Serial number",ascending=True))
            if r3 == 4:
                dbms[" Serial number"] = dbms[" Serial number"].astype(int)
                print(dbms.sort_values(by=" Serial number",ascending=False))
            if r3 == 5:
                dbms["Unit(s)"] = dbms["Unit(s)"].astype(int)
                print(dbms.sort_values(by="Unit(s)",ascending=False))
                
        