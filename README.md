# Financial Statement Casting App

This project demonstrates a simple Streamlit interface for uploading
financial statement documents (PDF, Word, or Excel) and sending their
contents to OpenAI for analysis.

## Setup

1. Install the required packages (the app uses the
   [OpenAI Python library](https://github.com/openai/openai-python)
   version 1 or later):

```bash
pip install -r requirements.txt
```

2. Export your OpenAI API key as an environment variable:

```bash
export OPENAI_API_KEY=your-api-key
```

You can also create a `.env` file containing the key so it is loaded
automatically when the app starts:

```
OPENAI_API_KEY=your-api-key
```

## Usage

Run the Streamlit app with:

```bash
streamlit run financial_cast_app.py
```

Upload a financial statement and press **Analyze** to receive a concise
summary from OpenAI. The app uses the latest chat completions API.


