import requests
from bs4 import BeautifulSoup
import json

def scrape_json_ld(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    script_tag = soup.find('script', type='application/ld+json')
    
    json_content = json.loads(script_tag.string)
    
    event_name = json_content.get('name', '')
    start_date = json_content.get('startDate', '')
    end_date = json_content.get('endDate', '')
    location = json_content.get('location', {}).get('name', '')
    address = json_content.get('location', {}).get('address', {}).get('streetAddress', '')
    city = json_content.get('location', {}).get('address', {}).get('addressLocality', '')
    region = json_content.get('location', {}).get('address', {}).get('addressRegion', '')
    country = json_content.get('location', {}).get('address', {}).get('addressCountry', '')
    postal_code = json_content.get('location', {}).get('address', {}).get('postalCode', '')
    description = json_content.get('description', '')
    event_url = json_content.get('url', '')
    organizer = json_content.get('organizer', {}).get('name', '')
    
    offers = json_content.get('offers', [])
    pricing = [{'name': offer.get('name', ''), 'price': offer.get('price', ''), 'currency': offer.get('priceCurrency', '')} for offer in offers if offer.get('name') and offer.get('price') and offer.get('priceCurrency')]

    return {
        'Event Name': event_name,
        'Start Date': start_date,
        'End Date': end_date,
        'Location': location,
        'Address': address,
        'City': city,
        'Region': region,
        'Country': country,
        'Postal Code': postal_code,
        'Description': description,
        'Event URL': event_url,
        'Organizer': organizer,
        'Offers' : offers,
        'Pricing': pricing
    }

def main():
    event_urls = [
        'https://www.eventbrite.com/e/international-d2c-conclave24-tickets-884043807827',
        'https://www.eventbrite.at/e/red-bull-bc-one-cypher-india-tickets-910465897007',
        'https://www.eventbrite.com/e/founders-conclave-startup-mixer-investor-and-d2c-tickets-924950771657',
        'https://www.eventbrite.co.uk/e/eco-consciousness-and-wellness-expo-tickets-878457408757',
        'https://www.eventbrite.com/e/india-health-wellness-expo-2024-tickets-888133440027',
        
    ]
    
    events_data = []

    for url in event_urls:
        event_data = scrape_json_ld(url)
        events_data.append(event_data)

    with open('b2b_events.json', 'w') as json_file:
        json.dump(events_data, json_file, indent=4)

if __name__ == '__main__':
    main()
