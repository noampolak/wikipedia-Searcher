from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from app.wiki_utils import wiki_search
import logging
import logging.config

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <head>
            <title>WikipediaSearcher</title>
        </head>
        <body>
            <h1>WikipediaSearcher</h1>
        </body>
    </html>
    """


@app.get("/api/search_term/{wiki_term}")
async def search_item(wiki_term: str, k: int = 1):

    return wiki_search(wiki_term, k)
