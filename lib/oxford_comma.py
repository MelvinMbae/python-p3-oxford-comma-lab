def oxford_comma(items):
    if len(items) == 1:
        return "".join(items)
    elif len(items) ==2:
        return " and ".join(items)
    else:
        comma_separator = ", ".join(items[:-1])
        return f"{comma_separator}, and {items[-1]}"

items = ["kiwi", "durian", "starfruit"]
print(oxford_comma(items))
