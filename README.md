# Semantic Search App

A simple Semantic Search web app built using Streamlit and Sentence Transformers.

## Features

- Semantic text search
- AI embeddings using Sentence Transformers
- Cosine similarity matching
- Simple and beginner friendly
- Streamlit web interface

---

## Tech Stack

- Python
- Streamlit
- Sentence Transformers
- NumPy

---

## Project Structure

```txt
semantic-search-app/
│
├── app.py
├── requirements.txt
└── data.txt
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/semantic-search-app.git
cd semantic-search-app
```

Create virtual environment (optional):

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the App

```bash
streamlit run app.py
```

---

## Example Search

Search query:

```txt
soccer championship
```

Possible result:

```txt
Messi won the world cup with Argentina.
```

The app understands meaning instead of exact keyword matching.

---

## Deployment

This app can be deployed easily using Streamlit Community Cloud.

### Deployment Steps

1. Push project to GitHub
2. Open Streamlit Cloud
3. Select repository
4. Deploy `app.py`

Useful links:

- https://streamlit.io
- https://github.com
- https://www.sbert.net

---

## Sample Data

Example entries inside `data.txt`:

```txt
Messi won the world cup with Argentina.
Python is used for AI and machine learning.
Chennai is famous for Marina Beach.
```

---
Screenshot(with score for random search)
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/085218e1-9669-493f-a1e5-2fc84bede605" />

---

## Future Improvements

- PDF semantic search
- Vector database integration
- RAG chatbot
- Voice search
- Image search
- Database storage
- Multi-language support

---

## License

MIT License
