import os

SEARCH_URL = (
    "https://www.googleapis.com/customsearch/v1?key={key}&cx={cx}&q={query}&start={start}&num=10&gl="
    + os.environ.get("COUNTRY")
)
RESULT_COUNT = 20
