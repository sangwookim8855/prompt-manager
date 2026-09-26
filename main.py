# 초기 프롬프트 데이터 (최소 3개 이상)
prompts = [
    {
        "id": 1,
        "title": "블로그 글 작성 페르소나",
        "category": "텍스트",
        "content": "당신은 IT 전문 에디터입니다. 서론-본론-결론 구조로 작성해 주세요.",
        "is_favorite": False,
    },
    {
        "id": 2,
        "title": "SF 스타일 배경 이미지 생성",
        "category": "이미지",
        "content": "Cyberpunk city street at night, neon lights, 8k resolution, photorealistic",
        "is_favorite": True,
    },
    {
        "id": 3,
        "title": "코드 리뷰어 페르소나",
        "category": "개발",
        "content": "제공된 Python 코드의 가독성과 성능 관점에서 개선점을 피드백해 주세요.",
        "is_favorite": False,
    },
]


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


def list_prompts(prompt_list=None):
    target_list = prompts if prompt_list is None else prompt_list
    if not target_list:
        print("\n등록된 프롬프트가 없습니다.")
        return

    print("\n [ 프롬프트 목록 ]")
    print("-" * 50)
    for p in target_list:
        fav_mark = "★" if p["is_favorite"] else "☆"
        print(f"[{p['id']}] {fav_mark} [{p['category']}] {p['title']}")
    print("-" * 50)


def view_prompt_detail():
    list_prompts()
    try:
        pid = int(input("\n상세 조회할 프롬프트 ID를 입력하세요: "))
        found = next((p for p in prompts if p["id"] == pid), None)
        if found:
            fav_status = "등록됨" if found["is_favorite"] else "해제됨"
            print("\n" + "=" * 50)
            print(f" ID        : {found['id']}")
            print(f" 제목      : {found['title']}")
            print(f" 카테고리  : {found['category']}")
            print(f" 즐겨찾기  : {fav_status}")
            print("-" * 50)
            print(f" 내용:\n{found['content']}")
            print("=" * 50)
        else:
            print("\n해당 ID의 프롬프트를 찾을 수 없습니다.")
    except ValueError:
        print("\n올바른 숫자를 입력해 주세요.")


def add_prompt():
    print("\n [ 새 프롬프트 추가 ]")
    title = input("제목: ").strip()
    category = input("카테고리 (예: 텍스트, 이미지, 개발): ").strip()
    content = input("프롬프트 내용: ").strip()

    if not title or not content:
        print("\n제목과 내용은 필수 입력 항목입니다.")
        return

    new_id = max([p["id"] for p in prompts], default=0) + 1
    new_prompt = {
        "id": new_id,
        "title": title,
        "category": category if category else "기타",
        "content": content,
        "is_favorite": False,
    }
    prompts.append(new_prompt)
    print(f"\n 프롬프트 #{new_id}가 새로 추가되었습니다!")


def filter_by_category():
    categories = list(set(p["category"] for p in prompts))
    print(f"\n현재 등록된 카테고리: {', '.join(categories)}")
    target_cat = input("조회할 카테고리를 입력하세요: ").strip()

    filtered = [p for p in prompts if p["category"].lower() == target_cat.lower()]
    print(f"\n [ '{target_cat}' 카테고리 결과 ]")
    list_prompts(filtered)


def search_prompts():
    keyword = input("\n검색할 키워드를 입력하세요 (제목/내용): ").strip().lower()
    if not keyword:
        print("\n검색어를 입력해 주세요.")
        return

    results = [
        p
        for p in prompts
        if keyword in p["title"].lower() or keyword in p["content"].lower()
    ]
    print(f"\n [ '{keyword}' 검색 결과 ]")
    list_prompts(results)


def toggle_favorite():
    list_prompts()
    try:
        pid = int(input("\n즐겨찾기를 토글할 프롬프트 ID를 입력하세요: "))
        found = next((p for p in prompts if p["id"] == pid), None)
        if found:
            found["is_favorite"] = not found["is_favorite"]
            status = "★ 등록" if found["is_favorite"] else "☆ 해제"
            print(f"\n'{found['title']}' 항목이 즐겨찾기에 {status}되었습니다.")
        else:
            print("\n해당 ID의 프롬프트를 찾을 수 없습니다.")
    except ValueError:
        print("\n올바른 숫자를 입력해 주세요.")


def view_favorites():
    favorites = [p for p in prompts if p["is_favorite"]]
    print("\n [ ★ 즐겨찾기 프롬프트 목록 ]")
    list_prompts(favorites)


def main():
    while True:
        display_menu()
        choice = input("선택할 메뉴 번호를 입력하세요: ").strip()

        if choice == "1":
            list_prompts()
        elif choice == "2":
            view_prompt_detail()
        elif choice == "3":
            add_prompt()
        elif choice == "4":
            filter_by_category()
        elif choice == "5":
            search_prompts()
        elif choice == "6":
            toggle_favorite()
        elif choice == "7":
            view_favorites()
        elif choice == "0":
            print("\n프로그램을 종료합니다.")
            break
        else:
            print("\n아직 개발 중인 기능입니다.")


if __name__ == "__main__":
    main()
