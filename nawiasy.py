def check_parentheses(s: str) -> bool:
    stos = []

    for znak in s:
        if znak == '(':
            stos.append(znak)
        elif znak == ')':
            if not stos:
                return False
            stos.pop()

    if len(stos) == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    examples = [
        "Czesc (o kurcze, chyba niechcacy zamkne ten nawias dwa razy))",
    ]
    for example in examples:
        print(f"{example} -> {check_parentheses(example)}")