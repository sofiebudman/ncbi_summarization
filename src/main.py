from fetch import fetchFromId,fetchFromUrl
from preProcess import extractAbstract, removePunctuation, removeStopWords

pmid = "27741350"  # Replace with a valid PMID
article_info = fetchFromId(pmid)

#creates a summary of the abstract
#generates word cloud
#provides Pubmed IDs and abstracts of 10 related articles


