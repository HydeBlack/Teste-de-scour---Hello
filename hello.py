import requests
from bs4 import BeautifulSoup
import re

urls = ['https://en.wikipedia.org/wiki/Hello', 'https://en.wikipedia.org/wiki/World', 'https://en.wikipedia.org/wiki/This_Is_Us']
tags = ['p', 'h1', 'h2', 'h3', 'span']
hello_text = None
world_text = None

for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')  

    for tag in tags:
        elements = soup.find_all(tag)
        for element in elements:
            # Procura 'hello' e 'world' como expressões regulares nas tags
            hello_match = re.search(r'\bhello\b', element.get_text(), re.IGNORECASE)
            world_match = re.search(r'\bworld\b', element.get_text(), re.IGNORECASE)
            
            if hello_match and not hello_text:
                hello_text = hello_match.group(0)
                
            if world_match and not world_text:
                world_text = world_match.group(0)
                
            if hello_text and world_text:
                break
        
        if hello_text and world_text:
            break
    
    if hello_text and world_text:
        break

if hello_text and world_text:
    print(f"Esta é uma string interpolada: {hello_text}, {world_text}!")
else:
    print("Palavras 'hello' e 'world' não encontradas.")


