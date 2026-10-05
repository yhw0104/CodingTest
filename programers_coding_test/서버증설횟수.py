def solution(players, m, k):
    answer = 0
    
    servers = []
    cnt = 1
    for player in players:
        count = 0 #열려있는 서버 수
        for server in servers:
            if server > 0:    
                count += 1
                # print("생성되어있는 서버 수: ", count)
        need = player // m - count # 필요한 증설 서버 수
        # print(cnt, "번째 시각 사용자 수: ", player)
        cnt += 1
        # print("필요한 증설 서버 수: ", need)
        if need > 0 :
            answer += need
            for i in range(need):
                servers.append(k)

        for i in range(len(servers)):
            if servers[i] != 0:
                servers[i] -= 1

        # print("생성되어있는 서버", servers)
        # print("총 증설 서버 수: ", answer)
        # print("-----------------------------------")
    return answer




print("정답 = 7 / 현재 풀이 값 = ", solution([0, 2, 3, 3, 1, 2, 0, 0, 0, 0, 4, 2, 0, 6, 0, 4, 2, 13, 3, 5, 10, 0, 1, 5], 3, 5))
print("정답 = 11 / 현재 풀이 값 = ", solution([0, 0, 0, 10, 0, 12, 0, 15, 0, 1, 0, 1, 0, 0, 0, 5, 0, 0, 11, 0, 8, 0, 0, 0], 5, 1))
print("정답 = 12 / 현재 풀이 값 = ", solution([0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 5, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1], 1, 1))