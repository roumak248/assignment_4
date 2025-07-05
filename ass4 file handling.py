try:
    file1=open('sample.txt','r')
    reading_file=file1.readline()
    print('Line 1: ',reading_file)
    reading_file=file1.readline()
    print('Line 2: ',reading_file)
    file1.close()
except:
    print('the file sample.txt was not found')
finally:
    print('\nThank you for checking my assignment.')
