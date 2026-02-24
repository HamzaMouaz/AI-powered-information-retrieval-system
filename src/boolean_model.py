from src.preprocessing import preprocess

def boolean_search(query, inverted_index):
    tokens = query.split()

    if not tokens:
        return []

    result = None
    operator = None

    for token in tokens:
        if token.upper() in ["AND", "OR", "NOT"]:
            operator = token.upper()
        else:
            processed = preprocess(token)
            if not processed:
                continue

            term = processed[0]
            docs = inverted_index.get(term, set())

            if result is None:
                result = docs
            else:
                if operator == "AND":
                    result = result.intersection(docs)
                elif operator == "OR":
                    result = result.union(docs)
                elif operator == "NOT":
                    result = result.difference(docs)

    return list(result) if result else []