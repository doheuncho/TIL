그래프를 보여주는 웹페이지를 처음부터 어떻게 만들지 고민이였다.
웹페이지 기본 틀인 html, 디자인 요소인 css, 동적인 기능이 들어간 javascript. 처음부터 공간을 나누는 것부터가 문제였다. div태그끼리 나누었지만, 생각보다 어려웠고 생각대로 구역이 나눠지지 않아 헤맸다. 그러다가 부트스트랩을 알게 되었다.

부트스트랩은 웹사이트를 쉽게 만들 수 있게 도와주는 **HTML, CSS, JS 프레임워크**이다. 하나의 css로 휴대폰, 테블릿, 데스크탑 등 다양한 기기에서 작동하는 반응형 웹을 만들 수 있다.

우리는 [startbootstrap](https://startbootstrap.com/)에서 [https://startbootstrap.com/template/sb-admin](https://startbootstrap.com/template/sb-admin)을 가져와 커스터마이징하였다. 안쓰는 것을 삭제하는 과정에서 부트스트랩에 단점을 알 수 있었는데, 그것은 우리가 애초에 설정하지 않은 class명이기에 어떤 것을 삭제해야하고, css를 삭제하고 그것을 따로 설정하는 과정에서 어려움을 겪었다.
사용하는 html에 class 또는 id 명과 css에 있는 class 또는 id을 대조하여, 사용하지 않는 것을 삭제하였고, javascript를 이용하여 동적인 기능을 넣기 위해서도 html, css의 구조를 알아야 했다.

정리를 하자면, 부트스트랩 장점과 단점은 아래와 같다.
**장점**

- 내부 클래스들만 알고 있다면 빠르고 쉽게 여러형태의 웹 페이지를 제작할 수 있다.
- 각 해상도 대응에 대한 처리가 되어있기 때문에 반응형 처리가 어렵지 않다.

**단점**

- 미리 짜여진 스타일이 많기 때문에 정형화된 디자인과 기능이 많다. 뜯어고칠게 많은 경우에 오히려 더 많은 시간을 작업하게 된다
- 구성요소는 타 프레임워크와 비교해도 별 차이가 없지만, 페이지 로딩 속도를 비교해보면 다른 프레임워크에 비해 굉장히 무겁다
- 미리 정의된 클래스들을 하나하나 다 분석하고 있어야 하며, 각 해상도에 어떻게 반응하는지 파악하고 있어야 한다.

그래도 부트스트랩 덕분에 처음부터 웹페이지를 제작할 시간을 아끼고, 다른 곳에 집중할 수 있어서 프론트엔드가 주요 프로젝트가 아니라면 부트스트랩을 쓰는것을 추천한다.
