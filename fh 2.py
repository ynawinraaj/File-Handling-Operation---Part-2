file_read=open('Codingal.txt','r')
print("file in read mode")
print(file_read.read())
file_read.close()

file_write=open('Codingal.txt','w')
file_write.write("file in read mode")
file_write.write("hi i am nawinraaj")
file_write.close()

file_append=open('Codingal.txt','w')
file_append.write("file in read mode")
file_append.write("hi i am nawinraaj.my age is 13")
file_append.close()