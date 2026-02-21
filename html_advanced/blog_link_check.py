#!/usr/bin/env python3
"""
Check blog links in HTML file
"""

from bs4 import BeautifulSoup

# Read the HTML file
with open('23-index.html', 'r') as f:
    content = f.read()

soup = BeautifulSoup(content, 'html.parser')

# Find the Latest news section
latest_news = soup.find('section', id='latest_news')
if latest_news:
    articles = latest_news.find_all('article')
    
    # Expected link texts
    expected_texts = ['Career', 'Digital Life', 'Social']
    
    for i, article in enumerate(articles):
        link = article.find('a')
        if link and link.text.strip() == expected_texts[i]:
            print(f"first link is correct" if i == 0 else 
                  f"second link is correct" if i == 1 else 
                  f"third link is correct")
