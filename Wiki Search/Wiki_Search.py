"""
pip install wikipedia
pip install wikipedia-api
"""

import wikipedia

search = str(input("What Are You Looking For: "))

try:
    result = wikipedia.summary(search)
    print(result)
except wikipedia.exceptions.DisambiguationError as e:
    print(f"Ambiguous search query. Please choose one of the following options:")
    options = e.options
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
except wikipedia.exceptions.PageError:
    print(f"No page found for the search query: {search}")
except Exception as e:
    print(f"An error occurred: {e}")

