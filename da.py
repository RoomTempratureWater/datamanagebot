


def search(words):
    spcl = ['[','@','!','#','$','%','^','&','*','(',')','<','>','?','/','|','}','{','~',':',']','-','...']
    let_cnt = {}
    for i in range(0,len(words)-1):
        for element in words[i]:
            if element in spcl:
                continue
            elif element in words[i+1]:
                try:
                    let_cnt[element] += 1
                except:
                    let_cnt[element] = 1

    max_occur = max(let_cnt.values())
    cnt = 0
    res = ''
    for i in let_cnt:
        if let_cnt[i] == max_occur:
            cnt += 1
            res += i + ' '

    return res
