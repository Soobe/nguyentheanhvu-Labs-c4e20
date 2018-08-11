import pyexcel

a_list_of_dictionaries = [
     {
        "Name": 'thai',
         "Age": 28
     },
     {
         "Name": 'tuan anh',
         "Age": 29
     },
     {
         "Name": 'vu',
         "Age": 30
     },
     {
        "Name": 'Dean',
        "Age": 26
     }
 ]
pyexcel.save_as(records=a_list_of_dictionaries, dest_file_name="testpy.xlsx")