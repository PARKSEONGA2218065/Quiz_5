def validate_resident_registration_number(rrn):
    # 주민등록번호의 길이가 13이 아니면 유효성 검사 실패
    if len(rrn) != 13:
        return False

    # 주민등록번호의 첫 자리부터 마지막 자리 전까지 2,3,4,5,6,7,8,9,2,3,4,5를 곱하고 더한다.
    weighted_sum = sum(int(rrn[i]) * (i % 10 + 2) for i in range(12))

    # 더한 결과를 11로 나눈 나머지 값을 구하고 11에서 나머지 값을 뺀다.
    remainder = (11 - (weighted_sum % 11)) % 10

    # 계산된 결과와 주민등록번호의 마지막 자리 숫자를 비교하여 유효성을 확인한다.
    return remainder == int(rrn[-1])

# 주민등록번호 입력 받기
rrn = input("주민등록번호를 입력하세요 (예: 123456-1234567): ")

# '-' 문자를 제거하고 유효성 검사 수행
rrn = rrn.replace('-', '')
if validate_resident_registration_number(rrn):
    print("유효한 주민등록번호입니다.")
else:
    print("유효하지 않은 주민등록번호입니다.")
