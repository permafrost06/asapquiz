from loremipsum import get_sentences

questions = []
question = {}

for i in range(1,21):
    question["text"] = get_sentences(1)[0] + " " + get_sentences(1)[0]
    question["option_a"] = get_sentences(1)[0]
    question["option_b"] = get_sentences(1)[0]
    question["option_c"] = get_sentences(1)[0]
    question["option_d"] = get_sentences(1)[0]
    questions.append(question)

print(questions)