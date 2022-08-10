import wikipedia
import logging

# setup loggers
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
fh = logging.FileHandler(filename="./server.log")
logger.addHandler(ch)  # Exporting logs to the screen
logger.addHandler(fh)  # Exporting logs to a file


def wiki_find_leaves(term: str, k: int):
    terms_to_return = wikipedia.search(term, results=k + 1)
    terms_to_return = terms_to_return[1:]
    terms_to_return_pages = []
    for term_to_return in terms_to_return:
        try:
            wiki_page = wikipedia.page(term_to_return, auto_suggest=False)
            logger.info(f"adding {wiki_page.title}")
            terms_to_return_pages.append(wiki_page)
            logger.info(f"len terms_to_return_pages is {len(terms_to_return_pages)}")
            if len(terms_to_return_pages) == k:
                break
        except wikipedia.exceptions.DisambiguationError as e:
            logger.info(f"going into Disambiguation page on term {term_to_return}")
            terms_to_return_pages.extend(
                wiki_find_leaves(term_to_return, k - len(terms_to_return_pages))
            )
            if len(terms_to_return_pages) == k:
                break
    return terms_to_return_pages


def wiki_search(term: str, k: int):
    terms_to_return_pages = []
    try:
        terms_to_return_pages.append(wikipedia.page(term, auto_suggest=False))
    except wikipedia.exceptions.PageError as e:
        return []
    except wikipedia.exceptions.DisambiguationError as e:
        terms_to_return_pages = wiki_find_leaves(term, k)

    return [
        {"title": term_page.title, "summary": term_page.summary}
        for term_page in terms_to_return_pages
    ]
