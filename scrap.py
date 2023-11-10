import streamlit as st
import requests
from bs4 import BeautifulSoup

def scrape_shopee_products(keyword, location):
    url = f'https://shopee.co.id/search?keyword={keyword}&locations={location}&noCorrection=true&page=0'
    #https://shopee.co.id/search?keyword=baju&locations=Bali&noCorrection=true&page=0
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        product_list = []

        for product in soup.find_all('div', class_='col-xs-2-4 shopee-search-item-result__item'):
            product_details = {
                'name': product.find('div', class_='O6wiAW').text.strip(),
                'price': product.find('span', class_='VfPpfd ZdBevf i5DZme').text.strip(),
            }
            product_list.append(product_details)

        return product_list
    else:
        st.error(f"Failed to retrieve data. Status code: {response.status_code}")
        return []

# Streamlit app
def main():
    st.title('Shopee Product Scraper')
    keyword = st.text_input('Enter a keyword:')
    location = st.text_input('Enter a location:')

    if st.button('Scrape Products'):
        if keyword and location:
            products = scrape_shopee_products(keyword, location)
            st.write('Scraped Product Data:')
            st.write(products)
            st.write(requests.get(url))
        else:
            st.warning('Please enter a keyword and location.')

if __name__ == '__main__':
    main()
