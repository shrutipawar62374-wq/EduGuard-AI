
def check_question(question):

    text = question.lower()

    unsafe_words = [
        "hack someone's account",
        "steal password",
        "make a bomb",
        "kill someone",
        "create malware",
        "steal data"
    ]

    for word in unsafe_words:
        if word in text:
            return False, "I cannot help with harmful or unauthorized activities."

    educational_words = [
        "what", "why", "how", "explain", "define",
        "describe", "difference", "meaning", "uses",
        "advantages", "disadvantages", "example",
        "python", "java", "computer", "science",
        "artificial intelligence", "machine learning",
        "database", "programming", "algorithm",
        "education", "mathematics", "technology"
    ]

    if any(word in text for word in educational_words):
        return True, "Question accepted."

    return False, "This question is outside my educational topic."


def retrieve_knowledge(question):

    with open("knowledge.txt", "r", encoding="utf-8") as file:
        knowledge = file.read()

    question_words = question.lower().split()

    relevant_lines = []

    for line in knowledge.splitlines():

        if any(word in line.lower() for word in question_words):
            relevant_lines.append(line)

    return "\n".join(relevant_lines)
