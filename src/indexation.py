from collections import defaultdict
from src.preprocessing import preprocess
from src.utils import read_documents, save_to_file

def create_descriptors(documents):
    descriptors = {}
    for doc_name, content in documents.items():
        tokens = preprocess(content)
        descriptors[doc_name] = tokens
    return descriptors


def create_inverted_index(descriptors):
    inverted_index = defaultdict(set)

    for doc_name, terms in descriptors.items():
        for term in terms:
            inverted_index[term].add(doc_name)

    return inverted_index


def build_index(collection_path, output_path):
    documents = read_documents(collection_path)

    descriptors = create_descriptors(documents)
    inverted_index = create_inverted_index(descriptors)

    # Sauvegarde descripteurs
    desc_text = ""
    for doc, terms in descriptors.items():
        desc_text += f"{doc}: {', '.join(terms)}\n"
    save_to_file(f"{output_path}/descripteurs.txt", desc_text)

    # Sauvegarde index inversé
    inv_text = ""
    for term, docs in inverted_index.items():
        inv_text += f"{term}: {', '.join(docs)}\n"
    save_to_file(f"{output_path}/index_inverse.txt", inv_text)

    return inverted_index