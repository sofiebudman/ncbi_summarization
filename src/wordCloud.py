#word cloud from importance

def generate_tfidf_wordcloud(abstract):
    # Preprocess the abstract text
    abstract = preprocess_text(abstract)
    
    
    tfidf = TfidfVectorizer(stop_words=stopwords.words('english'), max_features=100)
    
    
    tfidf_matrix = tfidf.fit_transform([abstract])
    
   
    terms = tfidf.get_feature_names_out()
    scores = tfidf.idf_  
    
    
    word_importance = dict(zip(terms, scores))
    
    
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_importance)
    
    # plot
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()
