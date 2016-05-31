import urllib

def read_text():
    quotes = open("HD/Applications/TextEdit/movie_quotes")
    contents_of_file = quotes.read()
    print (contents_of_file)
    quotes.close()
    check_profanity()

def check_profanity():
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    print(output)
    connection.close()

read_text()
