/**
 * 1. 연산자를 찾아서 수를 구분
 *      "11+23-32" -> 11, 23, 32 (배열에 저장)
 * 2. 연산자도 다른 배열에 저장
 * 3. 순서대로 연산하기
*/

function calculate(input){
    const numberArr = [];

    const operatorArr = [];

    let number = 0;
    let number2 = 0;
    let count = 0;
    for(let i = 0; i < input.length; i++){
        const char = input[i]
        if(char === '+' || char === '-' || char === "*" || char === "/"){
            operatorArr.push(char);

            numberArr.push(number);
            number = 0;
            
        }

        else if(char === '.'){
            for(let a = i+1; a < input.length; a++){
                i++;
                const afterPoint = input[a];
                if(afterPoint === '0'){
                    count += 1;
                    number2 = 0;
                    number = number + number2 * (0.1 ** count);
                }
                else if(afterPoint === '1'){
                    count += 1;
                    number2 = 1;
                    number = number + number2 * (0.1 ** count); 
                }
                else if(afterPoint === '2'){
                    count += 1;
                    number2 = 2;
                    number = number + number2 * (0.1 ** count); 
                }
                else if(afterPoint === '3'){
                    count += 1;
                    number2 = 3;
                    number = number + number2 * (0.1 ** count); 
                }
                else if(afterPoint === '4'){
                    count += 1;
                    number2 = 4;
                    number = number + number2 * (0.1 ** count); 
                }
                else if(afterPoint === '5'){
                    count += 1;
                    number2 = 5;
                    number = number + number2 * (0.1 ** count); 
                }
                else if(afterPoint === '6'){
                    count += 1;
                    number2 = 6;
                    number = number + number2 * (0.1 ** count); 
                }
                else if(afterPoint === '7'){
                    count += 1;
                    number2 = 7;
                    number = number + number2 * (0.1 ** count); 
                }
                else if(afterPoint === '8'){
                    count += 1;
                    number2 = 8;
                    number = number + number2 * (0.1 ** count); 
                }
                else if(afterPoint === '9'){
                    count += 1;
                    number2 = 9;
                    number = number + number2 * (0.1 ** count); 
                }

                else if(afterPoint === '+' || afterPoint === '-' || afterPoint === '*' || afterPoint === '/'){
                    count = 0;
                    number2 = 0;
                    i = i - 1;
                    break;
                }
            }
        
        }


        else{
            if(number === 0){
                number = charToNum(char);
            }
            else{
                number = number * 10 + charToNum(char);
            }
        }
    }
    numberArr.push(number);


    number = numberArr[0]
    for(let i = 0; i < operatorArr.length; i++){
        const operator = operatorArr[i]
        if(operator === '+'){
            number = number + numberArr[i+1]
        }
        else if(operator === '-'){
            number = number - numberArr[i+1]
        }
        else if(operator === '*'){
            number = number * numberArr[i+1]
        }
        else if(operator === '/'){
            number = Math.floor(number / numberArr[i+1])
        }
    };

    return number;

}


function charToNum(char){
    if(char === '0'){
        return 0;
    }
    else if(char === '1'){
        return 1;
    }
    else if(char === '2'){
        return 2;
    }
    else if(char === '3'){
        return 3;
    }
    else if(char === '4'){
        return 4;
    }
    else if(char === '5'){
        return 5;
    }
    else if(char === '6'){
        return 6;
    }
    else if(char === '7'){
        return 7;
    }
    else if(char === '8'){
        return 8;
    }
    else if(char === '9'){
        return 9;
    }
}