import random

questions = {
    "Cloud Computing": [
        "What is the difference between IaaS, PaaS, and SaaS?",
        "Explain how AWS EC2 works.",
        "What is Kubernetes and why is it used?"
    ],
    "Software Engineering": [
        "Explain object-oriented programming.",
        "What are design patterns?",
        "What is REST API?"
    ],
    "Machine Learning": [
        "What is overfitting?",
        "Explain supervised vs unsupervised learning.",
        "What is gradient descent?"
    ],
    "Data Science": [
        "What is feature engineering?",
        "Explain the bias-variance tradeoff.",
        "What is a confusion matrix?"
    ]
}

def generate_question(domain):
    return random.choice(questions[domain])
