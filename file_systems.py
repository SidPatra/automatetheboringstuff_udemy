'''
File management, etc. in Python
'''
#path examples below
path1 = 'c:\\spam\\eggs.png' # this is a specifically windows path
print(path1)
print('\\') #will print single slash

print(r'c:\spam\eggs.png')# uses raw string, automatically prints path1 without needing double slashes

#problem from above: Windows uses '\', Mac/Linux uses '/'
# can we use something to make sure we can just normally use 
# whichever is appropriate regardless of OS?

path2 = '\\'.join(['folder1','folder2','folder3','file.png'])
print(path2)

import os

path3 = os.path.join('folder1','folder2','folder3','file.png')
# above path uses os to build a path depending on os being used. 
print(path3)

print(os.sep)#prints out the separator the os uses

print(os.getcwd())#current working directory

os.chdir('c:\\')#changes working directory to root
os.chdir(r'C:\Users\Siddharth_Patra\Documents\GitHub\automatetheboringstuff_udemy')#back to current
print(os.getcwd())

#2 types of filepaths: relative and absolute

#Relative: is relative to the working directory, so will look in working directory
# It will also search relative to it. So, to go to the parent of working directory,
# just use .\. To go up 2 levels: ..\. 

file4 = os.path.abspath('file_systems.py')#abspath gets you the absolute path of a file or directory
file5 = os.path.abspath('..\\..\\file_systems.py')
print(file4)
print(file5)

file6 = os.path.isabs(r'C:\Users\Siddharth_Patra\Documents\GitHub\automatetheboringstuff_udemy')
print(file6) #isabs tells you wether a filepath is absolute or not. This should say true.

file7 = os.path.relpath(r'C:\Users\Siddharth_Patra\Documents\GitHub\automatetheboringstuff_udemy', r'c:\Users\Siddharth_Patra\Documents')
print(file7)#relpath gives you a relative path from the second param (which is like current working directory) to the first one.

file8 = os.path.dirname(r'C:\Users\Siddharth_Patra\Documents\GitHub\automatetheboringstuff_udemy/file_systems.py')
print(file8) #gets you directory name of a file

file9 = os.path.basename(r'C:\Users\Siddharth_Patra\Documents\GitHub\automatetheboringstuff_udemy')
print(file9) #gets you base directory in all of this

file10 = os.path.exists(r'C:\Users\Siddharth_Patra\Documents\GitHub\automatetheboringstuff_udemy/file_systems.py')
print(file10) #tells you if a file even exists

file11 = os.path.isfile(r'C:\Users\Siddharth_Patra\Documents\GitHub\automatetheboringstuff_udemy')
print(file11) #tells you if address passed in refers to a file -> T/F

file12 = os.path.isdir(r'C:\Users\Siddharth_Patra\Documents\GitHub\automatetheboringstuff_udemy')
print(file12) #tells you if address passed in refers to a folder -> T/F

file13 = os.path.getsize(r'C:\Users\Siddharth_Patra\Documents\GitHub\automatetheboringstuff_udemy')
print(file13) #gets size of file in bytes

file14 = os.listdir(r'C:\Users\Siddharth_Patra\Documents\GitHub\automatetheboringstuff_udemy')
print(file14) #prints out list of all the files in a directory

'''SAMPLE PROGRAM: Finding total size of all files in a folder'''

def prog():
    totalSize = 0
    for filename in os.listdir(r'C:\Users\Siddharth_Patra\Documents\GitHub\automatetheboringstuff_udemy'):
        if not os.path.isfile(os.path.join(r'C:\Users\Siddharth_Patra\Documents\GitHub\automatetheboringstuff_udemy',filename)):
            continue
        else:
            totalSize += os.path.getsize(os.path.join(r'C:\Users\Siddharth_Patra\Documents\GitHub\automatetheboringstuff_udemy',filename))
    return totalSize

print(prog())


file15 = os.makedirs('c:\\Users\\Siddharth_Patra\\Documents\\GitHub\\automatetheboringstuff_udemy\\stuff1\\stuff2\stuff3')
print(file15)