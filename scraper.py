import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import urllib.parse

SEARCH_TERM = "artificial intelligence"
MAX_PAGES = 5 
BASE_URL = "https://www.congress.gov/search"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}