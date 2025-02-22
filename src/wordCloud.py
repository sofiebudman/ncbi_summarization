#word cloud from importance

def generate_tfidf_wordcloud(abstract):
    # Preprocess the abstract text
    abstract = preprocess_text(abstract)
    
    # Create TF-IDF vectorizer object
    tfidf = TfidfVectorizer(stop_words=stopwords.words('english'), max_features=100)
    
    # Fit the model on the text (convert text to TF-IDF matrix)
    tfidf_matrix = tfidf.fit_transform([abstract])
    
    # Get the terms and their corresponding TF-IDF scores
    terms = tfidf.get_feature_names_out()
    scores = tfidf.idf_  # Inverse document frequency
    
    # Create a dictionary of term:score
    word_importance = dict(zip(terms, scores))
    
    # Generate the word cloud using the TF-IDF scores as word importance
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_importance)
    
    # Display the word cloud
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()