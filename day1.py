from input_template import get_input

content = get_input()

number_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def get_numbers(line: str):
    numbers = [(i, c) for i, c in enumerate(line) if c.isdigit()]

    # Part one
    first_digit = numbers[0]
    last_digit = numbers[-1]

    # Part two
    first_word = (9999, None)
    last_word = (-9999, None)
    for key, value in number_map.items():
        fw = line.find(key)
        lw = line.rfind(key)

        if fw == -1:
            continue
        elif fw < first_word[0]:
            first_word = (fw, value)

        if lw == -1:
            continue
        elif lw > last_word[0]:
            last_word = (lw, value)

    first = min(first_digit, first_word)
    last = max(last_digit, last_word)

    number = int(first[1] + last[1])
    return number


answer = sum([get_numbers(x) for x in content])
print(answer)
