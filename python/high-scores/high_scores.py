def latest(scores):
    return scores[-1]

def personal_top_three(scores):
    sorted_score = sorted(scores, reverse=True)
    print(sorted_score)
    return sorted_score[:3]

def personal_best(scores):
    sorted_score = sorted(scores, reverse=True)
    return sorted_score[0]


