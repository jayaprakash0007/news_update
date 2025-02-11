import requests
def get_gdp_data(country_code):
    url = f"http://api.worldbank.org/v2/country/{country_code}/indicator/NY.GDP.MKTP.CD?format=json"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200 and len(data) > 1:
        gdp = data[1][0]['value']
        year = data[1][0]['date']
        return f"GDP for {country_code} in {year}: ${gdp:,.2f}"
    else:
        return "GDP data not available"
def get_news_headlines(country_code):
    api_key = '##NEWS_API_KEY'
    url = f"https://newsapi.org/v2/top-headlines?country={country_code}&apiKey={api_key}"
    response = requests.get(url)
    news_data = response.json()
    if response.status_code == 200:
        articles = news_data['articles']
        headlines = [article['title'] for article in articles[:10]]  
        return headlines
    else:
        return "No news available"
def get_country_updates(country_name, country_code):
    gdp_data = get_gdp_data(country_code)
    news_headlines = get_news_headlines(country_code)

    print(f"Updates for {country_name}:\n")
    print(gdp_data)
    print("\nTop News Headlines:")
    for idx, headline in enumerate(news_headlines, 1):
        print(f"{idx}. {headline}")

country_name = "#ENTER COUNTRY"
country_code = "#ENTER COUNTRY CODE"
get_country_updates(country_name, country_code)
