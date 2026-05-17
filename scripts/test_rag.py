import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.services.rag_service import RagService

rag = RagService()
response = rag.ask("what is attention mechanism?")

print("\n")
print("=" * 50)
print("ANSWER")
print("=" * 50)
print(response['answer'])


print("\n")
print("=" * 50)
print("CONTEXT")
print("=" * 50)
for i, context in enumerate(response["contexts"]):
    print(f"Source{i+1}:")
    print(f"Metadata: {context['metadata']}")
    print(f"Score: {context['score']}")
    print(f"Text: {context['page_content']}")
    print("\n")
print("=" * 50)
print("END")
print("=" * 50
)