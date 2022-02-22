html, css, js를 이용하여 기본적인 웹페이지를 만들었다. flask를 이용하여 서버에 뛰울려고 한다. 처음에는 각 그래프마다 html을 만들어 render_template을 이용하였다.

<img src="https://images.velog.io/images/tkddn2075/post/027fb228-b215-4bf3-bde5-81fbf4b82410/jinja%EC%93%B0%EA%B8%B0%EC%A0%84.PNG" width="50%" height="50%">
하지만 이렇게 하면 효율적이지 않고, 제목과 그래프만 다르고 다른 나머지 html은 같기 때문에 Jinja를 이용하기로 하였다.

Jinja란? [공식홈페이지](https://jinja.palletsprojects.com/en/2.10.x/)에는 다음처럼 작성되어 있다.
--Jinja2 is a templating engine for Python.
templating engine은 무엇인가?

--A template processor (also known as a template engine or template parser) is software designed to combine templates with a data model to produce result documents.
->templating(문서 원형)과 data model을 혼합하여, 새로운 document를 만드는 것.이라고 해석할 수 있다.

<img src="https://images.velog.io/images/tkddn2075/post/820a165d-f53e-4fe1-84ea-4502194bf343/jinja%EC%9D%B4%EB%AF%B8%EC%A7%80.PNG" width="50%" height="30%">

어떻게 쓸 것인가?

- Tableau(데이터 시각화 툴)에서 그린 그래프를 ifram태그를 이용하여 가져오는 방식을 사용하였다.
- 템플릿 상속을 이용하여 subway.html을 부모 템플릿으로 두고, 각 graph가 있는 iframe태그를 바꿔주는 형식을 사용
  <img src="https://images.velog.io/images/tkddn2075/post/f1ada555-fe15-4bf4-b9de-99d097a1e7a1/%ED%85%9D%ED%94%8C%EB%A6%BF%20%EC%83%81%EC%86%8D.PNG" width="1000%" height="30%">
  바껴야 하는 부분을 위에 처럼 감싸주고, 아래와 같이 subway.html을 상속하여 block으로 감싸면 render_template을 할 경우 jinja에 내용만 바뀌기 코드를 간략하게 바꿀 수 있었다.
  <img src="https://images.velog.io/images/tkddn2075/post/d7603175-6434-426d-982f-d1bbbac770a0/%ED%85%9C%ED%94%8C%EB%A6%BF%20%EC%83%81%EC%86%8D2.PNG" width="100%" height="30%">
