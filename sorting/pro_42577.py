# 전화번호 목록

# 정렬 사용 풀이
def solution1(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False

    return answer


# 해시 사용 풀이
def solution2(phone_book):
    answer = True
    dic = {}
    for phone in phone_book:
        dic[phone] = 1

    for phone in phone_book:
        s = ""
        for number in phone:
            s += number
            if s != phone and s in dic:
                return False
    return answer


phone_book_list = [
    ["119", "97674223", "1195524421"],
    ["123","456","789"],
    ["12","123","1235","567","88"]
]
for data in phone_book_list:
    print(solution2(data))
