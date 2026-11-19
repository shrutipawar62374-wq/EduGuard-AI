
import json
from openai import OpenAI
from guardrails import check_question, retrieve_knowledge

client = OpenAI()

total_input_tokens = 0
total_output_tokens = 0

def ask_question(question):

    global total_input_tokens, total_output_tokens

    allowed, message = check_question(question)

    if not allowed:
        print("\nEduGuard AI:", message)
        return

    knowledge = retrieve_knowledge(question)

    if not knowledge:
        print("\nEduGuard AI: Sorry, I don't have enough information in my knowledge base to answer this question.")
        return

    prompt = f"""
You are EduGuard AI, a safe educational assistant.

Rules:
1. Answer only educational questions.
2. Use only the provided knowledge.
3. Do not invent information.
4. If the answer is not available, say so.
5. Never provide harmful instructions.

Knowledge:
{knowledge}

Student Question:
{question}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    answer = response.choices[0].message.content

    total_input_tokens += response.usage.prompt_tokens
    total_output_tokens += response.usage.completion_tokens

    print("\nEduGuard AI:", answer)

def show_usage():

    print("\n----- TOKEN USAGE -----")
    print("Input Tokens:", total_input_tokens)
    print("Output Tokens:", total_output_tokens)
    print("Total Tokens:", total_input_tokens + total_output_tokens)

    print("\nEstimated API Cost (USD):")
    input_cost = total_input_tokens * 0.00000015
    output_cost = total_output_tokens * 0.00000060

    print("Total Cost: $", round(input_cost + output_cost, 8))

print("================================")
print("       EDUGUARD AI")
print(" Safe Educational Assistant")
print("================================")

while True:

    question = input("\nStudent: ")

    if question.lower() == "exit":
        show_usage()
        print("\nThank you for using EduGuard AI!")
        break

    ask_question(question)
