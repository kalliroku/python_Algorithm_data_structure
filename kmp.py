def kmp_math(txt, pat):
    pt = 1
    pp = 0
    skip = [0] * (len(pat) + 1)

    # 건너 뛰기 표 만들기
    skip[pt] = 0
    while pt != len(pat):
        if pat[pt] == pat[pp]:
            pt += 1
            pp += 1
            skip[pt] = pp
        elif pp == 0:
            pt += 1
            skip[pt] = pp
        else: #여기가 핵심 일진데...
    while pt != len(txt) and pp != len(pat):
        if pat[pt] == pat[pp]:
            pp = skip[pp]
            pt += 1
            pp += 1
            skip[pt] = pp
        elif pp == 0:
            pt += 1
            skip[pt] = pp
        else: #여기가 핵심 일진데...
            pp = skip[pp]

    print(skip)

pat = "abcabd"

kmp_math(pat)
