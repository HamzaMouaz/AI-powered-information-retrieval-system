import os

def read_documents(folder_path):
    documents = {}
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as f:
                documents[filename] = f.read()
    return documents


def save_to_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)