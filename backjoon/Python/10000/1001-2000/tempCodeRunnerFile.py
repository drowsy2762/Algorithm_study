for string in strings:
    for i in range(len(string)):
        if string[i][0].lower() not in skey:
            skey.append(string[i][0].lower())

            string[i] = "[" + string[i][0] + "]" + string[i][1:]
            break
        else:
            for j in range(len(string)):
                if string[i][j].lower() not in skey:
                    skey.append(string[i][j].lower())
                    string[i] = string[i][:j] + '[' + string[i][j] + ']' + string[i][j:]
                    break
                break