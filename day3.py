from input_template import get_input

content = get_input()

# lines = [line for line in content]


def symbol_index(symbol, i, j):
    print(f"Symbol: {symbol} at ({i},{j})")


# print(not ".".isdigit())

part_numbers = []

for i, line in enumerate(content):
    current_number = ""
    current_number_line = i
    cn_valid = False

    for j, symbol in enumerate(line):
        if not symbol.isdigit():
            # print(current_number, f"Is valid: {cn_valid}")
            if cn_valid:
                part_numbers.append(int(current_number))

            current_number = ""
            current_number_indices = []
            cn_valid = False

        if symbol.isdigit():
            current_number += symbol

            # Is at start of line
            if j == 0:
                # Check for symbol on right
                if content[i][j + 1] != "." and not content[i][j + 1].isdigit():
                    cn_valid = True

                # Is at first row
                if i == 0:
                    # Check for symbol below
                    if content[i + 1][j] != ".":
                        cn_valid = True
                    # Check for symbol on right below
                    if content[i + 1][j + 1] != ".":
                        cn_valid = True

                # Is at the last row
                elif i == len(content) - 1:
                    # Check for symbol above
                    if content[i - 1][j] != ".":
                        cn_valid = True
                    # Check for symbol on right above
                    if content[i - 1][j + 1] != ".":
                        cn_valid = True

                # Is in any other row
                else:
                    # Check for symbol above
                    if content[i - 1][j] != ".":
                        cn_valid = True

                    # Check for symbol below
                    if content[i + 1][j] != ".":
                        cn_valid = True

                    # Check for symbol on right below
                    if content[i + 1][j + 1] != ".":
                        cn_valid = True

                    # Check for symbol on right above
                    if content[i - 1][j + 1] != ".":
                        cn_valid = True

            # Is at end of line
            elif j == len(line) - 1:
                # Check for symbol on left
                if content[i][j - 1] != "." and not content[i][j - 1].isdigit():
                    cn_valid = True

                # Is at first row
                if i == 0:
                    # Check for symbol below
                    if content[i + 1][j] != ".":
                        cn_valid = True
                    # Check for symbol left below
                    if content[i + 1][j - 1] != ".":
                        cn_valid = True

                # Is at the last row
                elif i == len(content) - 1:
                    # Check for symbol above
                    if content[i - 1][j] != ".":
                        cn_valid = True
                    # Check for symbol left above
                    if content[i - 1][j - 1] != ".":
                        cn_valid = True
                # Is in any other row
                else:
                    # Check for symbol above
                    if content[i - 1][j] != ".":
                        cn_valid = True

                    # Check for symbol below
                    if content[i + 1][j] != ".":
                        cn_valid = True

                    # Check for symbol left below
                    if content[i + 1][j - 1] != ".":
                        cn_valid = True

                    # Check for symbol left above
                    if content[i - 1][j - 1] != ".":
                        cn_valid = True

            # Is in any other position of the line
            else:
                # Check for symbol on right
                if content[i][j + 1] != "." and not content[i][j + 1].isdigit():
                    cn_valid = True

                # Check for symbol on left
                if content[i][j - 1] != "." and not content[i][j - 1].isdigit():
                    cn_valid = True

                # Is at the first row
                if i == 0:
                    # Check for symbol below
                    if content[i + 1][j] != ".":
                        cn_valid = True
                    # Check for symbol left below
                    if content[i + 1][j - 1] != ".":
                        cn_valid = True
                    # Check for symbol on right below
                    if content[i + 1][j + 1] != ".":
                        cn_valid = True

                # Is at the last row
                elif i == len(content) - 1:
                    # Check for symbol above
                    if content[i - 1][j] != ".":
                        cn_valid = True
                    # Check for symbol left above
                    if content[i - 1][j - 1] != ".":
                        cn_valid = True
                    # Check for symbol on right above
                    if content[i - 1][j + 1] != ".":
                        cn_valid = True

                # Is in any other row
                else:
                    # Check for symbol below
                    if content[i + 1][j] != ".":
                        cn_valid = True
                    # Check for symbol left below
                    if content[i + 1][j - 1] != ".":
                        cn_valid = True
                    # Check for symbol on right below
                    if content[i + 1][j + 1] != ".":
                        cn_valid = True
                    # Check for symbol above
                    if content[i - 1][j] != ".":
                        cn_valid = True
                    # Check for symbol left above
                    if content[i - 1][j - 1] != ".":
                        cn_valid = True
                    # Check for symbol on right above
                    if content[i - 1][j + 1] != ".":
                        cn_valid = True

        if cn_valid and j == len(line) - 1:
            part_numbers.append(int(current_number))

        # print(current_number, f"Is valid: {cn_valid}")

part_numbers = [int(number) for number in part_numbers]

# [print(numb) for numb in part_numbers]
sum_of_part_numbers = sum(part_numbers)
print(sum_of_part_numbers)
