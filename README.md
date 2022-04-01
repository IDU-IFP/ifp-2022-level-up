# 💻 IFP 2022 Level Up!


- 활동 기간 : 2022.04.04(월) ~ 2022.12.31(토)

- 참여 동아리원

  - 경준현 <[hyeon0697](https://github.com/hyeon0697)>
  - 김성환 <[PotatoMeme](https://github.com/PotatoMeme)>
  - 유경덕 <[N0Rib](https://github.com/N0Rib)>
  - 이민욱 <[adasey](https://github.com/adasey)>
  - 박부현 <[PARKBUHYEON](https://github.com/PARKBUHYEON)>
  - 홍석환 <[hsh519](https://github.com/hsh519)>
  - 권성민 <[KwonSeongMin1](https://github.com/KwonSeongMin1)>
  - 김주하 <[khabh](https://github.com/khabh)>
  - 김  진 <[chamjin](https://github.com/chamjin)>

## ❓ 무엇을 하는가?

- 파이썬 51 ~ 150문
  - <[51 ~ 100문](https://www.acmicpc.net/workbook/view/460 )>
  - <[101 ~ 150문](https://www.acmicpc.net/workbook/view/461)>

- 프로그래머스 문제 풀이 
  - <[프로그래머스](https://programmers.co.kr/)>
## 🔍 어떻게 하는가?

1. 주어진 과제를 수행

2. 작성한 코드를 관련 폴더에 저장

3. 저장한 파일을 개인별 Fork한 Repo의 main로 PUSH

4. 개인별 깃허브 Repo에 PUSH된 main를 IFP의 겨울방학 스터디 저장소의 main로 PR을 보냄

5. 해당 과정을 반복

   ```
   1. IFP의 Level Up! 스터디 저장소 Fork
   2. 본인의 Level Up!스터디 저장소를 Clone (로컬의 저장소 폴더가 생성됨)
   3. IFP의 Level Up!스터디 저장소와 동기화 (변경된 내역을 나의 저장소에도 일치시켜주는 작업)
   
   # 먼저 로컬부터 동기화해줘야 한다. (Fork 하기 전의 레포. 즉, IFP 레포의 remote 이름을 "upstream"이라고 해준다.)
   # upstream 추가 -> 통상적으로 upstream이라고 해주는게 원칙이다.
   $ git remote add upstream https://github.com/IDU-IFP/ifp-2022-level-up.git
   # upstream 레포의 변경 내역을 로컬의 저장소와 병합
   $ git pull upstream main
   
   4. 관련 폴더(ex: Kyungjunhyeon) 생성
   $ mkdir Kyungjunhyeon
   
   5. Kyungjunhyeon폴더로 이동
   $ cd Kyungjunhyeon
   
   6. 풀이한 코드 업로드 (파일명 : 코드업-기초-100제-34번.py)
   
   7. 깃 Staging Area에 저장 (ex: git add 파일명)
   # 파일명에 "."을 하면 현재 폴더의 전체 파일을 tracked함.
   # 파일명에 "-a"(all의 약자)을 하면 ".git" 폴더가 위치한 루트 경로부터 전체 파일을 tracked 함.
   $ git add -a 
   
   8. ".git" 폴더에 저장 (ex: git commit -m "main(이름): 메세지") -> "-m"은 message의 약자
   $ git commit -m "main: 코드업-기초-100제-34번-풀이"
   
   9. 본인이 Fork한 깃헙 저장소에 업로드 (ex: git push <Remote> <Branch>)
   $ git push origin main
   
   10. 본인이 Fork한 깃헙 저장소로 이동하여 Pull Request(PR)를 보낸다.
    ❗ 이때, IFP 저장소의 main 브랜치로 보냄!
    이후 스터디장이 확인한 후 IFP 저장소의 메인에 병합시켜주는 작업을 하게 된다.
   ```
