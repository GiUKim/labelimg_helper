# labelimg_helper
labeling 툴 labelimg에서 작업 시 속도 증가를 위한 레이블링 보조 자동화
---
  - pip install pyautogui
  - pip install keyboard
---
## Usage
0. python labeledit.py (실행만 해놓으면 됨)
1. bbox 그리고 bbox 선택 또는 이미 그려진 bbox 선택
2. f1 ~ f? 키 입력 -> 특정 클래스 레이블로 자동 변환
3. f 입력 -> 최대치 줌 인, g 입력 -> 최대치 줌 아웃 (현재 커서가 있는 곳 기준으로)
4. f10 키 입력 -> py 파일 실행 종료

모든 단축키와 클래스 명시는 코드에서 수정 가능
