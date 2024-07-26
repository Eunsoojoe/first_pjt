# Django

1. 프로젝트 생성
```bash
django-admin startproject {프로젝트명} .
```
-> 기존에 생성된 프로젝트 파일 내에 mange.py와 파이썬 파일 생성

2. 가상환경 생성
```bash
python -m venv venv
```

3. 가상환경 활성화
```bash
source venv/Scripts/activate
```

4. 가상환경 내부에 프로젝트를 위한 django 설치
```bash
pip install django
```

5. 서버 실행 (종료 : 'ctrl + c')
```bash
python manage.py runserver
```

6. 앱 생성
```bash
django-admin startapp {app_name}
```

*django, spring, next의 공통점 : MVC(MTV) 패턴 

7. 앱 등록
```python
INSTALLED_APPS = [
    ...
    '{app_name}'
]
```