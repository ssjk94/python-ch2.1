import keyword

# 변수 이름 = 문자, 숫자, _ 로 구성 (한글 이름도 가능 : UTF-8 호환)
friend = 1
my_name = "정세윤"
myName = "정세윤"
_yourName = "둘리"
member1 = "도우넛"
가격 = 2000
print(가격-200)

# 에러여부1 : 다른 구성 변수 이름 사용 불가
# friend$ = 1
# a! = 10
# 1member = 10

# 에러여부2 : 예약어는 변수 이름으로 사용 불가 ex) def, if 등
# def = 10
# 예약어 목록
print(keyword.kwlist)
print(len(keyword.kwlist))

# 자료구조 3가지
# [] : List, {} : Dic, () : Turple
