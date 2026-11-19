
import json
import csv
from guardrails import check_question, retrieve_knowledge

with open("evaluation_dataset.json", "r", encoding="utf-8") as file:
    dataset = json.load(file)

correct = 0
total = len(dataset)

results = []

for item in dataset:

    question = item["question"]
    expected = item["expected"]

    allowed, message = check_question(question)

    if expected == "answer":
        if allowed and retrieve_knowledge(question):
            actual = "answer"
        else:
            actual = "reject"

    else:
        if not allowed:
            actual = "reject"
        else:
            actual = "answer"

    if actual == expected:
        correct += 1
        status = "PASS"
    else:
        status = "FAIL"

    results.append([
        question,
        item["category"],
        expected,
        actual,
        status
    ])

accuracy = (correct / total) * 100

with open("results/evaluation_results.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    writer.writerow([
        "Question",
        "Category",
        "Expected",
        "Actual",
        "Result"
    ])

    writer.writerows(results)

print("======= EVALUATION RESULTS =======")
print("Total Questions:", total)
print("Correct Results:", correct)
print("Incorrect Results:", total - correct)
print("Evaluation Score:", round(accuracy, 2), "%")
print("Results saved in results/evaluation_results.csv")
