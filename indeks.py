def index_documents(documents: list[str], queries: list[str]) -> list[list[int]]:
    oczyszczone_dokumenty = []

    for doc in documents:
        doc_lower = doc.lower()
        for znak in ".,!?:;\"'()[]{}":
            doc_lower = doc_lower.replace(znak, ' ')
        oczyszczone_dokumenty.append(doc_lower.split())

    results = []
    for q in queries:
        q_lower = q.lower()
        znalezienia = []

        for doc_idx in range(len(oczyszczone_dokumenty)):
            ilosc = oczyszczone_dokumenty[doc_idx].count(q_lower)
            if ilosc > 0:
                znalezienia.append((ilosc, doc_idx))

        znalezienia.sort(key=lambda x: (-x[0], x[1]))

        indeksy = []
        for element in znalezienia:
            indeksy.append(element[1])

        results.append(indeksy)

    return results

if __name__ == "__main__":
    n = int(input("Podaj liczbę dokumentów: "))
    documents = []
    print("Wprowadź kolejne dokumenty:")
    for _ in range(n):
        documents.append(input())

    m = int(input("Podaj liczbę zapytań: "))
    queries = []
    print("Wprowadź kolejne zapytania:")
    for _ in range(m):
        queries.append(input().strip())

    results = index_documents(documents, queries)

    print("Wyniki:")
    for res in results:
        print(res)