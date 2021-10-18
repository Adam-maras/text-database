import os
import sys

arr = os.listdir()
arr2 = []
for file in arr:
    if file.endswith(".tdb"):
        arr2.append(file)
    else:
        pass
tdb_files = len(arr2)
if tdb_files == 1:
    multi_tdb = False
    solo_database = ''.join(arr2)
elif tdb_files == 0:
    solo_database = ''
elif tdb_files > 1:
    multi_tdb = True
    solo_database = ''

def existes():
    if tdb_files == 0:
        return False
    else:
        return True

def create(database_name):
    open(str(database_name) + '.tdb', 'w').close
    print('Database: ' + str(database_name) + '.tdb' + ' was succesfully created!')

def write(writing_request, database_to_write = solo_database):
    if multi_tdb == False:
        f = open(solo_database, 'a')
        f.write(str(writing_request))
        f.close()
    else:
        try:
            with open(database_to_write, 'a') as file:
                file.write(str(writing_request))
        except:
            print('Please spesify wich database to write to.')

def overwrite(overwriting_request, database_to_write = solo_database):
    if multi_tdb == False:
        with open(solo_database, 'w') as file:
            file.write(str(overwriting_request))
    else: 
        try:
            with open(database_to_write, 'w') as file:
                file.write(str(overwriting_request))
        except:
            print('Please spesify wich database to overwrite.')
    
def name():
    return solo_database

def readline(line_to_read, database_to_read = solo_database):
    myfile = ''
    if multi_tdb == False:
        myfile = open(solo_database , "r")
    else:
       myfile = open(database_to_read + '.tdb', 'r')

    myline = myfile.readline()
    i = 0
    while myline: 
        myline = myfile.readline()
        if i == int(line_to_read) - 2:
            return myline.replace('\n', '')
        else:
            pass
        i = i + 1
    myfile.close() 
    
def read(database_to_read = solo_database):
    if  multi_tdb == False:
        f = open(solo_database, 'r')
    else:
        try: 
            f = open(database_to_read + '.tdb', 'r')
        except:
            print('Please spesify the database')
    return f.read()

def delete(database_to_delete = solo_database):
    if multi_tdb == False:
        comfirmation = input('Are you sure that you want to delete ' + solo_database + '? (Y/N)').lower()
        if comfirmation == 'y':
            os.remove(solo_database)
            print('Database succesfuly deleted!')
        elif comfirmation == 'yes':
            os.remove(solo_database)
            print('Database succesfuly deleted!')
        else:
            print('I am not deleting ' + solo_database)
    else:
        try: 
            comfirmation = input('Are you sure that you want to delete ' + database_to_delete + '? (Y/N)').lower()
            if comfirmation == 'y':
                os.remove(database_to_delete + '.tdb')
                print('Database succesfuly deleted!')
            elif comfirmation == 'yes':
                os.remove(database_to_delete + '.tdb')
                print('Database succesfuly deleted!')
            else:
                print('I am not deleting ' + database_to_delete)
        except:
            print('Please spesify the database that you want to delete.')

#store vars

def add_var(var_to_write, database_to_write = solo_database):
    f = open(database_to_write, 'a')
    variable_name = [k for k, v in locals().items() if v == var_to_write][0]
    f.write(variable_name + '/' + var_to_write + '/' + str(type(var_to_write)))

def get_var(var_to_get, var_database = solo_database):
    pass
