# 💻 IFP 2022 Level Up!

- 활동 기간 : 2022.04.04(월) ~ 2022.12.31(토)

- 동아리 회장 

  - 이하람 <[HalamLee](https://github.com/HalamLee)>

- 참여 동아리원
  - 경준현 <[hyeon0697](https://github.com/hyeon0697)>
  - 김성환<[PotatoMeme](https://github.com/PotatoMeme)>
  - 유경덕 <[N0Rib](https://github.com/N0Rib)>
  - 이민욱 <[adasey](https://github.com/adasey)>
  - 박부현<[PARKBUHYEON](https://github.com/PARKBUHYEON)>
  - 홍석환<[hsh519](https://github.com/hsh519)>
  - 권성민<[KwonSeongMin1](https://github.com/KwonSeongMin1)>
  - 김주하<[khabh](https://github.com/khabh)>
  - 김진<[chamjin](https://github.com/chamjin)>

## ❓ 무엇을 하는가?

- 파이썬 51 ~ 150문
  - <[51 ~ 100문](https://www.acmicpc.net/workbook/view/460 )>
  - <[101 ~ 150문](https://www.acmicpc.net/workbook/view/461)>

- 프로그래머스 문제 풀이 
  - <[프로그래머스](https://programmers.co.kr/)>
## 🔍 어떻게 하는가?

1. 주어진 과제를 수행

2. 작성한 코드를 관련 폴더에 저장

3. 저장한 파일을 개인별 Fork한 Repo의 main으로 PUSH

4. 개인별 깃허브 Repo에 PUSH된 main 브랜치를 IFP의 스터디 저장소의 main 브랜치로 PR을 보냄

5. 해당 과정을 반복

   ```
   1. IFP의 Level Up! 스터디 저장소 Fork
   2. 본인의 Level Up!스터디 저장소를 Clone (로컬의 저장소 폴더가 생성됨)
   $ git clone https://github.com/[자신의 계정이름]/ifp-2022-level-up.git
   3. IFP의 Level Up!스터디 저장소와 동기화 (변경된 내역을 나의 저장소에도 일치시켜주는 작업)
   
   # 먼저 로컬부터 동기화해줘야 한다. (Fork 하기 전의 레포. 즉, IFP 레포의 remote 이름을 "upstream"이라고 해준다.)
   # upstream 추가 -> 통상적으로 upstream이라고 해주는게 원칙이다.
   $ git remote add upstream https://github.com/IDU-IFP/ifp-2022-level-up.git
   # upstream 레포의 변경 내역을 로컬의 저장소와 병합
   $ git pull upstream main
   
   4. 자신의 영문 이름으로 된 폴더(ex: Kyungjunhyeon) 생성 
  
   5. Kyungjunhyeon폴더로 이동
   6. 코드작업을 시작하기 전에 원본 레포지토리로부터 pull을 받고 진행하면 된다.   
   # pull을 이용하여 원본 레포지토리의 main 브랜치에 있는 최신 파일들을 받아온다.
   $ git pull upstream main
   7. 코드작업 진행 (파일명 : 백준_0000번문제.py)
   
   7.5 코드 작업이 끝나고 다시 pull을 받아온다.
   # 코드 작업중 누군가가 새로운 파일을 push할 가능성이 있으므로 다시 최신화 시켜준다.
   $ git pull upstream main
   
   8. 깃 Staging Area에 저장 (ex: git add 파일명)
   # 파일명에 "."을 하면 현재 폴더의 전체 파일을 tracked함.
   $ git add . 
   
   9. ".git" 폴더에 저장 (ex: git commit -m "이름: 메세지") -> "-m"은 message의 약자
   $ git commit -m "Kyungjunhyeon : 백준_0000번문제 풀이"
   
   10. 본인이 Fork한 깃헙 저장소에 업로드 (ex: git push <Remote> <Branch>)
   $ git push origin 자신의 영문이름 폴더(ex: Kyungjunhyeon)
   
   11. 본인이 Fork한 깃헙 저장소로 이동하여 Pull Request(PR)를 보낸다.
    ❗ 이때, IFP 저장소의 main 브랜치가 아닌 "복사한 레포지토리"로 보내야함
    이후 스터디 그룹장이 확인한 후 IFP 저장소의 main 브랜치로 병합시켜주는 작업을 하게 된다.
   
   12. 다른 스터디원의 문제 풀이가 올라온 경우 다음 주차가 넘어가지 전까지 코드리뷰를 해준다.
   ```
### ❗주의해야할 점
- **git pull**을 이용하여 코드작업 전, 후로 **최신화** 시켜주기
- **git pull**을 이용하면 **다른 사람의 폴더가 자신의 작업 환경에 생기는데** 이때 다른 사람의 폴더를 **절대로 삭제**하지 않습니다!!
- **pull**을 사용할 때에는 **원본 레포지토리**를 이용한다.
- **push**을 할 때에는 **fork한 개인 레포지토리**를 이용한다.
