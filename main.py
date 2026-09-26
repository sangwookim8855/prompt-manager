def display_menu():
    print("\n" + "=" * 40)
    print("      📝 나만의 프롬프트 관리자")
    print("=" * 40)
    print("1. 전체 프롬프트 목록 보기")
    print("2. 프롬프트 상세보기")
    print("3. 새 프롬프트 추가")
    print("4. 카테고리별 조회")
    print("5. 키워드 검색")
    print("6. 즐겨찾기 토글 (등록/해제)")
    print("7. 즐겨찾기 목록 보기")
    print("0. 프로그램 종료")
    print("=" * 40)


def main():
    while True:
        display_menu()
        choice = input("선택할 메뉴 번호를 입력하세요: ").strip()

        if choice == "0":
            print("\n프로그램을 종료합니다.")
            break
        else:
            print("\n아직 개발 중인 기능입니다.")


if __name__ == "__main__":
    main()
    