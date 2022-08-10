# wikipedia-Searcher

### Setup
`python -m venv ./.venv` \
`source .venv/bin/activate` \ 
`pip install -r requirements.txt`

### Run
`uvicorn app.main:app --host 0.0.0.0 --port 8000`

### Run On docker
`docker build . --load -t wikipedia_searcher:latest` \
`docker run -p 8000:80 wikipedia_searcher:latest` &

### Usage
Open localhost:8000/docs to open the swagger and use the ** Search Item ** endpoint. \
wiki_term = The term you want to search. \
k = Number of possible results.

### Test
Run this command from the root directory: \
`PYTHONPATH=`pwd` pytest`
