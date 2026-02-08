# Fami Chatbot

A simple rule-based chatbot built using Python, NLTK, and scikit-learn. The chatbot uses TF-IDF vectorization and cosine similarity to find relevant responses from a knowledge base.

## Features

- Natural language processing using NLTK
- TF-IDF vectorization for text analysis
- Cosine similarity for response matching
- Lemmatization for better word matching
- Greeting detection
- Stop word filtering

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/chatbot.git
cd chatbot
```

2. Install required packages:
```bash
pip install numpy nltk scikit-learn
```

3. Download NLTK data (automatic on first run):
```python
import nltk
nltk.download('punkt_tab')
nltk.download('wordnet')
```

## Usage

1. Make sure you have a `chatbot.txt` file with your knowledge base content
2. Run the chatbot:
```bash
python chatbot.py
```

3. Start chatting! Type 'bye' to exit.

### Example Conversation:
```
BOT: My name is Fami. Let's have a conversation! Also, if you want to exit any time, just type Bye!
You: Hello
BOT: hi there
You: What is data science?
BOT: Data science is the study of data to extract meaningful insights.
You: bye
BOT: Goodbye!
```

## How It Works

1. **Text Preprocessing**: User input is converted to lowercase, punctuation is removed, and words are lemmatized
2. **Vectorization**: Text is converted to TF-IDF vectors
3. **Similarity Matching**: Cosine similarity finds the most relevant response from the knowledge base
4. **Response Generation**: The most similar sentence is returned as the bot's response

## Project Structure
```
chatbot/
│
├── chatbot.py          # Main chatbot script
├── chatbot.txt         # Knowledge base text file
├── README.md           # This file
└── requirements.txt    # Python dependencies (optional)
```

## Technologies Used

- **Python 3.11**
- **NLTK** - Natural Language Toolkit for tokenization and lemmatization
- **scikit-learn** - TF-IDF vectorization and cosine similarity
- **NumPy** - Numerical computations

## Customization

### Adding Your Own Knowledge Base

Edit `chatbot.txt` with your own content. Each sentence will be a potential response. For example:
```
Data science is the study of data to extract meaningful insights.
Machine learning is a subset of artificial intelligence.
Python is a popular programming language for data science.
```

### Modifying Greetings

Edit the `GREET_INPUTS` and `GREET_RESPONSES` tuples in `chatbot.py`:
```python
GREET_INPUTS = ("hello", "hi", "hey", "yo", "wassup")
GREET_RESPONSES = ["Hello!", "Hi there!", "Hey!", "Greetings!"]
```

## Limitations

- Responses are limited to sentences in the knowledge base
- Cannot generate new responses or learn from conversations
- May struggle with very specific or complex queries
- Requires well-written knowledge base for good performance

## Future Improvements

- [ ] Add conversation context/memory
- [ ] Implement sentiment analysis
- [ ] Add GUI interface
- [ ] Support for multiple languages
- [ ] Integration with external APIs
- [ ] Deploy as a web application

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

Fatima Amir Fahim
- GitHub: [@fatimaamirfahim-bit](https://github.com/fatimaamirfahim-bit)
- Email: fahimfatimaamir@gmail.com

## Acknowledgments

- NLTK documentation
- scikit-learn documentation
- Inspiration from various chatbot tutorials

## Contact

If you have any questions or suggestions, feel free to reach out!

---

⭐ If you found this project helpful, please consider giving it a star!