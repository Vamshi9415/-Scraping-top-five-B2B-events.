## README

### Overview

This Python script scrapes event data from specified Eventbrite URLs and extracts structured information embedded in JSON-LD format. The extracted data includes event details, location, dates, description, and pricing information.

### Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library

### Installation

1. Clone the repository or download the script files.
2. Install the required Python libraries using pip:
   ```bash
   pip install requests beautifulsoup4
   ```

### Usage

1. Update the `event_urls` list in the `main` function with the Eventbrite URLs you want to scrape.
2. Run the script:
   ```bash
   python script_name.py
   ```
   Replace `script_name.py` with the name of your script file.

3. The script will output a JSON file named `b2b_events.json` containing the collected event data.

### Data Collected

The script collects the following data for each event:

- Event Name
- Start Date
- End Date
- Location (Venue Name)
- Address
  - Street Address
  - City
  - Region
  - Country
  - Postal Code
- Description
- Event URL
- Organizer
- Offers (all available ticket types and their prices)
- Pricing (filtered offers with non-empty `name`, `price`, and `currency`)

### Example Output

Here is an example of what the JSON output will look like:

```json
[
    {
        "Event Name": "International D2C Conclave'24",
        "Start Date": "2024-07-13T08:30:00+05:30",
        "End Date": "2024-07-13T18:00:00+05:30",
        "Location": "Radisson Hotel Gurugram Udyog Vihar",
        "Address": "Nh-8 Udyog Vihar Phase 3 Road #Adjacent to Plot No. 406, Gurugram, HR 122016",
        "City": "Gurugram",
        "Region": "HR",
        "Country": "IN",
        "Postal Code": "122016",
        "Description": "The International D2C Conclave 2024 in Mumbai is Co-Organized with Global Startup Summit \u201924 it is an high ticket B2B event with 400+ pax",
        "Event URL": "https://www.eventbrite.com/e/international-d2c-conclave24-tickets-884043807827",
        "Organizer": "MOJO STARTUP PVT LTD",
        "Offers": [
            {
                "availabilityEnds": "2024-07-13T03:00:00Z",
                "priceCurrency": "USD",
                "url": "https://www.eventbrite.com/e/international-d2c-conclave24-tickets-884043807827",
                "lowPrice": 27.72,
                "highPrice": 58.83,
                "@type": "AggregateOffer",
                "availabilityStarts": "2024-04-15T18:30:00Z",
                "validFrom": "2024-04-15T18:30:00Z",
                "availability": "InStock"
            },
            {
                "name": "Sliver Delegates ( Without Lunch )",
                "priceCurrency": "USD",
                "url": "https://www.eventbrite.com/e/international-d2c-conclave24-tickets-884043807827",
                "price": 27.72,
                "@type": "Offer",
                "availability": "InStock"
            },
            {
                "name": "Gold Delegate ( With Lunch )",
                "priceCurrency": "USD",
                "url": "https://www.eventbrite.com/e/international-d2c-conclave24-tickets-884043807827",
                "price": 58.83,
                "@type": "Offer",
                "availability": "InStock"
            }
        ],
        "Pricing": [
            {
                "name": "Sliver Delegates ( Without Lunch )",
                "price": 27.72,
                "currency": "USD"
            },
            {
                "name": "Gold Delegate ( With Lunch )",
                "price": 58.83,
                "currency": "USD"
            }
        ]
    },
    ...
]
```

### Notes

- Ensure that the URLs provided in the `event_urls` list are correct and publicly accessible.
- The script assumes that the JSON-LD data is present in the `script` tag with `type='application/ld+json'` within the HTML content of the event page.
- The `Pricing` list is filtered to exclude any offers with empty `name`, `price`, or `currency` fields.