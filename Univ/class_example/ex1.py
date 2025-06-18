
class Book:
    def __init__(self, title, author, isbn, booked=False):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.booked = booked

    def display_info(self): # 책 정보 출력
        print(f'제목 : {self.title}, 저자 : {self.author}, ISBN : {self.isbn}, 대출여부 : {self.booked}')
        pass

    def booking(self): # 대출 메소드
        self.booked = True
        pass

    def returning(self): # 반납 메소드
        self.booked = False
        pass

    def __str__(self):
        return str({'제목': self.title, '저자': self.author, 'ISBN': self.isbn, '대출 여부': self.booked})

class Member:
    def __init__(self, name, memberNum, bookList=[]):
        self.name = name
        self.memberNum = memberNum
        self.bookList = bookList

    def display_info(self): # 맴버 정보 출력
        print(f'회원 이름 : {self.name}, 회원 번호 : {self.memberNum}')
        print(f'대출중인 책 목록 : {self.bookList}')

    def booking(self, book): # 도서 대출
        if book.booked == False:
            book.booking()
            self.bookList.append(book.title)
        else:
            print(f'대출 불가능한 책입니다.')

    def returning(self, book): # 도서 반납
        if book.title in self.bookList: # 책제목이 책 목록에 있으면 반납 가능
            book.returning()
            self.bookList.remove(book.title)

    def __str__(self):
        return str({'name': self.name, 'id': self.memberNum, '빌린 책 목록': self.bookList})


class Library:
    def __init__(self, name, booklist=[], memberlist=[]):
        self.name = name
        self.booklist = booklist
        self.memberlist = memberlist
        self.mem_id_seq = 1001

    def display_info(self): # 맴버 정보 출력
        print(f'도서관 이름 : {self.name}')
        print(f'보유 책 목록 : {list(map(str, self.booklist))}')
        print(f'회원 목록 : {list(map(str, self.memberlist))}')

    def add_book(self, title, author, isbn):
        b = Book(title, author, isbn)
        self.booklist.append(b)
        print(f'{b.title} 도서가 추가됨')

    def remove_book(self, title):
        for idx, b in enumerate(self.booklist):
            if b.title == title:
                self.booklist.pop(idx)
                print(f'{b.title} 도서가 제거됨')


    def add_member(self, name):
        m = Member(name, self.mem_id_seq)
        self.memberlist.append(m)
        self.mem_id_seq += 1

        print(f'{m.name}이 추가됨')

    def remove_member(self, name):
        for idx, m in self.memberlist:
            if name == m.name:
                self.memberlist.pop(idx)
                print(f'멤버 {m.name}이 제거됨')


# 도서관에서 멤버랑 책을 주면 빌리게 해주는거 만들어보기