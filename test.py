# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 22:08:44 2023

@author: jeanl
"""

import requests
import re

def download_webpage(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print("Falha ao fazer o download da página.")
        return None

def find_pdf_links(html_content):
    pdf_links = re.findall(r'<a\s+[^>]*href="([^"]*\.pdf)"', html_content, re.IGNORECASE)
    return pdf_links

if __name__ == "__main__":
    url = "https://www.jstor.org/stable/44547530"  # Substitua pela URL real que deseja analisar

    html_content = download_webpage(url)
    if html_content:
        pdf_links = find_pdf_links(html_content)

        if pdf_links:
            print("Links para arquivos PDF encontrados:")
            for link in pdf_links:
                print(link)
        else:
            print("Nenhum link para arquivo PDF encontrado.")