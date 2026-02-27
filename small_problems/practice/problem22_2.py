def solution(full_text, search_text):
    start = 0
    count = 0

    while True:
        pos = full_text.find(search_text, start)
        if pos == -1:
            break
        count += 1
        start = pos + 1

    return count