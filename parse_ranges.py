

def parse_ranges(x):
    x = x.replace(" ", "").split(",")
    for y in x:
        y = y.replace("->", "-")
        if "-" in y:
            start, finish = y.split("-")
            if finish.isdigit():
                finish = int(finish)
            else:
                finish = start
            for i in range(int(start), int(finish)+1):
                yield i
        else:
            yield int(y)

numbers = parse_ranges('1-2,4-4,8-10')
print(parse_ranges('0-0, 4-8, 20-20, 43-45'))