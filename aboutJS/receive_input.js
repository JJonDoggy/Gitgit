// 1. alert : 메세지를 보여준다
alert('환영합니다 ' + '현석님.')

// 2. prompt : 사용자에게 메세지를 보여주고 입력받음 
let name = promt('이름을 입력해주세요') // 걍 파이썬 input이랑 똑같다.
// 얘도 문자열로 입력받아서 Number() 을 통해 숫자로 변환시킬 수 있다.

// 3. confirm : 사용자에게 확인/취소 값 받음
const isAdult = confirm('당신은 어른입니까?')
console.log(isAdult); // 이러면 사용자는 메세지를 보고 확인/취소로 대답한다.





















let sleepy = prompt('잠와 안잠와로 대답해')

let 너의상태 = {
    수면상태 : sleepy,
    태고 : 'want'
}


function 잠오는데(a){
    a.수면상태 = '잠와'
    console.log('넌 이제 잠이온다 상태를 확인해봐')
}

잠오는데(너의상태)

// ㅅㅂ 왜 안돼

