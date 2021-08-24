def parse(rec: str):
    sp = rec.split()
    d = dict()
    for score, item in enumerate(reversed(sp[1:]), start=1):
        d[item] = score

    return sp[0], d


def solution(table, languages, preference):
    max_score = 0
    titles = []
    for rec in table:
        title, d = parse(rec)
        score = sum(d.get(lang, 0) * pref for lang, pref in zip(languages, preference))
        if max_score == score:
            titles.append(title)
        elif max_score < score:
            titles.clear()
            max_score = score
            titles.append(title)

    titles.sort()
    return titles[0]


def main():
    assert solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
                     "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
                     "GAME C++ C# JAVASCRIPT C JAVA"], ["PYTHON", "C++", "SQL"], [7, 5, 5]) == "HARDWARE"
    assert solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
                     "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
                     "GAME C++ C# JAVASCRIPT C JAVA"], ["JAVA", "JAVASCRIPT"], [7, 5]) == "PORTAL"


if __name__ == '__main__':
    main()
