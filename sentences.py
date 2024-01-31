import random

def get_determiner(quantity):
    """Return a randomly chosen determiner."""
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    return random.choice(words)

def get_noun(quantity):
    """Return a randomly chosen noun."""
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

    return random.choice(words)

def get_verb(quantity, tense):
    """Return a randomly chosen verb."""
    verbs_past = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    verbs_present_singular = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    verbs_present_plural = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    verbs_future = [f"will {v}" for v in verbs_present_singular]

    if tense == "past":
        return random.choice(verbs_past)
    elif tense == "present" and quantity == 1:
        return random.choice(verbs_present_singular)
    elif tense == "present" and quantity != 1:
        return random.choice(verbs_present_plural)
    elif tense == "future":
        return random.choice(verbs_future)

def get_preposition():
    """Return a randomly chosen preposition."""
    prepositions = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below",
                    "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of",
                    "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]

    return random.choice(prepositions)

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed of three words."""
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)

    prepositional_phrase = f"{preposition} {determiner} {noun}"
    return prepositional_phrase

def make_sentence(quantity, tense):
    """Build and return a sentence with four parts: a determiner, a noun, a verb, and a prepositional phrase."""
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    prepositional_phrase = get_prepositional_phrase(quantity)

    sentence = f"{determiner.capitalize()} {noun} {verb} {prepositional_phrase}."
    return sentence

def main():
    # Generate and print six sentences with different characteristics
    sentences = [
        ("single", "past"),
        ("single", "present"),
        ("single", "future"),
        ("plural", "past"),
        ("plural", "present"),
        ("plural", "future"),
    ]

    for quantity, tense in sentences:
        sentence = make_sentence(quantity, tense)
        print(sentence)

if __name__ == "__main__":
    main()
