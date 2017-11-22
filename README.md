# google drive 연동

구글 드라이브 연동

## 시크릿 키 생성

[시크릿 키 생성하러 가기](https://console.developers.google.com/flows/enableapi?apiid=drive)

여기서 생성한 시크릿 키는 `./config/google/google_drive_secret_key.json`으로 생성해줍니다.

[설명 보러가기](http://blog.naver.com/pjt3591oo/221145739394)

## 실행

```bash

$ python app.py

```

만약 `./config/google/download`와 `./config/google/upload`가 비어있다면 인증 페이지가 나타납니다.

인증 페이지는 `./config/google/download/drive-python-download.json` `./config/google/upload/drive-python-upload.json`가 존재하지 않을때만 나타납니다.