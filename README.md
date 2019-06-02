# MLCVE

saveFilePath = 컨테이너 안 결과값이 저장된 문서가 저장된 디렉토리의 위치

saveHostPath = 호스트 에 결과값을 저장할 디렉토리의 위치

datasetpath = 호스트에 데이터셋들이 저장된 디렉토리의 위치

컨테이너 안 머신러닝 학습 실행 파일 이름 = run.py (추후에 수정 가능)

취약점 9가지 분류: cwe 78 120(121) 126 134 190 327 377 676 785 
데이터셋규격 : 데이터셋경로에 폴더별로 구분 (ex: cwe78, cwe120 ...)

flawfinder.py : flawfinder라는 소스코드 취약점 분석도구로 소스파일에서 데이터 추출
              데이터셋절대경로/cnt/에 폴더별로 텍스트 파일로저장
	사용법 : python flawfinder.py 데이터셋절대경로
	ex: python flawfinder.py /home/jihyeon/Desktop/MLCVE/Juliet/C/testcases/

countconvert.py : 추출한 데이터를 이미지로 바꾸는 파일
	데이터셋절대경로/cnt/png 에 폴더별로 이미지 파일로 저장
	사용법: python countconvert.py 데이터셋절대경로/cnt/
	ex: python countconvert.py /home/jihyeon/Desktop/MLCVE/Juliet/C/testcases/cnt/

