import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Function to scrape product data from Shopee for a specific location using Selenium
def scrape_shopee_products(keyword, location):
    # Define the URL with the specified keyword and location
    url = f'https://shopee.co.id/search?keyword={keyword}&locations={location}&noCorrection=true&page=0'

    # Create a Selenium WebDriver instance (you need to specify the path to your web driver)
    driver = webdriver.Chrome(executable_path='C:\Users\BPSAdmin\Downloads\chromedriver_win32')

    # Open the URL in the browser
    driver.get(url)

    # Wait for the page to load (you might need to adjust the wait time)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'product')))

    # Get the page source after it has fully loaded
    page_source = driver.page_source

    # Close the browser
    driver.quit()

    # Parse the HTML content of the page
    soup = BeautifulSoup(page_source, 'html.parser')

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
        else:
            st.warning('Please enter a keyword and location.')

if __name__ == '__main__':
    main()
