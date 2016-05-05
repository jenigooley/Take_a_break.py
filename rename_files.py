def rename_file():
    
    import os
    
    file_list =  os.listdir(r'Dropbox (Personal)/Jeni/alphabet')
    saved_path = os.getcwd()
    print saved_path
    os.chdir('Dropbox (Personal)/Jeni/alphabet')
    
    for file_name in file_list:
        os.rename(file_name,(file_name.translate(None, '0123456789')))
        print 'new file name:', file_name.translate(None, '01234456789')
    os.chdir(saved_path)    
   
rename_file()


 
