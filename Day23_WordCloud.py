import sys
import numpy as np
from PIL import Image
import wikipedia
from wordcloud import WordCloud, STOPWORDS
import os

def main():
    try:
        topic = input("Enter the name of which you want to make a word cloud: ").strip()
        if not topic:
            print("No input provided.")
            return

        search_results = wikipedia.search(topic)
        if not search_results:
            print("No results found on Wikipedia.")
            return

        title = search_results[0]
        page = wikipedia.page(title)
        text = page.content
        print(f"Generating word cloud for: {title}")

        if not os.path.exists("abcd.jpg"):
            print("Background image 'abcd.jpg' not found.")
            return

        bg = np.array(Image.open("abcd.jpg"))
        unwanted_words = set(STOPWORDS)

        wordcloud = WordCloud(
            background_color="black",
            max_words=400,
            mask=bg,
            stopwords=unwanted_words,
            contour_width=1,
            contour_color='white'
        ).generate(text)

        wordcloud.to_file("sample.png")
        print("Word cloud saved as sample.png")

    except wikipedia.exceptions.DisambiguationError as e:
        print(f"Disambiguation error: {e}")
    except wikipedia.exceptions.PageError:
        print("Page not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
