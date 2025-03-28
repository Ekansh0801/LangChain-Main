from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.lazy_load()  
# lazy load help us when documents are very huge or in large quantity
# Returns a generator of documents
# Documents fetched once at a time


for document in docs:
    print(document.metadata)