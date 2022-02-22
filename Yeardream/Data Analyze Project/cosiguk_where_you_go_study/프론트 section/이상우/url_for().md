기존의 만들었던 html, css, js을 만들었다.
이것을 flask서버 위에 띄워서 통신이 되게 하는게 목적이다.

> 우선 flask에서 제공하는 **@app.route()**인 데코레이터를 사용해야 한다.

**@app.route('/') -> http://localhost:5000/** 을 의미
flask에서는 기본적으로 5000번 포트를 사용하기 때문이다.

**@app.route('hello') -> http://localhost:5000/hello** 를 의미

이렇게 데코레이터가 가리키는 주소에 접근했을 경우, 해당하는 함수를 실행하는 것이 기본적인 동작 구조이다.

![](https://images.velog.io/images/tkddn2075/post/7ccd68e2-c481-4834-b4c0-347123d4ccf9/%EA%B8%B0%EB%B3%B8%EA%B5%AC%EC%A1%B0.PNG)
위의 사진처럼 5000번포트에서는 home.html을 불러오고, first를 추가하게 되면, main.html을 불러오는 함수를 실행한다. render_template은 해당하는 html을 불러오는 것이다. 대신 render_template를 쓰려면** html파일을 templates폴더 내에 넣어야한다.** 아래 이미지와 같이.

![](https://images.velog.io/images/tkddn2075/post/0b7f366a-1350-4c14-a228-6a68f41d57b8/%EB%94%94%EB%A0%89%ED%86%A0%EB%A6%AC%20%EA%B5%AC%EC%A1%B0.PNG)

flask를 쓰기전에는 html에서 html로, html에서 css를 적용하는 것도, js를 적용하는것도 해당하는 파일을 절대경로 또는 상대경로를 넣으면 됬었지만, flask에서는 제대로 동작하지않았다. 이것을 해결하는 방법이 **url_for()**이다.

> **url_for()함수**는 함수 이름으로 된 **종단점(endpoint)의 URL을 생성**하는 것이다.

![](https://images.velog.io/images/tkddn2075/post/8c152c9d-ab5d-4112-a390-0ccda3a67326/htmlflask.PNG)
이 코드를 설명하자면 a태그를 눌렀을 시 html 포트에 first를 추가하는 것이다. 즉 기본 포트에서 first가 추가된@app.route('first')데코레이터에 해당하는 함수를 실행하게 되는 것이다.

그러면 기존에 적용했던 css 나 js는 어떻게 적용해야할까?
우선 static폴더 아래에 css, js를 넣어야 한다. 왜냐하면 기본적으로 url_for()을 css, js에 쓰려면 html을 flask에서 불러오기 위해서 templates폴더아래에 두는거와 같다고 생각하면 된다.
![](https://images.velog.io/images/tkddn2075/post/c1107513-7b62-4796-8f71-0dcef026af8d/static.PNG)

> **css 입히는 방법**![](https://images.velog.io/images/tkddn2075/post/a083f28f-3b7d-454d-af9e-c4296abcb927/cssflask.PNG)

> **javascript입히는 방법**![](https://images.velog.io/images/tkddn2075/post/c1fd8c27-116e-424e-90d0-7ea3f5e815c6/jsflask.PNG)

그럼 static말고 다른 폴더에 넣어서 설정을 바꾼다면?
적용되지않는다. 왜냐하면 기본 flask기본설정이 static으로 되어있기 때문이다. 만약에 바꾸고싶다면 flask 즉, app.py에서
app = FLASK(**name**, static_folder='./static') 여기 설정을 바꿔야 한다. 그러면 가능할 것이다.

> 결론을 짓자면, flask에서 웹페이지를 뛰우기 위해서는 절대경로, 상대경로로 설정되어있는 것들을 모두 url_for()로 바꿔야한다는 것이다.
> sssss
