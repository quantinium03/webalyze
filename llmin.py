from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

template = (
    "You are tasked with extracting specific information from the following text_content: {dom_stuff}."
    "Please follow these instructions carefully: \n\n"
    "1. **Extract information:** Only extract the information that directly matches the provided description: {parse_desciption}."
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response."
    "3. **Empty Response:** If no information matches the description, return an empty string ('' )."
    "4. **Direct data only:** Your output should contain only the data that is explicitly requested, with no other text."
)

model = OllamaLLM(model="llama3.1")

def parse_with_llm(dom_chunks, parse_desciption):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    result = []
    for i, chunk in enumerate(dom_chunks, start=1):
        try:
            res = chain.invoke({"dom_stuff": chunk, "parse_desciption": parse_desciption})
            print(f"Parsed batch {i} of len {len(dom_chunks)}")
            result.append(res)
        except Exception as e:
            print(f"Error parsing chunk {i}: {str(e)}")
            result.append('')  # Append empty string on error

    return "\n".join(result)
