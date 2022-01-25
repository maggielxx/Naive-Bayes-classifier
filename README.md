# Naive-Bayes-classifier
an implementation of a Naive Bayes algorithm

The task is to implement an improved version of the Naive Bayes algorithm that is able to predict the domain - one of Archaea, Bacteria, Eukaryota or Virus - from the abstract of research papers about proteins taken from the MEDLINE database. 

The second attribute (class) in each record specifies the domain of the protein. 
The third attribute (abstract) in the record is a character string containing the abstract to be classified. The string is preprocessed: it contains only whitespace, alphanumerical lowercase characters, digits, the dash (-) and the prime ('). Each contiguous sequence of non-whitespace characters framed by whitespace is considered a word.
The file trg.csv is the training set on which you have to train your Naive Bayes classifier.
