"""import string

def solution(word, pages):
    word = word.lower()
    DP = [[] for i in range(len(pages))]
    links = {}
    page_names_to_i = {}
    i_to_page_names = {}
    alphabets = string.ascii_lowercase
    l = len(word)
    for i, page in enumerate(pages):
        # in
        inner = 0
        pars = page.lower().replace('\n',' ').replace('\t',' ')
        idxs = [-1]
        while word in pars[idxs[-1]+1:]:
            idxs.append(pars.index(word,idxs[-1]+1))
        del idxs[0]
        for idx in idxs:
            bool1 = idx == 0 and pars[idx+l] not in alphabets
            bool2 = idx + l == len(pars) and pars[idx-1] not in alphabets
            if bool1 or bool2:
                inner += 1
            elif pars[idx-1] not in alphabets and pars[idx+l] not in alphabets:
                inner += 1

        # out
        outer = 0
        lines = page.lower().split('\n')
        to_link = []
        for line in lines:
            element = line.strip()
            if '<a href' in element:
                outer += 1
                k = element.index('https://')
                temp = element[k:element.index('''"''',k+1)]
                to_link.append(temp)
            # self content
            if '<meta' in element and 'content' in element:
                k = element.index('https://')
                my_link = element[k:element.index('''"''',k+1)]

        for to in to_link:
            links.setdefault(to,[]).append(my_link)
        page_names_to_i[my_link] = i
        i_to_page_names[i] = my_link
        # save
        DP[i] = [i,inner,outer]

    for i, dp in enumerate(DP):
        page_name = i_to_page_names[i]
        new_val = int(dp[1])
        if page_name in links:
            for connected in links[page_name]:
                if connected in page_names_to_i:
                    j = page_names_to_i[connected]
                    new_val += DP[j][1]/DP[j][2]

        dp.append(new_val)
    #print(page_names_to_i)
    #print(i_to_page_names)
    #print(links)

    ans = max(DP,key=lambda tup : (tup[3],-tup[0]))

    return ans[0]"""

import string

def solution(word, pages):
    word = word.lower()
    DP = [[] for i in range(len(pages))]
    links = {}
    page_names_to_i = {}
    i_to_page_names = {}
    alphabets = string.ascii_lowercase
    l = len(word)
    for i, page in enumerate(pages):
        # in
        inner = 0
        pars = page.lower().replace('\n',' ').replace('\t',' ').replace('\"','"').replace('  ',' ')
        idxs = [-1]
        while word in pars[idxs[-1]+1:]:
            idxs.append(pars.index(word,idxs[-1]+1))
        del idxs[0]
        for idx in idxs:
            if pars[idx-1] not in alphabets and pars[idx+l] not in alphabets:
                inner += 1

        # self content
        targ = pars[pars.index('<head>'):pars.index('</head>')]
        idxs = [-1]
        while '<meta' in targ[idxs[-1]+1:]:
            idxs.append(targ.index('<meta',idxs[-1]+1))
        del idxs[0]
        for idx in idxs:
            end = targ.index('>',idx)
            temp = targ[idx:end]
            if 'https://' in temp:
                q = temp.index('https://',temp.index('content'))
                my_link = temp[q:temp.index('''"''',q+1)].strip()

        # out
        to_link = []
        idxs = [-1]
        while '<a' in pars[idxs[-1]+1:]:
            idxs.append(pars.index('<a',idxs[-1]+1))
        del idxs[0]
        for idx in idxs:
            k = pars.index('https://',idx)
            to_link.append(pars[k:pars.index('''"''',k+1)].strip())
        outer = len(idxs)

        for to in to_link:
            links.setdefault(to,[]).append(my_link)
        page_names_to_i[my_link] = i
        i_to_page_names[i] = my_link
        # save
        DP[i] = [i,inner,outer]

    for i, dp in enumerate(DP):
        page_name = i_to_page_names[i]
        new_val = int(dp[1])
        if page_name in links:
            for connected in links[page_name]:
                if connected in page_names_to_i:
                    j = page_names_to_i[connected]
                    new_val += DP[j][1]/DP[j][2]

        dp.append(new_val)
    #print(page_names_to_i)
    #print(i_to_page_names)
    print(links)
    #print(DP)

    ans = max(DP,key=lambda tup : (tup[3],-tup[0]))

    return ans[0]

print(solution('blind',["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]))
print(solution('Muzi',["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]))
