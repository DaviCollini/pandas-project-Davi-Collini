# to clean a NaN and other features
    if r1 == 12:
     while True:
        r4 = int(input('''[0] TO GO BACK
[1] DROP ALL ROW THAT HAVE NaN/NONE VALUES
[2] DROP EMPTY ROW
[3] FILL THE NaN TO 0 
[4] RESET INDEX
        '''))
        if r4 == 0:
            break
        if r4 == 1:
            dbms.dropna()
            print(dbms)
        if r4 == 2:
            dbms.dropna(how="all")
            print(dbms)
        if r4 == 3:
            dbms.fillna(0)
            print(dbms)
        if r4 == 4:
            dbms.reset_index
            print(dbms)
