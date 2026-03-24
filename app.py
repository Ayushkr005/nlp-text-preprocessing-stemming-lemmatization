"""
Text Preprocessing Application: Comparing Stemming vs. Lemmatization in Terms of Accuracy and Efficiency

This is a comprehensive NLP assignment project that demonstrates and compares
stemming and lemmatization techniques for text preprocessing.

Done By- Ayush Kumar
Reg no.-RA2311003012333
Section-R2
Branch and Department- CSE CORE/C-Tech
"""

import streamlit as st
import nltk
import re
import time
import string
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import pandas as pd

# Download required NLTK data (only needed once)
def download_nltk_data():
    """Download all required NLTK data packages."""
    import nltk
    
    # List of required packages
    required_packages = [
        'punkt_tab',  # Updated for newer NLTK versions
        'stopwords',
        'wordnet',
        'omw-1.4'  # Open Multilingual Wordnet for lemmatization
    ]
    
    for package in required_packages:
        try:
            nltk.data.find(f'tokenizers/{package}' if 'punkt' in package else f'corpora/{package}')
        except LookupError:
            print(f"Downloading {package}...")
            nltk.download(package, quiet=True)

# Download data on startup
download_nltk_data()

class TextPreprocessor:
    """
    A comprehensive text preprocessing class that handles all NLP operations
    including stemming and lemmatization comparison.
    """
    
    def __init__(self):
        """Initialize the text preprocessor with necessary NLTK components."""
        self.stemmer = PorterStemmer()
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
        
    def preprocess_text(self, text):
        """
        Perform basic text preprocessing steps.
        
        Args:
            text (str): Raw input text
            
        Returns:
            str: Preprocessed text
        """
        # Convert to lowercase
        text = text.lower()
        
        # Remove punctuation
        text = text.translate(str.maketrans('', '', string.punctuation))
        
        # Remove special characters and numbers (keep only letters and spaces)
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text).strip()
        
        return text
    
    def tokenize_text(self, text):
        """
        Tokenize preprocessed text into individual words.
        
        Args:
            text (str): Preprocessed text
            
        Returns:
            list: List of tokens
        """
        tokens = word_tokenize(text)
        return tokens
    
    def remove_stopwords(self, tokens):
        """
        Remove stopwords from token list.
        
        Args:
            tokens (list): List of tokens
            
        Returns:
            list: List of tokens without stopwords
        """
        filtered_tokens = [token for token in tokens if token not in self.stop_words]
        return filtered_tokens
    
    def apply_stemming(self, tokens):
        """
        Apply Porter stemming algorithm to tokens.
        
        Args:
            tokens (list): List of tokens
            
        Returns:
            tuple: (stemmed_tokens, processing_time)
        """
        start_time = time.time()
        stemmed_tokens = [self.stemmer.stem(token) for token in tokens]
        processing_time = (time.time() - start_time) * 1000  # Convert to milliseconds
        return stemmed_tokens, processing_time
    
    def apply_lemmatization(self, tokens):
        """
        Apply WordNet lemmatization to tokens.
        
        Args:
            tokens (list): List of tokens
            
        Returns:
            tuple: (lemmatized_tokens, processing_time)
        """
        start_time = time.time()
        lemmatized_tokens = [self.lemmatizer.lemmatize(token) for token in tokens]
        processing_time = (time.time() - start_time) * 1000  # Convert to milliseconds
        return lemmatized_tokens, processing_time
    
    def analyze_differences(self, original_tokens, stemmed_tokens, lemmatized_tokens):
        """
        Analyze the differences between stemming and lemmatization results.
        
        Args:
            original_tokens (list): Original tokens
            stemmed_tokens (list): Stemmed tokens
            lemmatized_tokens (list): Lemmatized tokens
            
        Returns:
            dict: Analysis results
        """
        # Count transformations
        stem_transformations = sum(1 for orig, stem in zip(original_tokens, stemmed_tokens) if orig != stem)
        lemma_transformations = sum(1 for orig, lemma in zip(original_tokens, lemmatized_tokens) if orig != lemma)
        
        # Calculate readability scores (simplified)
        stem_readability = self._calculate_readability(stemmed_tokens)
        lemma_readability = self._calculate_readability(lemmatized_tokens)
        
        return {
            'stem_transformations': stem_transformations,
            'lemma_transformations': lemma_transformations,
            'stem_readability': stem_readability,
            'lemma_readability': lemma_readability
        }
    
    def _calculate_readability(self, tokens):
        """
        Calculate a simple readability score based on word length and common words.
        
        Args:
            tokens (list): List of tokens
            
        Returns:
            float: Readability score (0-1, higher is better)
        """
        if not tokens:
            return 0.0
        
        # Simple heuristic: longer words and fewer transformations indicate better readability
        avg_length = sum(len(token) for token in tokens) / len(tokens)
        normalized_length = min(avg_length / 6.0, 1.0)  # Normalize to 0-1
        
        return normalized_length

def create_comparison_table(original_tokens, stemmed_tokens, lemmatized_tokens):
    """
    Create a side-by-side comparison table for analysis.
    
    Args:
        original_tokens (list): Original tokens
        stemmed_tokens (list): Stemmed tokens
        lemmatized_tokens (list): Lemmatized tokens
        
    Returns:
        pd.DataFrame: Comparison table
    """
    max_length = max(len(original_tokens), len(stemmed_tokens), len(lemmatized_tokens))
    
    # Pad lists to equal length
    original_tokens.extend([''] * (max_length - len(original_tokens)))
    stemmed_tokens.extend([''] * (max_length - len(stemmed_tokens)))
    lemmatized_tokens.extend([''] * (max_length - len(lemmatized_tokens)))
    
    df = pd.DataFrame({
        'Original': original_tokens,
        'Stemmed': stemmed_tokens,
        'Lemmatized': lemmatized_tokens
    })
    
    return df

def main():
    """
    Main function to run the Streamlit web application.
    """
    # Initialize the preprocessor
    preprocessor = TextPreprocessor()
    
    # Configure Streamlit page
    st.set_page_config(
        page_title="Text Preprocessing: Stemming vs Lemmatization",
        page_icon="📚",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Main title and description
    st.title("📚 Text Preprocessing Application")
    st.markdown("### Comparing Stemming vs. Lemmatization in Terms of Accuracy and Efficiency")
    st.markdown("---")
    
    # Sidebar for input options
    st.sidebar.header("📝 Input Options")
    
    # Sample text selection
    st.sidebar.subheader("Sample Text Options")
    sample_texts = {
        "Academic Text": "Natural language processing enables computers to understand human language. Researchers are developing sophisticated algorithms that can analyze, interpret, and generate text. These advancements have revolutionized how we interact with technology.",
        "News Article": "The government announced new policies regarding environmental protection. Scientists have been studying climate change for decades and believe immediate action is necessary. The public response has been overwhelmingly positive.",
        "Literary Text": "The beautiful flowers were dancing gracefully in the gentle breeze. Children were running happily through the meadows, laughing and playing without any worries. Nature has always been a source of inspiration for poets and writers.",
        "Custom Input": ""
    }
    
    selected_sample = st.sidebar.selectbox("Choose sample text:", list(sample_texts.keys()))
    
    # Text input area
    if selected_sample == "Custom Input":
        input_text = st.text_area(
            "Enter your text here:",
            height=150,
            placeholder="Paste or type your text here for preprocessing analysis..."
        )
    else:
        input_text = st.text_area(
            "Sample Text:",
            value=sample_texts[selected_sample],
            height=150
        )
    
    # File upload option
    st.sidebar.subheader("File Upload")
    uploaded_file = st.sidebar.file_uploader("Upload a .txt file", type=['txt'])
    
    if uploaded_file is not None:
        input_text = uploaded_file.read().decode('utf-8')
        st.sidebar.success("File uploaded successfully!")
    
    # Processing buttons
    st.sidebar.subheader("Processing Options")
    col1, col2 = st.sidebar.columns(2)
    
    with col1:
        process_stemming = st.button("🌿 Apply Stemming", key="stem")
        process_lemmatization = st.button("🔤 Apply Lemmatization", key="lemma")
    
    with col2:
        process_both = st.button("⚖️ Compare Both", key="both")
        clear_results = st.button("🗑️ Clear", key="clear")
    
    # Clear results if requested
    if clear_results:
        st.rerun()
    
    # Main content area for results
    if input_text and (process_stemming or process_lemmatization or process_both):
        st.markdown("## 📊 Analysis Results")
        st.markdown("---")
        
        # Step 1: Show original text
        st.subheader("📄 Original Text")
        st.text_area("", value=input_text, height=100, disabled=True, key="original")
        
        # Step 2: Preprocessing
        with st.spinner("Preprocessing text..."):
            preprocessed_text = preprocessor.preprocess_text(input_text)
            tokens = preprocessor.tokenize_text(preprocessed_text)
            filtered_tokens = preprocessor.remove_stopwords(tokens)
        
        # Step 3: Show preprocessing results
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("🔧 Preprocessed Text")
            st.text_area("", value=preprocessed_text, height=100, disabled=True, key="preprocessed")
        
        with col2:
            st.subheader("🏷️ Tokens (Stopwords Removed)")
            st.text_area("", value=", ".join(filtered_tokens), height=100, disabled=True, key="tokens")
        
        # Step 4: Apply requested processing
        if process_stemming or process_both:
            with st.spinner("Applying stemming..."):
                stemmed_tokens, stem_time = preprocessor.apply_stemming(filtered_tokens)
            
            st.subheader("🌿 Stemmed Output")
            st.text_area("", value=", ".join(stemmed_tokens), height=100, disabled=True, key="stemmed")
            st.info(f"⏱️ Stemming processing time: {stem_time:.2f} milliseconds")
        
        if process_lemmatization or process_both:
            with st.spinner("Applying lemmatization..."):
                lemmatized_tokens, lemma_time = preprocessor.apply_lemmatization(filtered_tokens)
            
            st.subheader("🔤 Lemmatized Output")
            st.text_area("", value=", ".join(lemmatized_tokens), height=100, disabled=True, key="lemmatized")
            st.info(f"⏱️ Lemmatization processing time: {lemma_time:.2f} milliseconds")
        
        # Step 5: Comparison and Analysis
        if process_both:
            st.markdown("## 🔍 Comparative Analysis")
            st.markdown("---")
            
            # Performance comparison
            st.subheader("⚡ Performance Comparison")
            perf_col1, perf_col2, perf_col3 = st.columns(3)
            
            with perf_col1:
                st.metric("Stemming Time", f"{stem_time:.2f} ms")
            
            with perf_col2:
                st.metric("Lemmatization Time", f"{lemma_time:.2f} ms")
            
            with perf_col3:
                time_diff = abs(stem_time - lemma_time)
                faster = "Stemming" if stem_time < lemma_time else "Lemmatization"
                st.metric("Faster Method", f"{faster} by {time_diff:.2f} ms")
            
            # Detailed analysis
            analysis = preprocessor.analyze_differences(filtered_tokens, stemmed_tokens, lemmatized_tokens)
            
            st.subheader("📈 Transformation Analysis")
            analysis_col1, analysis_col2 = st.columns(2)
            
            with analysis_col1:
                st.metric("Words Transformed by Stemming", analysis['stem_transformations'])
                st.metric("Words Transformed by Lemmatization", analysis['lemma_transformations'])
            
            with analysis_col2:
                st.metric("Stemming Readability Score", f"{analysis['stem_readability']:.2f}")
                st.metric("Lemmatization Readability Score", f"{analysis['lemma_readability']:.2f}")
            
            # Side-by-side comparison table
            st.subheader("📋 Side-by-Side Comparison")
            comparison_df = create_comparison_table(filtered_tokens, stemmed_tokens, lemmatized_tokens)
            st.dataframe(comparison_df, use_container_width=True)
            
            # Conclusion section
            st.markdown("## 🎯 Conclusion")
            st.markdown("---")
            
            conclusion_col1, conclusion_col2 = st.columns(2)
            
            with conclusion_col1:
                st.markdown("### 🏆 Performance Results")
                if stem_time < lemma_time:
                    st.success("**Stemming is faster**")
                    st.write(f"Stemming completed {lemma_time/stem_time:.1f}x faster than lemmatization.")
                else:
                    st.success("**Lemmatization is faster**")
                    st.write(f"Lemmatization completed {stem_time/lemma_time:.1f}x faster than stemming.")
            
            with conclusion_col2:
                st.markdown("### 🎨 Accuracy & Readability")
                if analysis['lemma_readability'] > analysis['stem_readability']:
                    st.success("**Lemmatization produces more meaningful output**")
                    st.write("Lemmatized words are more linguistically correct and readable.")
                else:
                    st.info("**Stemming produces comparable readability**")
                    st.write("Both methods produce reasonably readable results.")
            
            # Recommendations
            st.markdown("### 💡 Recommendations")
            
            rec_col1, rec_col2 = st.columns(2)
            
            with rec_col1:
                st.markdown("**🌿 Use Stemming when:**")
                st.write("• Speed is the primary concern")
                st.write("• Applications like search engines")
                st.write("• Text classification tasks")
                st.write("• Large-scale text processing")
            
            with rec_col2:
                st.markdown("**🔤 Use Lemmatization when:**")
                st.write("• Linguistic accuracy is important")
                st.write("• Chatbots and conversational AI")
                st.write("• Text summarization")
                st.write("• Language translation systems")
    
    # Footer information
    st.markdown("---")
    st.markdown("### 📚 About This Project")
    st.markdown("""
    This application demonstrates the fundamental NLP concepts of stemming and lemmatization.
    It provides a comprehensive comparison to help understand when to use each technique
    based on accuracy, efficiency, and application requirements.
    """)
    
    st.markdown("**Technologies Used:** Python, NLTK, Streamlit, Pandas")
    st.markdown("**Algorithms:** Porter Stemmer, WordNet Lemmatizer")

if __name__ == "__main__":
    main()
