def get_input() -> list:
    content = []

    while True:
        line = input()
        if line:
            content.append(line)
        else:
            break

    return content
