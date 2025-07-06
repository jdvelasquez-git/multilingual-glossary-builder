#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Essentials
from openai import OpenAI
import pandas as pd
import requests
import time
import json
from tqdm import tqdm


# In[ ]:


# Load Excel data via user input
print(
    f"Welcome to AI-Assisted Multilingual Glossary Builder!\n"
    f"Please follow the instructions below to build your glossary.\n"
    f"-----------------\n"
    )
termListPath = input('1. Paste the full path of your term list in Excel format.\n')
termListColumn = input('2. What\'s the name of your term list column?\n')
translationsPath = input('3. Paste the full path of your translation memory in Excel format (1 column).\n')
sourceColumn = input('4. What\'s the language code or name of your source column?\n')
targetColumn = input('5. What\'s the language code or name of your target column?\n')
print(f"-----------------\nThanks! We are ready to get started 👷🏻‍♂️.\n-----------------\n")

TermsList = pd.read_excel(termListPath)
Translations = pd.read_excel(translationsPath)

# Save Excel data in lists
allTerms = set(TermsList[termListColumn].dropna().astype(str).unique())
memory = [(str(getattr(row, sourceColumn)), str(getattr(row, targetColumn))) for row in Translations.itertuples(index=False)]

# Load Perplexity
client = OpenAI(api_key="API-KEY-HERE", base_url="https://api.perplexity.ai")


# In[ ]:


# 1- Iterate through English terms
# 2- Translate a candidate in the target language
# 3- Find candidate in the translations

activeTerm = ""
matchList = []
newGlossary = []
seen_matches = set()

for term in tqdm(allTerms,desc='Processing English terms'):
    for source, target in memory:
        if term in seen_matches:
            continue
        if term in source:
            seen_matches.add(term)
            matchList.append({'term':term})
            prompt = (
                "Given this English term and its context, extract its translation from the provided translations:\n"
                f"Term: {term}\n"
                f"Context: {source}\n"
                f"Translations: {target}\n"
                "Output: Translated term in the detected language.\n"
                "Rules: No punctuation; no formatting; no intros; no explanations; no descriptions."
            )
            plex = client.chat.completions.create(
                model="sonar",
                messages=[{"role": "user", "content": prompt}],
                temperature=0
            )
            newGlossary.append({'en_us':term,'fr_fr':plex.choices[0].message.content.strip()})
            time.sleep(1.3)
            break

df = pd.DataFrame(newGlossary)
excel_filename = "glossary_LOTS.xlsx"
df.to_excel(excel_filename, index=False)
print(f"\n✅ Excel file created: {excel_filename}")

