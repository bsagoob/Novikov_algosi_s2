valid_tags = {'a', 'abbr', 'b', 'body', 'caption', 'cite', 'code', 'div', 'form',
              'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'header', 'i', 's'}

tag = input()
text = input()

if tag in valid_tags:
    print(f"<{tag}>{text}</{tag}>")
else:
    print("Введён неверный тег")
