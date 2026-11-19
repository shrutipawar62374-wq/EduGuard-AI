
# EduGuard AI

## Safe and Grounded Educational Assistant

### 1. Introduction

EduGuard AI is an AI-powered educational assistant developed using Python and the OpenAI API.

It is designed to answer educational questions using an approved knowledge base while rejecting unrelated and unsafe requests.

### 2. Objectives

- Build an educational AI chatbot.
- Implement topic-based guardrails.
- Prevent unsafe responses.
- Use a knowledge base for grounded answers.
- Evaluate chatbot performance.
- Measure token usage and estimated API cost.

### 3. Technologies Used

- Python
- OpenAI API
- JSON
- CSV
- GitHub

### 4. Main Features

1. Educational question answering.
2. Off-topic question rejection.
3. Unsafe request detection.
4. Knowledge-based responses.
5. Automated evaluation.
6. Evaluation score calculation.
7. Token usage tracking.
8. Estimated API cost calculation.

### 5. Project Structure

- main.py: Main chatbot application.
- guardrails.py: Question checking and knowledge retrieval.
- knowledge.txt: Educational knowledge base.
- evaluation_dataset.json: Testing questions.
- evaluation.py: Evaluation program.
- requirements.txt: Required library.
- results/evaluation_results.csv: Evaluation report.

### 6. Installation

Install the required library:

pip install -r requirements.txt

Set your OpenAI API key as an environment variable.

### 7. How to Run

Run the chatbot:

python main.py

Run the evaluation:

python evaluation.py

Type exit to close the chatbot and display token usage.

### 8. Evaluation

The evaluation dataset contains educational, off-topic and unsafe questions.

The evaluation program compares actual results with expected results and calculates the evaluation score.

### 9. Cost Measurement

The chatbot records input tokens and output tokens for API requests and calculates an estimated API cost.

### 10. Conclusion

EduGuard AI demonstrates how an AI assistant can be developed with topic restrictions, safety checks, knowledge-based responses and performance evaluation.

The project provides a simple example of building a responsible and measurable AI assistant.
