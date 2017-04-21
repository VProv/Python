import argparse
import re
import sys


def read_from_file(file_name):
    file = open(file_name, "r")
    text = ""
    for line in file.readlines():
        text += line
    file.close()
    return text


def format_text(text, max_line_length, paragraph_spaces):
    text_list = re.findall(r'[A-Za-z0-9]+|[,.?!\-:\'\n]', text)
    separators = [',', '.', '?', '!', '-', ':', "'"]
    new_paragraph_flag = True
    new_line_counter = 0
    new_text_list = []
    for index in range(len(text_list)):
        if text_list[index] != '\n':
            new_line_counter = 0
        if text_list[index] == '\n':
            new_line_counter += 1
            # Element \n means new paragraph.
            if new_line_counter == 2:
                new_paragraph_flag = True
        elif text_list[index] in separators:
            if new_paragraph_flag:
                new_paragraph_flag = False
                new_text_list.append('\n')
                new_text_list.append(text_list[index])
            else:
                new_text_list[-1] += str(text_list[index])
        else:
            if new_paragraph_flag:
                new_paragraph_flag = False
                new_text_list.append('\n')
            new_text_list.append(text_list[index])

    first_paragraph_flag = True
    result = " " * paragraph_spaces
    current_line_length = paragraph_spaces
    for word in new_text_list:
        if len(word) > max_line_length:
            raise Exception("Too long word")
        if word == '\n':
            if first_paragraph_flag:
                first_paragraph_flag = False
                continue
            result += '\n' + ' ' * paragraph_spaces
            current_line_length = paragraph_spaces
        else:
            if current_line_length + len(word) <= max_line_length:
                if current_line_length == 0:
                    current_line_length += len(word)
                    result += word
                else:
                    if result[-1] != ' ':
                        result += ' ' + word
                        current_line_length += len(word) + 1
                    else:
                        result += word
                        current_line_length += len(word)
            else:
                result += '\n' + word
                current_line_length = len(word)

    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', default=None)
    parser.add_argument('-o', '--output', default=None)
    parser.add_argument('-l', '--line-length', default=None)
    parser.add_argument('-p', '--paragraph-spaces', default=None)
    args = parser.parse_args()

    text = ""
    # Read text.
    if args.input is not None:
        text = read_from_file(args.input)
    else:
        for line in sys.stdin.readlines():
            text += line

    max_line_length = 80
    if args.line_length is not None:
        max_line_length = int(args.line_length)

    paragraph_spaces = 4
    if args.paragraph_spaces is not None:
        paragraph_spaces = int(args.paragraph_spaces)
    if paragraph_spaces >= max_line_length:
        raise Exception("Too many paragraph spaces")
    result = format_text(text, max_line_length, paragraph_spaces)

    if args.output is not None:
        file = open(args.output, "w")
        file.write(result)
        file.close()
    else:
        sys.stdout.write(result)

main()
