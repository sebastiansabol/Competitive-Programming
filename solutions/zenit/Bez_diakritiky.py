import unicodedata

nfkd = unicodedata.normalize('NFKD', text)
clean = ''.join(c for c in nfkd if not unicodedata.combining(c))
