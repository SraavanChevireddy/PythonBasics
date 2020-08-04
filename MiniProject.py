import sys
from urllib.request import urlopen


# This project uses commandline arguments to use them

# http://sixty-north.com/c/t.txt   --- Use this URL from the Command line to know how the module works.

def fetch_words(url):
    # Opening a URL Connection from the 'urllib.request import urlopen' library.
    story = urlopen(url)
    story_words = []
    for line in story :
        line_words = line.split()
        for word in line_words:
            story_words.append(word)
    story.close() # Its equally important to close a URL Connection like opening it. 
    return story_words
 

def print_words(story_words):
     for word in story_words:
         print(word) # These are the words that are obtained from the strory words


def main():
    url = sys.argv[1] # This gets the URL from the Command line argument.
    words = fetch_words(url)
    print_words(words)

# To run this as a separate module, use dunders in the `main` script.
# Type in the __main__ key word to get the block as a snippet.

if __name__ == "__main__":
    main() 
