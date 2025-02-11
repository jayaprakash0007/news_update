Country GDP and News Updates Script
This script allows users to retrieve the latest GDP data and top news headlines for any country. It utilizes the World Bank API for GDP data and the News API for fetching news headlines.

Table of Contents
Prerequisites
Installation
Usage
Functions
get_gdp_data
get_news_headlines
get_country_updates
Examples
Contributing
License
Prerequisites
Before using this script, ensure you have the following:

Python 3 installed on your system.
Internet access for the script to make API requests.
An API key for the News API. You can get it by signing up at News API.
Installation
Install the required Python packages using pip.

```bash
pip install requests
```
Usage
Replace ##NEWS_API_KEY with your actual News API key.

```python
api_key = 'YOUR_NEWS_API_KEY'
```
Enter the country name and country code in the script.

```python 
country_name = "India"
country_code = "IN"```
Functions
get_gdp_data(country_code)
This function retrieves the GDP data for a given country using the World Bank API.

Parameters: country_code (str): The ISO 3166-1 alpha-2 code of the country (e.g., "US" for the United States).
Returns: A formatted string containing the GDP data and year or a message indicating that GDP data is not available.
get_news_headlines(country_code)
This function retrieves the top news headlines for a given country using the News API.

Parameters: country_code (str): The ISO 3166-1 alpha-2 code of the country (e.g., "US" for the United States).
Returns: A list of the top 10 news headlines or a message indicating that no news is available.
get_country_updates(country_name, country_code)
This function prints the GDP data and top news headlines for a given country.

Parameters:
country_name (str): The name of the country (e.g., "United States").
country_code (str): The ISO 3166-1 alpha-2 code of the country (e.g., "US").
