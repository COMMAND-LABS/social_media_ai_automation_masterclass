# TLDR

Notes related to this mini helper project

## Initial setup

```sh
python -m venv .venv
source .venv/bin/activate
pip install uv
uv init
rm hello.py
touch main.py
echo "print('Hello World')" > main.py
uv run main.py
touch .gitignore
echo ".env\n" >> .gitignore
```

##

- `uv add pinecone`
- `touch .env`
- `echo "PINECONE_API_KEY=" > .env`