import hashlib


class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        m = hashlib.sha256()
        m.update(password.encode("utf-8"))
        self.__password = m.hexdigest()

    def display(self):
        print(f"\n이름: {self.name}\n아이디: {self.username}")

    def auth(self, password):
        m = hashlib.sha256()
        m.update(password.encode("utf-8"))
        if self.__password == m.hexdigest():
            return True
        else:
            return False


class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author


member_data = [
    {"name": "민수", "username": "ms1608", "password": "alstn0"},
    {"name": "진호", "username": "jh3370", "password": "wlsgh1"},
    {"name": "수빈", "username": "sb4511", "password": "tnqls2"},
]

post_data = [
    {
        "title": "안녕하세요!",
        "content": "게시판 여러분들 반갑습니다.",
        "author": "ms1608",
    },
    {
        "title": "라면 끓이는 법",
        "content": "라면 끓이는 법 좀 알려주세요. 배고파요.",
        "author": "ms1608",
    },
    {
        "title": "수학 질문",
        "content": "1 더하기 1은 얼마인가요?",
        "author": "ms1608",
    },
    {
        "title": "모두들 반갑습니다!",
        "content": "좋은 게시판 문화 만들어가요!",
        "author": "jh3370",
    },
    {
        "title": "운동 메이트 구함",
        "content": "매일 공원에서 달리기 하실 분 구합니다.",
        "author": "jh3370",
    },
    {
        "title": "맛집 좀 알려주세요",
        "content": "근처 맛집 이름과 메뉴추천 부탁드립니다.",
        "author": "jh3370",
    },
    {
        "title": "첫 글 써봅니다!",
        "content": "글 쓰는 건 처음인데 인사드립니다.",
        "author": "sb4511",
    },
    {
        "title": "컴퓨터가 안됩니다.",
        "content": "갑자기 컴퓨터가 부팅이 되지 않습니다. 어떻게 해야 하나요?",
        "author": "sb4511",
    },
    {
        "title": "오늘 점심 메뉴 추천",
        "content": "점심 메뉴로 뭐가 좋을지 추천 부탁드려요.",
        "author": "sb4511",
    },
]

members = [Member(**md) for md in member_data]
posts = [Post(**pd) for pd in post_data]


def create_member():
    name = input("이름: ")
    username = input("아이디: ")
    password = input("비밀번호: ")
    member = Member(name, username, password)
    members.append(member)
    print(f"가입을 환영합니다 {member.name}님!")


def show_member_name():
    for member in members:
        member.display()


def search_by_id():
    username = input("조회할 아이디 입력: ")
    print()
    flag = 0
    for post in posts:
        if post.author == username:
            flag = 1
            print(f"- {post.title}")
    if not flag:
        print("검색 결과가 없습니다.")


def search_by_keyword():
    keyword = input("조회할 단어 입력: ")
    print()
    flag = 0
    for post in posts:
        if keyword in post.content:
            flag = 1
            print(f"- {post.title}")
    if not flag:
        print("검색 결과가 없습니다.")


def create_post():
    print("인증이 필요한 메뉴입니다.\n")
    username = input("아이디: ")
    count = 0
    for member in members:
        if member.username == username:
            while count < 5:
                count += 1
                password = input("패스워드: ")
                if member.auth(password):
                    break
                print("잘못된 비밀번호입니다. 다시 입력해주세요.\n")
            if count >= 5:
                print("비밀번호를 5회 이상 틀렸습니다.")
                return
            break
    else:
        print("존재하지 않는 아이디입니다.")
        return
    print("\n인증되었습니다! 게시글 작성이 가능합니다.\n")
    title = input("제목: ")
    content = input("내용: ")
    posts.append(Post(title, content, username))
    print("작성이 완료되었습니다!")


def main():
    menu_name = [
        "회원가입",
        "회원목록 조회",
        "아이디로 게시글 조회",
        "키워드로 게시글 조회",
        "게시글 작성",
    ]
    menu = [
        create_member,
        show_member_name,
        search_by_id,
        search_by_keyword,
        create_post,
    ]
    print("\n게시판에 오신 것을 환영합니다!")
    while True:
        print("\n원하는 메뉴를 선택하세요!\n")
        for i in range(len(menu_name)):
            print(f"{i+1}. {menu_name[i]}")
        n = int(input("\n메뉴번호: ")) - 1
        print()
        if n > len(menu):
            print("잘못된 번호가 입력되었습니다.")
            continue
        menu[n]()
        if input("\n처음 화면으로 돌아가기 (Y/n): ") == "n":
            print("\n이용해 주셔서 감사합니다.!")
            break


main()
