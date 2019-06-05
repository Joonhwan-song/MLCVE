# MLCVE

#각 컨테이너(알고리즘) 조건# -Image 만들때 양식에 맞춰야함
(1)
/cve/dataset
    /saveresult
    /newbinary    
/cve/에 각 폴더를 생성만 해둘것

/cve/dataset -> 데이터셋이나 알고리즘이 만들어진후 호스트에서 복사한 데이터셋들이 저장될 장소

/cve/saveresult -> 새 바이너리 파일이 들어온후 그 결과값을 예측한 후 그 결과값을 저장될 장소
		 ex)softmax 알고리즘에 Juliet을 학습시킬경우 파일 이름은 softmax_Juliet, 파일 내용은 softmax_Juliet 94% CWE121:Bufferoverflow
/cve/newbinary -> 검증할 바이너리 파일이 저장될 곳(NEWBINARY->숫자 데이터셋 , NEWBINARY.png ->이미지 데이터셋 들이 저장될 예정)

(2)
/save.py
/load.py

/save.py -> 각 데이터셋을 해당 컨테이너 알고리즘에 학습시키는 프로그램. 학습시킬 파일 뒤에 입력값으로 데이터셋 이름이 옴
	   ex)python3 save.py Juliet
	      python3 save.py KISA
	 -> 알고리즘을 들어온 데이터셋에 맞게 학습시키고 학습모델을 만들어서 저장 (학습모델 저장위치는 알아서, 나중에 불러올수만 있으면 됨)
             데이터셋은 /cve/dataset에 있음
	     
/load.py -> 새로 검증할 바이너리 파일이 들어왔을 경우 기존에 학습시켰던(save.py에서) 모델을 불러와 바이너리 파일의 결과값을 예측하고 그 값을 저장
	 ex)python3 save.py Juliet
         ex)python3 load.py KISA
	 ->정확도(92%)와 취약점(CWE121:Bufferoverflow)을 /cve/saveresult 폴더 안에 저장
	   ex)softmax 알고리즘에 Juliet 데이터셋일 경우 파일 이름은 softmax_Juliet, 파일 내용은 softmax_Juliet 94% CWE121:Bufferoverflow



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

