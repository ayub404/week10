raw_scores = [
    ("Alice", "Math", 85),
    ("Bob", "Math", 75),
    ("Alice", "Physics", 90),
    ("Charlie", "History", 88),
    ("Bob", "Physics", 82),
    ("Alice", "History", 92)
]

def process_scoreses(raw_scores):
    gradebook = {}
    for name, subject, scores in raw_scores:
        if name not in gradebook:
            gradebook[name] = {subject: scores}
        gradebook[name][subject] = scores
        
    for name, subject in gradebook.items():
        print(f"{name}: {subject}")
    return gradebook
result = process_scoreses(raw_scores)

