class promptBuilder:
    @staticmethod
    def build_prompt(query:str, retrieved_chunks) -> str:
        context_blocks=[]
        for idx, chunk in enumerate(retrieved_chunks,1):
            if isinstance(chunk, tuple):
                text= chunk[0]
            elif isinstance(chunk, dict):
                text = (chunk.get("page_content",""))
            else:
                text = str(chunk)

        context_blocks = "\n\n".join(context_blocks)

        prompt = f"""
            You are a grounded AI assitant
            Answer ONLY from the provided context below. 

            Rules:
            1. Do NOT hallucinate.
            2. Do NOT invent information.
            3. if information is missing say "I could not find enough information"
            4. Use concise technical explanation
            5. prefer factual accuracy over fluency.

            Retrevied context:
            {context_blocks}

            User Question:
            {query}

            Answer:
            """
        return prompt