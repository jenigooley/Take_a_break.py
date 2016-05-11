import os
import random
import time


#organize files into message "stay rad"
#save in folder 
#add random ints to front of filenames
#save new names in folder 
#sremove ints from files

def mix_up_files():
    
    file_list = os.listdir(r'Dropbox (Personal)/Jeni/alphabet')
    print file_list
    saved_path = os.getcwd()
    print saved_path 
    os.chdir('Dropbox (Personal)/Jeni/alphabet')
    for file_name in file_list:
        os.rename(file_name,(str(random.randint(0,42)) + file_name))    
        os.open('Dropbox\ \(\Personal\)\/Jeni/alphabet')
    os.chdir(saved_path)


mix_up_files()
 
