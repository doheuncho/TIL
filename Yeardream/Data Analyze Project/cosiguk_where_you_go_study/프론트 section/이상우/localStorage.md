이전에 sidetab.js 기능을 통해 sidetab을 클릭시, class에 actvie를 추가하여 active가 있는 경우 css의 vsibility를 이용하여 visible or hidden으로 해당하는 그래프를 보여주는 것을 하였다. 하지만 새로고침 시 1번그래프로 되돌아가는 문제를 발견하게 되었다. 아마도 새로고침시 subway.html 처음상태로 돌아가는 문제 때문이것 같다. 이것을 해결하기 위해선 웹 스토리지중 하나인 localStorage를 이용하면 된다고 구글링에 나왔다.

### 웹 스토리지란?

- 웹 스토리지는 사용자의 브라우저에 저장되는 데이터이다.
- 로컬 스토리지 -> 브라우저 창이 닫힌 후에도 유지되는 만료 날짜가 없는 데이터이다.
- 세션 스토리지 -> 브라우저 창이 닫힌 후 지워지는 데이터이다.
- 이 기능은 사용자 기본 설정(웹 사이트의 밝은 색 또는 어두운 색 테마), 장바구니 담기 또는 웹 사이트에 로그인한 사용자 기억과 같은 데이터를 저장할 때 유용하다.
- 이전에는 이러한 유형의 임시 데이터를 기억하기 위한 유일한 선택이 쿠키다.
- 다음 localStorage메서드에 대한 개요이다.
  | Method | Description |
  | setItem() | 로컬 스토리지에 키, 값을 추가한다. |
  | getItem() | 키에 맞는 값을 찾는다. |
  | removeItem() | 키에 맞는 값을 삭제한다. |
  | clear() | 로컬 스토리지에 저장된 모든 내용을 삭제한다. |

이렇게 나와있지만, 우리같은 경우에는 어떻게 사용해야할지 아무리 찾아봐도 감이 안잡혀 stackoverflow에 질문을 올렸고, 해당하는 페이지와 같이 해답을 얻게 되었다.
[스텍오버플로우 질문](https://stackoverflow.com/questions/70089972/how-do-i-keep-the-active-tab-after-page-refresh-with-localstorage)

<img src="https://images.velog.io/images/tkddn2075/post/22c1e04d-e5d9-4dea-be7e-3f16b45e074b/local.PNG" width="100%" height="30%">
