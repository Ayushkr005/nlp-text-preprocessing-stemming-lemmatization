# Text Preprocessing Application: Comparing Stemming vs. Lemmatization in Terms of Accuracy and Efficiency

## 📚 Project Title
**Text Preprocessing Application: Comparing Stemming vs. Lemmatization in Terms of Accuracy and Efficiency**

## 🎯 Objective
This project demonstrates and compares two fundamental Natural Language Processing (NLP) techniques: **Stemming** and **Lemmatization**. The application provides a comprehensive analysis of both methods in terms of processing speed, accuracy, and linguistic quality of output, helping users understand when to use each technique in real-world NLP applications.

## ✨ Features
- **Interactive Web Interface**: Clean, professional Streamlit-based UI for academic demonstration
- **Multiple Input Methods**: Text input, sample texts, and file upload (.txt) support
- **Complete Text Preprocessing Pipeline**:
  - Lowercase conversion
  - Punctuation removal
  - Special character removal
  - Tokenization
  - Stopword removal
- **Dual Processing Options**:
  - Porter Stemmer for stemming
  - WordNet Lemmatizer for lemmatization
  - Side-by-side comparison
- **Performance Analysis**:
  - Processing time measurement (in milliseconds)
  - Transformation count analysis
  - Readability scoring
  - Comparative metrics
- **Educational Output**: Clear explanations and recommendations for different use cases

## 🛠️ Technologies Used
- **Python 3.8+**: Core programming language
- **NLTK (Natural Language Toolkit)**: Text processing and linguistic data
- **Streamlit**: Web application framework
- **Pandas**: Data manipulation and display
- **Regular Expressions**: Pattern matching for text cleaning

## 📁 Project Structure
```
NLP/
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── sample_texts/         # Sample text files for testing
│   ├── academic.txt
│   ├── news.txt
│   └── literary.txt
└── screenshots/          # Application screenshots (optional)
```

## 🚀 Steps to Run

### 🌐 **Live Demo**
**🔗 Deployed Application**: https://text-preprocessing-application.streamlit.app/

### 📋 **Local Development**

### Prerequisites
- Python 3.8 or higher installed on your system
- pip (Python package installer)

### Installation and Setup

1. **Clone or Download the Project**
   ```bash
   # If using git
   git clone <repository-url>
   cd NLP
   
   # Or download and extract the ZIP file
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
   This will install:
   - streamlit==1.28.0
   - nltk==3.8.1
   - pandas==2.0.3
   - regex==2023.8.8

3. **Run the Application**
   ```bash
   streamlit run app.py
   ```

4. **Access the Application**
   - The application will automatically open in your default web browser
   - If not, navigate to `http://localhost:8501` in your browser

### First Run Setup
On the first run, NLTK will automatically download required data packages:
- `punkt` (for tokenization)
- `stopwords` (for stopword removal)
- `wordnet` (for lemmatization)

This is a one-time process and may take a few minutes depending on your internet connection.

## 📊 Sample Output Explanation

### Input Text Example
```
"The beautiful flowers were dancing gracefully in the gentle breeze."
```

### Preprocessing Steps
1. **Lowercase**: "the beautiful flowers were dancing gracefully in the gentle breeze."
2. **Remove Punctuation**: "the beautiful flowers were dancing gracefully in the gentle breeze"
3. **Remove Special Characters**: "the beautiful flowers were dancing gracefully in the gentle breeze"
4. **Tokenize**: ['the', 'beautiful', 'flowers', 'were', 'dancing', 'gracefully', 'in', 'the', 'gentle', 'breeze']
5. **Remove Stopwords**: ['beautiful', 'flowers', 'dancing', 'gracefully', 'gentle', 'breeze']

### Processing Results

#### Stemming Output
```
beauti, flower, danc, graceful, gentl, breez
```

#### Lemmatization Output
```
beautiful, flower, dancing, gracefully, gentle, breeze
```

### Performance Metrics
- **Stemming Time**: ~2.5 milliseconds
- **Lemmatization Time**: ~8.7 milliseconds
- **Conclusion**: Stemming is ~3.5x faster but less linguistically accurate

## 🎓 Academic Value

### Learning Objectives
1. **Understanding Text Preprocessing**: Complete pipeline from raw text to processed tokens
2. **Algorithm Comparison**: Direct comparison of stemming vs. lemmatization
3. **Performance Analysis**: Measuring computational efficiency
4. **Linguistic Accuracy**: Evaluating output quality and readability
5. **Practical Application**: Real-world use case scenarios

### Key Concepts Demonstrated
- **Tokenization**: Breaking text into individual words
- **Stopword Removal**: Eliminating common words with little semantic value
- **Stemming**: Rule-based word normalization (Porter algorithm)
- **Lemmatization**: Dictionary-based word normalization (WordNet)
- **Performance Measurement**: Time complexity analysis
- **Quality Assessment**: Readability and linguistic correctness

## 📈 Analysis Results

### Performance Comparison
| Aspect | Stemming | Lemmatization | Winner |
|--------|----------|---------------|---------|
| **Speed** | ~2-5 ms | ~8-15 ms | Stemming |
| **Accuracy** | Medium | High | Lemmatization |
| **Linguistic Quality** | Low | High | Lemmatization |
| **Memory Usage** | Low | Medium | Stemming |

### Use Case Recommendations

#### 🌿 Use Stemming When:
- **Speed is critical**: Search engines, real-time processing
- **Large-scale text processing**: Document classification, spam detection
- **Approximate matching is acceptable**: Information retrieval systems
- **Resource constraints**: Limited computational resources

#### 🔤 Use Lemmatization When:
- **Linguistic accuracy matters**: Chatbots, language translation
- **Human-readable output**: Text summarization, content analysis
- **Semantic understanding**: Sentiment analysis, topic modeling
- **Quality over speed**: Academic applications, research

## 🔧 Technical Implementation

### Core Classes and Functions

#### TextPreprocessor Class
- `preprocess_text()`: Basic text cleaning and normalization
- `tokenize_text()`: Word tokenization using NLTK
- `remove_stopwords()`: Stopword filtering
- `apply_stemming()`: Porter stemming with timing
- `apply_lemmatization()`: WordNet lemmatization with timing
- `analyze_differences()`: Comparative analysis

### Performance Measurement
```python
# Timing implementation
start_time = time.time()
processed_tokens = algorithm(tokens)
processing_time = (time.time() - start_time) * 1000  # Convert to milliseconds
```

### Readability Scoring
Simple heuristic based on:
- Average word length
- Transformation frequency
- Linguistic correctness

## 📸 Screenshots

### 📊 Comparative Analysis
![Comparative Analysis](screenshots/comparative_analysis.png)

### ⚡ Performance Metrics
![Performance Metrics](screenshots/performance_metrics.png)

### 📋 Side-by-Side Comparison
![Side-by-Side Comparison](screenshots/side_by_side_comparison.png)

### 📈 Transformation Analysis
![Transformation Analysis](screenshots/transformation_analysis.png)

## 🎯 Conclusion

### Key Findings
1. **Stemming** is significantly faster but produces less accurate, sometimes non-dictionary words
2. **Lemmatization** is slower but maintains linguistic correctness and readability
3. **Choice depends on application requirements**: speed vs. accuracy trade-off
4. **Modern NLP systems** often prefer lemmatization despite performance costs

### Academic Significance
This project demonstrates fundamental NLP concepts that are essential for:
- Understanding text preprocessing pipelines
- Making informed algorithm choices
- Evaluating computational trade-offs
- Building practical NLP applications

## 🤝 Contributing

This is an academic assignment project. For educational purposes, feel free to:
- Study the code structure
- Modify the comparison metrics
- Add new preprocessing steps
- Extend with additional NLP techniques

## 📞 Support

For questions about this project:
- Review the inline code comments
- Check the application tooltips
- Refer to NLTK documentation
- Consult the sample outputs in the application

## 📄 License

This project is created for educational purposes. Feel free to use and modify for learning and academic assignments.

---

**Project Created for NLP Course Assignment**