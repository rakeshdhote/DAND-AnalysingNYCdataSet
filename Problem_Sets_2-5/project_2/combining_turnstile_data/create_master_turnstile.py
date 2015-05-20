import csv

def create_master_turnstile_file(filenames, output_file):
    '''
    Write a function that takes the files in the list filenames, which all have the
    columns 'C/A, UNIT, SCP, DATEn, TIMEn, DESCn, ENTRIESn, EXITSn', and consolidates
    them into one file located at output_file.  There should be ONE row with the column
    headers, located at the top of the file.

    For example, if file_1 has:
    'C/A, UNIT, SCP, DATEn, TIMEn, DESCn, ENTRIESn, EXITSn'
    line 1 ...
    line 2 ...

    and another file, file_2 has:
    'C/A, UNIT, SCP, DATEn, TIMEn, DESCn, ENTRIESn, EXITSn'
    line 3 ...
    line 4 ...
    line 5 ...

    We need to combine file_1 and file_2 into a master_file like below:
     'C/A, UNIT, SCP, DATEn, TIMEn, DESCn, ENTRIESn, EXITSn'
    line 1 ...
    line 2 ...
    line 3 ...
    line 4 ...
    line 5 ...
    '''
    with open(output_file, 'w') as master_file:
       master_file.write('C/A,UNIT,SCP,DATEn,TIMEn,DESCn,ENTRIESn,EXITSn\n')
       wfile = csv.writer(master_file)

       for filename in filenames:
               rfileobject = csv.reader(open(filename,'rb'),skipinitialspace=True)

               for rowr in rfileobject:
                cinit = rowr[0:3][:]                    # first three column entries of each rowr
                rowr_len = len(rowr)                    # rowr length
                data_fix_incr = 5                       # fix data increment
                iterations = (rowr_len-3)/data_fix_incr

                for i in range(1, iterations+1):          #writing each row in the updated_+name file
                    roww = cinit + rowr[(i*data_fix_incr-2):((i+1)*data_fix_incr-2)][:]
                    wfile.writerow(roww)

if __name__ == "__main__":
    input_files = ['turnstile_110528.txt', 'turnstile_110604.txt']
    output = "turnstile_data_master.csv"
    create_master_turnstile_file(input_files, output)