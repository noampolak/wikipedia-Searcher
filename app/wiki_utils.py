import wikipedia


def wiki_search(term: str, k: int):
    try:
        term_data = wikipedia.page(term)
        return {"title": term_data.title, "summary": term_data.summary}
    except wikipedia.exceptions.PageError as e:
        return []
    except wikipedia.exceptions.DisambiguationError as e:
        terms_to_return = wikipedia.search(term)
        terms_to_return_pages = []

        for term_to_return in terms_to_return:
            try:
                terms_to_return_pages.append(
                    wikipedia.page(term_to_return, auto_suggest=False)
                )
                if len(terms_to_return_pages) == k:
                    break
            except wikipedia.exceptions.DisambiguationError as e:
                continue

        return [
            {"title": term_page.title, "summary": term_page.summary}
            for term_page in terms_to_return_pages
        ]
