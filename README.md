# 디장고(django) 가상환경 셋팅

<pre>
<code>
python -m venv 가상환경이름
</code>
</pre>
- 가상환경 만들기

<pre>
<code>
가상환경이름/Scripts/activate
</code>
</pre>
- 가상환경 실행

<pre>
<code>
deactivate
</code>
</pre>
- 가상환경 끄기

<pre>
<code>
django-admin startproject project 이름
</code>
</pre>
- Project 만들기

<pre>
<code>
python manage.py runserver
</code>
</pre>
- 서버 실행 시키기 주소는 http://127.0.1:8000/ 

<pre>
<code>
python manage.py startapp 앱 이름
</code>
</pre>
- 프로젝트의 구성 단위인 앱 만들기
</br>

# Django DB
model이란 django가 데이터베이스를 관리하게 해주고 admin은 model을 관리하는 역할

#### models.py
<pre>
<code>
class Mail(models.Model):                        #models.Model 장고 모델임을 나타냄
    title = models.CharField(max_length=20)      # 길이 제한이 있는 문자열
    contents = models.TextField()                # 길이 제한이 없는 문자열
</code>
</pre>
- 처리할 데이터의 종류를 class를 활용하여 등록. 각 내용은 class의 인스턴스


## python manage.py makemigrations
django와 데이터베이스가 소통할 수 있도록 마이그레이션을 생성
## python manage.py migrate
마이그레이션을 적용
#### - 모델 변경 시 위의 두 과정을 실행
</br>

## 쿼리셋(QuerySet)
 데이터베이스에서 전달 받은 객체의 목록. 데이터베이스로부터 데이터를 읽고, 정렬 등 다루는 작업을 수행

