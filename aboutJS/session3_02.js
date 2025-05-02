/**
 * 재료: 원두, 물
 * 원두 15g쓰고 물 180ml 써서 커피를 만들 수 있음
 * 재료가 부족하면 못만듦
 * 원두와 물을 보충을 할 수 있음 
 */

// 커피 머신을 만드는 함수
function makeCoffeemachine(){
    return {
        coffeeBeans : 50,
        water : 1000,
        makeCoffee : function(){
            if(this.coffeeBeans < 15 || this.water < 180){
                return false;
            }

            this.coffeeBeans -= 15;
            this.water -= 180;

            return true;
        },
        addBeans(amount){
            this.coffeeBeans += amount;
        },
        addWater(amount){
            this.water += amount;
        }
    };
}




// 사람 만드는 함수
function makeHuman(name, age){
    return {
        name : name,
        age : age,
        introduce : function(){
            console.log('제 이름은', this.name, '이고', '나이는', this.age, '입니다.')
        }
    }
}

// makeHuman을 이용해서 남자를 만드는 함수
function makeMan(name, age){
    const human = makeHuman(name, age);
    human.gender = 'male';
    return human;
}

const human1 = makeHuman('철수', 20);
const human2 = makeMan('민수', 21);