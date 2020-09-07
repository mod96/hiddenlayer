def solution(w,h): # 가로 + 세로 - 최대공약수
    W, H = sorted([w,h])
    while W != 0:
        (H, W) = (W, H % W)
    return w * h - (w + h - H)

# w,h 문제를 w/g, h/g 문제로 축소시킬 수 있고
# w/g, h/g 에서 격자가 없으므로 만나는 사각형 개수는 w/g + h/g - 1
# 마지막으로 x g 해주면 가로 + 세로 - 최대공약수 가 정답이 됨.
# https://m.blog.naver.com/orbis1020/220664563768

print(solution(8,12))