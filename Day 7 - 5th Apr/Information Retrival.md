# Information Retreival Basics

“Information Retrieval (IR) is finding material (usually documents) of an unstructured nature (usually text) that satisfies an information need from within large collections (usually stored on computers).” — Manning et al. It deals with the organization, storage, retrieval, and evaluation of information from document repositories, particularly textual information.

Why IR? Deals with *information overload*.

* Document
* Collection - A set of documents (sometimes static)

### Boolean Retrieval
* Indexing - Storing a mapping from terms to documents
* Querying - Looking up terms in the index and returning documents
* Boolean retrieval procedures - Lookup query term in the dictionary to retrieve the list of relevant documents (i.e. posting lists)
* Operations - AND: intersect the posting lists; OR: union the posting list; NOT: diff the posting list
