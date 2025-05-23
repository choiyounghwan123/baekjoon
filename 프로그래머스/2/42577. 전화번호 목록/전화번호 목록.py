# [프로그래머스] 전화번호 목록

def solution(phone_book):
    hash_map = dict()
    for number in phone_book:
        hash_map[number] = 1
    
    for number in phone_book:
        arr = ""
        for n in number:
            arr += n
            
            if arr in hash_map and arr != number:
                return False
    return True



print(solution(["119", "97674223", "1195524421"]))