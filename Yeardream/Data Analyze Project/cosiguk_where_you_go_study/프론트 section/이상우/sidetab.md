iframe 태그를 이용하여 Tableau에서 그린 그래프를 웹페이지로 불러오게 하였지만, 각 페이지마다 그래프를 render_template을 할때마다 로딩이 되는 문제를 겪게 되었다.
이 문제를 해결하기 할 것인지 고민을 하였고, 한페이지에 로딩을 다 시킨후, 메뉴에 해당하는 그래프를 보여주고 나머지 그래프는 보여주지않는 방법을 쓰면 좀 더 빠르게 보여줄 수 있지 않을까?라는 아이디어를 생각해냈다.

원래는 기본적으로 a태그의 href에 url_for을 이용하여 해당하는 그래프 html을 렌더링하는 방식을 사용하였다.

생각한 방식

- subway.html에 모든 그래프를 담아둔다.
- javascript을 이용하여 메뉴를 탭할 경우 클래스(active)를 추가, 기존에 있던 active클래스를 삭제
  <img src="https://images.velog.io/images/tkddn2075/post/19b894fd-020b-4961-ac2a-96337327857b/%EC%82%AC%EC%9D%B4%EB%93%9C%ED%83%ADjs.PNG" width="1000%" height="30%">
- 첫 그래프의 클래스에는 active를 미리 추가해놓고, 첫화면이 보이게 한다.
  <img src="https://images.velog.io/images/tkddn2075/post/0fdbd825-4b4a-484a-ae65-dbacecf125e4/html%EA%B7%B8%EB%9E%98%ED%94%84.PNG" width="1000%" height="30%">
- css에 active클래스가 있을 경우 visibility를 이용하여 visible을 설정하고 없을 경우는 hidden을 통해 안보이게 설정
  <img src="https://images.velog.io/images/tkddn2075/post/1b0b9153-c420-441d-b54f-912a393038ba/css%EC%82%AC%EC%9D%B4%EB%93%9C%ED%83%AD.PNG" width="1000%" height="30%">
