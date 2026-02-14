import random

# Names by number of letters (length -> list of names)
NAMES_BY_LENGTH = {
    2: ["Bo", "Jo", "Al", "Ed", "Mo"],
    3: ["Bob", "Joe", "Amy", "Eva", "Max", "Leo", "Sam", "Kim"],
    4: ["Anna", "John", "Emma", "Luke", "Noah", "Lucy", "Mark", "Jane"],
    5: ["Sarah", "David", "James", "Emily", "Chris", "Peter", "Maria", "Steve"],
    6: ["Daniel", "Sophie", "Oliver", "Isabel", "Samuel", "Rachel", "Thomas", "Lauren"],
    7: ["Michael", "William", "Jessica", "Oliviaa", "Anthony", "Amanada", "Asheley"],
    8: ["Alexandr", "Victoria", "Nicholas", "Jennifer", "Benjamin", "Margaret"],
    9: ["Elizabeth", "Alexander", "Katherine", "Sebastian", "Nathaniel"],
    10: ["Christofer", "Alexandera", "Maximilian"],
    11: ["Christopher"],
    12: ["Christabella"],
}

def name_with_letters(n):
    """Return a string of exactly n characters (names + spaces between them)."""
    if n <= 0:
        return ""
    if n == 1:
        return random.choice(NAMES_BY_LENGTH[2])[0]  # one letter from a 2-letter name
    if n in NAMES_BY_LENGTH:
        return random.choice(NAMES_BY_LENGTH[n])
    # Build a mixture: first name + space + rest; total chars = n (space counts)
    part_len = random.randint(2, min(12, n - 3))  # leave room for space and at least 1 char
    return random.choice(NAMES_BY_LENGTH[part_len]) + " " + name_with_letters(n - part_len - 1)

for i in [random.randint(j * 10, j * 10 + 9) for j in range(10)]:
    name = name_with_letters(i)
    print(name, i, len(name))
