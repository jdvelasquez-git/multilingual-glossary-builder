# ⚡ AI-Assisted Glossary Builder

If you work in Localization or Globalization your in organization, you likely rely on glossaries to ensure brand/product message consistency, especially for technical specifications. This handy Python script will help you leverage content from existing translation memories to create an almost-perfect bilingual glossary leveraging Perplexity's Sonar model. You can read more about why I made this script by visiting [Localization Times (blog)]([url](https://localizationtimes.com/blogs/building-glossaries-out-of-translation-memories/)).

## 📄 Requirements
1. A list of terms in Excel format.
2. A translation memory in Excel format. Check your TMS documentation for details: Phrase, MemoQ, Trados, or XTM.
3. Perplexity [API key]([url](https://www.perplexity.ai/account/api/keys)). You will need to use a valid payment method. Check their [API pricing (Sonar)]([url](https://docs.perplexity.ai/guides/pricing)) for more details.

## 💾 Libraries Used
1. OpenAI
2. Pandas

## 📄 General Instructions
1. Edit the script and add your API key (line 40).
2. Run the script.
3. Drag and drop your Excel files (minus quotation marks) following the interactive wizard.
4. Specify the column header names for each Excel file.
5. Enjoy your new glossary.

## 💭 Future Improvements
1. Ability to use TMX or Excel files interchangeably ([via lxml]([url](https://pypi.org/project/lxml/)) and some conditionals).
2. Reverse matching of extracted terms for validation purposes.
3. Code optimizations for reduced friction during the wizard.
