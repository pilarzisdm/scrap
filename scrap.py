import streamlit as st
import requests
from bs4 import BeautifulSoup

# Function to scrape product data from Shopee for a specific location using requests and BeautifulSoup
def scrape_shopee_products(keyword, location):
    # Define the URL with the specified keyword and location
    url = f'https://shopee.co.id/search?keyword={keyword}&locations={location}&noCorrection=true&page=0'

    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract product details
        product_list = []

        for product in soup.find_all('div', class_='product'):
            product_details = {
                'name': product.find('div', class_='product-name').text,
                'price': product.find('div', class_='product-price').text,
            }

            # You can add more fields as needed

            product_list.append(product_details)

        return product_list

    else:
        st.error('Failed to retrieve data. Please check the URL or try again later.')

# Streamlit app
def main():
    st.title('Shopee Product Scraper')
    keyword = st.text_input('Enter a keyword:')
    location = st.text_input('Enter a location:')
    
    if st.button('Scrape Products'):
        if keyword and location:
            products = scrape_shopee_products(keyword, location)
            if products:
                st.write('Scraped Product Data:')
                st.write(products)
        else:
            st.warning('Please enter a keyword and location.')

if __name__ == '__main__':
    main()
