# simplified_markdown_editor.py

def show_help():
    print("Доступні formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
    print("Special commands: !help !done")

def format_header():
    while True:
        level = input("Level: > ")
        if not level.isdigit() or not 1 <= int(level) <= 6:
            print("The level should be within the range of 1 to 6")
        else:
            break
    text = input("Text: > ")
    return f"{'#' * int(level)} {text}\n"

def format_plain():
    text = input("Text: > ")
    return text

def format_bold():
    text = input("Text: > ")
    return f"{text}"

def format_italic():
    text = input("Text: > ")
    return f"*{text}*"

def format_inline_code():
    text = input("Text: > ")
    return f"{text}"

def format_link():
    label = input("Label: > ")
    url = input("URL: > ")
    return f"[{label}]({url})"

def format_new_line():
    return "\n"

def format_ordered_list():
    while True:
        try:
            n = int(input("Number of rows: > "))
            if n <= 0:
                print("The number of rows should be greater than zero")
                continue
            break
        except ValueError:
            print("The number of rows should be greater than zero")
    result = ""
    for i in range(1, n + 1):
        row = input(f"Row #{i}: > ")
        result += f"{i}. {row}\n"
    return result

def format_unordered_list():
    while True:
        try:
            n = int(input("Number of rows: > "))
            if n <= 0:
                print("The number of rows should be greater than zero")
                continue
            break
        except ValueError:
            print("The number of rows should be greater than zero")
    result = ""
    for i in range(1, n + 1):
        row = input(f"Row #{i}: > ")
        result += f"* {row}\n"
    return result

def main():
    markdown_text = ""
    formatters = {
        "plain": format_plain,
        "bold": format_bold,
        "italic": format_italic,
        "header": format_header,
        "link": format_link,
        "inline-code": format_inline_code,
        "new-line": format_new_line,
        "ordered-list": format_ordered_list,
        "unordered-list": format_unordered_list,
    }

    while True:
        user_input = input("Choose a formatter: > ")
        if user_input == "!help":
            show_help()
        elif user_input == "!done":
            with open("output.md", "w", encoding="utf-8") as f:
                f.write(markdown_text)
            break
        elif user_input in formatters:
            markdown_text += formatters[user_input]()
            print(markdown_text)
        else:
            print("Unknown formatting type or command")

if __name__ == "__main__":
    main()