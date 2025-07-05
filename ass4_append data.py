a=input("Enter text to write to the file: ")
file1=open("output.txt","w")
writing_file=file1.write(a)
file1.close()
print("Data successfully written to output.txt")

b=input("Enter additional text to append: ")
file1=open("output.txt","w")
writing__file2=file1.write(b)
file1.close()
print("Data successfully appended")


print("Final content of output.txt: ",'\n'+ a+'\n'+b)