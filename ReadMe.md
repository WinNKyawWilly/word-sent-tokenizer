# NLTK Text Analyzer

## Overview

This Python script provides a comprehensive text analysis tool using the Natural Language Toolkit (NLTK). It offers advanced text processing capabilities, including text cleaning, sentence tokenization, word tokenization, and word frequency analysis.

## Features

- **Text Cleaning**: 
  - Converts text to lowercase
  - Removes numbers
  - Eliminates special characters
  - Normalizes whitespace

- **Tokenization**:
  - Sentence tokenization
  - Word tokenization with stopword removal

- **Word Frequency Analysis**:
  - Counts and ranks most frequent words
  - Customizable number of top words to display

- **File Output**:
  - Generates multiple text files with analysis results
  - Tracks processing time

## Prerequisites

- Python 3.7+
- NLTK Library
- Required NLTK Downloads: 
  - stopwords
  - punkt tokenizer

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/nltk-text-analyzer.git
cd nltk-text-analyzer
```

2. Install required dependencies:
```bash
pip install nltk
```

3. Download NLTK resources:
```python
import nltk
nltk.download('stopwords')
nltk.download('punkt')
```

## Usage

```python
from text_analyzer import TextAnalyzer

# Initialize the analyzer
analyzer = TextAnalyzer()

# Read your text file
with open('your_text_file.txt', 'r') as file:
    text = file.read()

# Perform analysis
sentences, words, word_freq = analyzer.get_analysis(text)

# Print results
print("Sentences:", sentences)
print("Words:", words)
print("Word Frequency:", word_freq)
```

## Output Files

The script generates the following files in the `nltk/` directory:
- `clean.txt`: Cleaned text
- `sentences.txt`: Tokenized sentences
- `words.txt`: Processed words
- `top10words.txt`: Word frequency analysis top 10
- `time.txt`: Processing time

## Performance

The script includes time tracking to measure processing duration for large text files.

## Dependencies

- NLTK
- Regular Expressions (re)
- Collections (Counter)

## Customization

- Modify `word_frequency()` method to change the number of top words
- Adjust `clean_text()` method to customize text preprocessing

## Limitations

- Currently supports English language processing
- Requires NLTK resources to be downloaded

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

