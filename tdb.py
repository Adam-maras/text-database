import os
import sys
#start of the functions

arr = os.listdir()
arr2 = []
for file in arr:
    if file.endswith(".tdb"):
        arr2.append(file)
    else:
        pass
tdb_files = len(arr2)
if tdb_files == 1:
    solo_database = ''.join(arr2)
elif tdb_files == 0:
    pass
else: 
    print('There are too many databasees, you can only use one a the time (this will change in the next update)')
    sys.exit()


def existes():
    if tdb_files == 0:
        return False
    else:
        return True

def database(user_database_name):
    if tdb_files == 0:
        open(str(user_database_name) + '.tdb', 'w').close
        print('Database: ' + str(user_database_name) + '.tdb' + ' was succesfully created!')
    else:
        print('There are too many databasees, you can only use one a the time (this will change in the next update)')

def write(writing_request):
    f = open(solo_database, 'a')
    f.write(str(writing_request))
    f.close()

def overwrite(overwriting_request):
    f = open(solo_database, 'w')
    f.write(str(overwriting_request))
    f.close()

def name():
    return solo_database

def readline(line_to_read):
    myfile = open(solo_database , "r")
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
    
def read():
    f = open(solo_database, 'r')
    return f.read()

def delete():
    comfirmation = input('Are you sure that you want to delete ' + solo_database + '? (Y/N)').lower()
    if comfirmation == 'y':
        os.remove(solo_database)
        print('Database succesfuly deleted!')
    elif comfirmation == 'yes':
        os.remove(solo_database)
        print('Database succesfuly deleted!')
    else:
        print('I am not deleting ' + solo_database)