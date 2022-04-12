vscode 기준 python venv 가상환경을 통한 개별 인터프리터 - 가상 개발 환경으로 프로젝트별 라이브러리 사용하기
라이브러리나 사용은 아나콘다를 통한 pycharm이 더 나을지 몰라도 실행만큼은 vscode가 더 편했다..

파이썬 프로젝트를 위한 공간을 만드면 하단의 terminal에 

python -m venv 가상환경명

ex) python -m venv pythonProj

을 사용하면 python 인터프리터가 설치된 공간이 만들어진다.

이때 F1 키를 눌러 python:select interpreter 를 눌러 현재 디렉토리의 가상환경명 디렉토리로 들어가면
안에 python.exe가 있다.

해당 파일을 선택해 ctrl + shift + ` 을 누르면 새 터미널이 열리는데

(가상환경명) ps 디렉토리경로~> 

이 화면이 나오면서 작동한다. 해당 터미널에서 라이브러리도 깔고 이것저것 설치하면 된다.