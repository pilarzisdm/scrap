import streamlit as st
import requests
from bs4 import BeautifulSoup

# Function to scrape shop data
def scrape_shops(location):
    # Define the URL with the specified location
    url = f'https://www.shopee.co.id/shops?location={location}'
    
    # Send an HTTP GET request to the website
    response = requests.get(url)
    
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract shop details
    shop_list = []
    
    for shop in soup.find_all('div', class_='shop'):
        shop_details = {
            'name': shop.find('h3').text,
            'address': shop.find('p', class_='address').text,
            'description': shop.find('p', class_='description').text,
        }
        
        # Check if the shop is in the desired location
        if location in shop_details['address']:
            shop_list.append(shop_details)
    
    return shop_list

# Streamlit app
def main():
    st.title('Web Scrap Online Shop E-Commerce')
    location = st.text_input('Masukan lokasi:')
    
    if st.button('Scrap Toko'):
        if location:
            shops = scrape_shops(location)
            st.write('Data Hasil Scrap:')
            st.write(shops)
        else:
            st.warning('Please enter a location.')

if __name__ == '__main__':
    main()
