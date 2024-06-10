import requests
from bs4 import BeautifulSoup

def scrape_hotel_names(url):
    # Send a GET request to the specified URL
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all elements with the specified class or tag that contain hotel names
    hotel_elements = soup.find_all(class_='f6431b446c a15b38c233')  # Replace 'hotel-name' with the actual class or tag name

    # Extract the hotel names from the elements
    hotel_names = [element.text.strip() for element in hotel_elements]

    return hotel_names

# Example usage
url = 'https://www.booking.com/searchresults.el.html?region=4071&aid=318615;label=New_Greek_EL_5226381745-4kpTWDLoY_o31TQgJu8JDgS637880914771:pl:ta:p1:p2:ac:ap:neg:fi55414606308:tidsa-302866489863:lp9062909:li:dec:dm:ag5226381745:cmp108542065;ws=&gclid=CjwKCAjwyJqzBhBaEiwAWDRJVF9cmMrVkTb1xFGWeolwTwzGsZ42zVT_QHOL71PAadTQ4d3Rvd7DSBoCbgcQAvD_BwE'  # Replace with the URL of the website you want to scrape
hotel_names = scrape_hotel_names(url)
print(hotel_names)