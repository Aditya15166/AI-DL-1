# Backward Chaining Algorithm

def backward_chaining(rules, facts, query):
    """
    Perform backward chaining to infer whether the query can be concluded from the given rules and facts.

    Parameters:
        rules: A list of rules in the format [(premise1, conclusion1), (premise2, conclusion2), ...]
        facts: A set of known facts.
        query: The goal we want to infer.

    Returns:
        True if the query can be inferred, False otherwise.
    """
    # If the query is a known fact, return True
    if query in facts:
        return True

    # Iterate over all rules
    for premise, conclusion in rules:
        # If the conclusion of the rule matches the query, check if the premise can be inferred
        if conclusion == query:
            # Recursively check if the premise can be inferred
            if backward_chaining(rules, facts, premise):
                return True

    # If no rule supports the query, return False
    return False


# Define rules in the format (premise, conclusion)
rules = [
    ("Rain", "Wet ground"),
    ("Cloudy", "Rain"),
    ("Sprinklers on", "Wet ground"),
    ("Cold", "Cloudy")
]

# Define known facts
facts = {"Cold", "Sprinklers on"}

# Define the query (the goal we want to check)
query = "Wet ground"

# Perform backward chaining to see if the query can be inferred
result = backward_chaining(rules, facts, query)

if result:
    print(f"The query '{query}' can be inferred.")
else:
    print(f"The query '{query}' cannot be inferred.")
