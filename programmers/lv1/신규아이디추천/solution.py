def solution(new_id):
    canUse = [chr(x) for x in range(97,123)]
    canUse += [str(n) for n in range(0,10)]
    canUse += ["-","_","."]
    canUse = set(canUse)

    new_id = list(new_id)

    # step1
    for i,c in enumerate(new_id):
        if c.isupper():
            new_id[i] = c.lower()

    # step2
    new_id = [c for c in new_id if c in canUse]
    
    # step3
    if new_id:
        for i, c in enumerate(new_id):
            if c == "." and new_id[i-1] == ".":
                new_id[i-1] = ""

        new_id = list("".join(new_id))

    # step4
    if new_id and set(new_id) != {"."}:
        if new_id[0] == ".":
            del new_id[0]
        if new_id[-1] == ".":
            del new_id[-1]

    # step5
    else:
        new_id.clear()
        new_id.append("a")

    # step6
    if len(new_id) > 15:
        new_id = new_id[:15]
        if new_id[-1] == ".":
            del new_id[-1]

    new_id = "".join(new_id)

    # step7
    while len(new_id) < 3:
        new_id += new_id[-1]

    return new_id
    

