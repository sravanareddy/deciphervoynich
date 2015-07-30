Data files and scripts that we used for the analysis of the Voynich manuscript in [Reddy and Knight (2011)](http://www.aclweb.org/anthology/W/W11/W11-1511.pdf).

# Data

All data files are in the data/ directory.

## Voynich text

## English
First 28551 words from the WSJ Penn Treebank, with each line an article. Devoweled version removes aeiou, but not y.

## Arabic
First 19327 words from the Quran in Buckwalter transcription, without vowels. Each line is a verse.

## Chinese

First 18791 words from the Sinica treebank that's included with NLTK (sinica.wds). Pinyin conversion (pinyin.wds) was done by looking up characters in the CJK library. Please let us know if you find errors in the conversion.
