#!/usr/bin/env python3
"""
Check blog links in Latest news section
"""

from bs4 import BeautifulSoup

# Read the HTML file
with open('23-index.html', 'r') as f:
    content = f.read()

soup = BeautifulSoup(content, 'html.parser')

# Find the Latest news section
latest_news = soup.find('section', id='latest_news')

if latest_news:
    # Find all articles inside Latest news
    articles = latest_news.find_all('article')
    
    # Expected texts in order
    expected = ['Career', 'Digital Life', 'Social']
    
    # Check each article's link
    for i, article in enumerate(articles):
        link = article.find('a')
        if link and link.text.strip() == expected[i]:
            if i == 0:
                print("first link is correct")
            elif i == 1:
                print("second link is correct")
            elif i == 2:
                print("third link is correct")
