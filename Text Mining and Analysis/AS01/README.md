# 1. Normalização

Realiza as seguintes operações no arquivo de entrada e gera o arquivo Shakespeare_Normalized.txt:

Redução para letras minúsculas (Lower case reduction)

Remoção de acentos e diacríticos (Accent and diacritic removal)

Padronização de acrônimos, moedas, datas e palavras hifenizadas

Remoção de pontuação (exceto em expressões monetárias e datas)

Remoção de caracteres especiais

# 2. Tokenização

Cada método de tokenização gera um arquivo de saída Shakespeare_Normalized_TokenizedXX.txt, onde XX representa o método utilizado:

White Space Tokenization (Shakespeare_Normalized_Tokenized01.txt)

NLTK: Word Tokenizer (Shakespeare_Normalized_Tokenized02.txt)

NLTK: Tree Bank Tokenizer (Shakespeare_Normalized_Tokenized03.txt)

NLTK: Word Punctuation Tokenizer (Shakespeare_Normalized_Tokenized04.txt)

NLTK: Tweet Tokenizer (Shakespeare_Normalized_Tokenized05.txt)

NLTK: MWE Tokenizer (Shakespeare_Normalized_Tokenized06.txt)

TextBlob Word Tokenizer (Shakespeare_Normalized_Tokenized07.txt)

spaCy Tokenizer (Shakespeare_Normalized_Tokenized08.txt)

Gensim Word Tokenizer (Shakespeare_Normalized_Tokenized09.txt)

Keras Tokenization (Shakespeare_Normalized_Tokenized10.txt)

# 3. Remoção de Stop-Words

Remove stop-words do texto tokenizado (subtarefa 2) e gera o arquivo de saída:

Shakespeare_Normalized_Tokenized_StopWord.txt

# 4. Lematização do Texto

Aplica o WordNet Lemmatizer ao texto gerado na etapa anterior e gera o arquivo de saída:

Shakespeare_Normalized_Tokenized_StopWord_Lemmatized.txt

# 5. Stemming

Aplica diferentes stemmers ao arquivo Shakespeare_Normalized_Tokenized_StopWord_Lemmatized.txt, gerando os seguintes arquivos:

Porter Stemmer (Shakespeare_Normalized_Tokenized_StopWord_Lemmatized_Stemming01.txt)

Snowball Stemmer (Shakespeare_Normalized_Tokenized_StopWord_Lemmatized_Stemming02.txt)

# 6. Análise do Vocabulário

Para cada lematizador e stemmer, são gerados arquivos CSV contendo:

Token (raiz resultante)

Número de ocorrências do token no documento resultante

Tamanho em caracteres de cada token
