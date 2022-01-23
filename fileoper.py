# fp = open('input.txt','r')
# content = fp.read()
# print(content)
# fp = open('input.txt','r')
# content = fp.readlines()
# print(content[:5])
# content = fp.readline()
# print(content)
fp = open('input1.txt','w')
fp.write('write this line to the file')

fp = open('input3.txt','w+')
content= fp.read()
print(fp.tell())
print(content)


