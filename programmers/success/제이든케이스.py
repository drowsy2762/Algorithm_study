def 해결책(문자열: str) -> str:
    결과_목록 = []
    단어_첫글자_확인 = True

    for 한글자 in 문자열:
        if 한글자 == " ":
            결과_목록.append(한글자)
            단어_첫글자_확인 = True
        else:
            if 단어_첫글자_확인:
                결과_목록.append(한글자.upper())
                단어_첫글자_확인 = False
            else:
                결과_목록.append(한글자.lower())

    return "".join(결과_목록)
