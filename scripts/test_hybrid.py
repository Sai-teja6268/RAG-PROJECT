import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.retrieval.hybrid_retriever import HybridRetriever

def main():
    retriever = HybridRetriever()
    results = retriever.search("What is attention mechanism?")
    
    for i, result in enumerate(results,1):
        print(f"Result {i}: {result['score']:.4f}")
        content = result['page_content'].encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding)
        print(f"Page Content: {content}")
        print(f"Source: {result['metadata'].get('source', 'unknown')}")
        print("="*50)

if __name__ == "__main__":
    main()