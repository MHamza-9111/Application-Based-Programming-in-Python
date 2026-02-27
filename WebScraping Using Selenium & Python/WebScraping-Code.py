from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://books.toscrape.com/")
time.sleep(5)

all_images = []
all_ratings = []
all_titles = []
all_prices = []

books = driver.find_elements("class name","product_pod")

for book in books:

    image_element = book.find_element("tag name","img")
    image = image_element.get_attribute("src")

    rating_element = book.find_element("class name","star-rating")
    rating = rating_element.get_attribute("class")

    title = book.find_element("tag name","h3").text

    price = book.find_element("class name","price_color").text

    all_images.append(image)
    all_ratings.append(rating)
    all_titles.append(title)
    all_prices.append(price)

print("Image-Links:",all_images)
print("Star-Ratings:",all_ratings)
print("Titles:",all_titles)
print("Prices:",all_prices)