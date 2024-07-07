import re

def get_movies(data):
    # Define the pattern to match movie title and release year
    pattern = re.compile(r'(?P<title>.*?) \((?P<year>\d{4})\)')
    
    # Find all matches in the input string
    matches = pattern.findall(data)
    
    # Create a list of tuples containing movie title and release year
    movies = [(matchs[0].strip(), matchs[1]) for matchs in matches]
    
    return movies

if __name__ == "__main__":
    data = input().strip()
    print(get_movies(data))
