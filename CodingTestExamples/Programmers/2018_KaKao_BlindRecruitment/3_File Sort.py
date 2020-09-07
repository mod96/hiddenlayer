def solution(files):
    nums = [str(i) for i in range(10)]
    def key_function(elt):
        head, number = '', ''
        i = 0
        while elt[i] not in nums:
            head += elt[i]
            i += 1
        while i < len(elt) and elt[i] in nums and len(number) < 5:
            number += elt[i]
            i += 1
        return (head.lower(),int(number))

    files.sort(key = key_function)
    return files

print(solution(['img12.png', 'img10.png', 'img02.png', 'img1.png', 'IMG01.GIF', 'img2.JPG']))
print(solution(['F-5 Freedom Fighter', 'B-50 Superfortress', 'A-10 Thunderbolt II', 'F-14 Tomcat']))