import wikipedia
import logging

# setup loggers
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
logger.addHandler(ch)  # Exporting logs to the screen


def wiki_find_leaves(term: str, k: int):
    terms_to_return = wikipedia.search(term, results=k + 1)
    # We should drop the first result because the function returns the disambiguation term as the first element and the list
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

    """
    Search the wikipedia api for pages that meet the request

    Keyword arguments:

    * term - the title of the page to load
    * k - in case the term returns disambiguation page it will limit the number of results
    """
    terms_to_return_pages = []
    try:
        terms_to_return_pages.append(wikipedia.page(term, auto_suggest=False))
        logger.debug(f"API found one result that meet with the search term - {term}")
    except wikipedia.exceptions.PageError as e:
        logger.debug(
            f"API didn't find any result that meet with the search term - {term}"
        )
        return []
    except wikipedia.exceptions.DisambiguationError as e:
        logger.debug(
            f"API got DisambiguationError exception, so we're sending the search term - {term} to the recursive function"
        )
        terms_to_return_pages = wiki_find_leaves(term, k)

    return [
        {"title": term_page.title, "summary": term_page.summary}
        for term_page in terms_to_return_pages
    ]
