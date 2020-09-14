my_file = open("/Users/bellamarkovitz/Desktop/1.txt",'r+',encoding='UTF8')
content = my_file.write("Desler 9 bnei brak")
my_file.seek(0)# mooved score to the first line
content = my_file.read()
print(content)