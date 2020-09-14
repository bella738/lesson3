2.
try:
    a = 1/0
except ZeroDivisionError:
    print("error")

3.
yes


6.
except IOError:
It is an error raised when an input/output operation fails,
such as the print statement or the open() function
when trying to open a file that does not exist.
It is also raised for operating system-related errors
except ZeroDivisionError:
when you division by zero

7.
my_file = open("/Users/bellamarkovitz/Documents/devops/lesson 3/words.txt","a",encoding="utf-8")
content = my_file.write("Bella Markovitz")
#8.
my_file = open("/Users/bellamarkovitz/Documents/devops/lesson 3/words.txt","r",encoding="utf-8")
content = my_file.read()
print(content)
my_file.close()
9.
my_hebrw_file = open("/Users/bellamarkovitz/Documents/devops/lesson 3/hebrw.txt","a",encoding="utf-8")
content = my_hebrw_file.write("שלום")
my_hebrw_file.seek(0)
my_hebrw_file = open("/Users/bellamarkovitz/Documents/devops/lesson 3/hebrw.txt","r",encoding="utf-8")
content = my_hebrw_file.read()
print(content)
my_hebrw_file.close()
11.
from PIL import Image

img = Image.new('RGB', (200,200), color = 'blue')
img.save('image_blue.png')
img.show()