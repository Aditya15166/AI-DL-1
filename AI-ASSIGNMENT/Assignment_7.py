# Foreword channing algorithm

def forward_chaining(rules, facts):
    inferred = set()
    agenda = facts.copy()

    while agenda:
        fact = agenda.pop(0)
        if fact not in inferred:
            inferred.add(fact)
            for premise, conclusion in rules:
                if premise == fact and conclusion not in inferred:
                    agenda.append(conclusion)
    return inferred

rules = [("A", "B"), ("B", "C"), ("C", "D")]
facts = ["A"]
inferred_facts = forward_chaining(rules, facts)
print("Inferred facts:", inferred_facts)
