// "a+b" 라는 문자열 -> a + b 계산해서 반환 하는 함수
// 연산에 사용할 수는 2개이고 모두 0 이상의 정수
// 연산자는 +, -, *, / 만 사용함
// input 예시) "13-11"

function calculate(input){
    let operatorIndex;
    for(let i = 0; i < input.length; i++){
        if(input[i] === "+" | input[i] === "-" | input[i] === "*" | input[i] === "/"){
            operatorIndex = i; // operatorIndex에 연산자 위치 저장
            break;  // 반복문 끝내기
        }
    }

    let number1 = 0;
    let number2 = 0;

    // number1 알아내기
    for(let i = 0; i < operatorIndex; i++){
        let number;
        if(input[i] === "0"){
            number = 0;
        }
        else if(input[i] === "1"){
            number = 1;
        }
        else if(input[i] === "2"){
            number = 2;
        }
        else if(input[i] === "3"){
            number = 3;
        }
        else if(input[i] === "4"){
            number = 4;
        }
        else if(input[i] === "5"){
            number = 5;
        }
        else if(input[i] === "6"){
            number = 6;
        }
        else if(input[i] === "7"){
            number = 7;
        }
        else if(input[i] === "8"){
            number = 8;
        }
        else if(input[i] === "9"){
            number = 9;
        }

        if(number1 === 0){
            number1 = number1 + number;
        }
        else{
            number1 = number1 * 10 + number;
        }
    }




    for(let i = operatorIndex + 1; i < input.length; i++){
        let number;
        if(input[i] === "0"){
            number = 0;
        }
        else if(input[i] === "1"){
            number = 1;
        }
        else if(input[i] === "2"){
            number = 2;
        }
        else if(input[i] === "3"){
            number = 3;
        }
        else if(input[i] === "4"){
            number = 4;
        }
        else if(input[i] === "5"){
            number = 5;
        }
        else if(input[i] === "6"){
            number = 6;
        }
        else if(input[i] === "7"){
            number = 7;
        }
        else if(input[i] === "8"){
            number = 8;
        }
        else if(input[i] === "9"){
            number = 9;
        }

        if(number2 === 0){
            number2 = number2 + number;
        }
        else{
            number2 = number2 * 10 + number;
        }
    }

    let operator = input[operatorIndex];  // 연산자 글자 가져오기기
    if(operator === "+"){
        return number1 + number2;
    }
    else if(operator === "-"){
        return number1 - number2;
    }
    else if(operator === "*"){
        return number1 * number2;
    }
    else if(operator === "/"){
        return Math.floor(number1 / number2);  // 소수점 버리기
    }
}
