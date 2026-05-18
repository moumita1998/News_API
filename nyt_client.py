import requests
from app.config import NYT_API_KEY

BASE_URL="https://api.nytimes.com/svc/news/v3/content"

def fetch_nyt_news(source: str ="all", limit: int=20):
    """
    Fetch latest NYT articels from TimesWire API.
    
    """

    url= f"{BASE_URL}/{source}/{section}.json"

    params={
        "api-key": NYT_API_KEY,
        "limit": limit
       }

    response= requests.get(url,params=params, timeout=30)

    if response.status_code!=200:
        raise Exception(
            f"NYT API failed with status"{response.status_code}:{response.text}"

        )

    data = response.json()

    articles=[]

    for item in data.get("results",[]):
        article={
            "title": item.get("title"),
            "abstract": item.get("abstract"),
            "section": item.get("section"),
            "subsection": item.get("subsection"),
            "url": item.get("url"),
            "byline": item.get("byline"),
            "item_type": item.get("item_type"),
            "source": item.get("source"),
            "published_date": item.get("published_date"),
            "updated_date": item.get("updated_date"),
            "material_type": item.get("material_type_facet"),
            "keywords": item.get("des_facet", []),
            "people": item.get("per_facet", []),
            "organizations": item.get("org_facet", []),
            "locations": item.get("geo_facet", [])

        }

        articles.append(article)

        return {
            "status": data.get("status"),
            "total_results":data.get("num_results"),
            "articles":articles
        }