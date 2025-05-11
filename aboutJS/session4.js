// class 에 대해 알아보자···

class Human{                    // class 기본 문법법
    constructor(name, age){
        this.name = name;
        this.age = age;
    }
}

const 철수 = new Human(철수, 15);

class sword{
    // 속성 선언하는 거 (프롬프트)
    name;
    maker;
    material;
    grade = 0;
    baseDamage = 1;

    constructor(name, maker){
        this.name = name;
        this.maker = maker;

    }

    upgrade(){
        this.grade += 2
    }

    get damage(){
        return this.baseDamage * (this.grade + 1);
    }
}

/**
 * material이 'iron'
 * baseDamage가 5;
 * 
 */

class IronSword extends sword{
    material = 'iron';
    baseDamage = 5;
}

/*
고래치가 만든 철검
maker 고래치
grade가 기본값 1
*/
class GoraechiIronSword extends IronSword{
    grade = 1;
    attribute;

    constructor(name, attribute){
        super(name, '고래치'); // Sword의 constructor
        this.attribute = attribute;
    }

    /**
     * grade가 5미만 -> 강화 2번
     * 5이상 -> 강화 1번(원래)
     */

    upgrade(){
        if(this.grade < 5){
            super.upgrade();
            super.upgrade();
        }
        else{
            super.upgrade();
        }
    }
}

const 검1 = new GoraechiIronSword('고래치가 만든 잡검', 'fire')

/*
클래스가 어떻게 작동하나
1. new 키워드로 클래스 호출
2. 객체가 만들어짐
3. 클래스의 constructor 함수 실행

프로토타입
어떤 객체 A, A의 프로토타입이 어떤 객체 B
A의 속성 'x'를 불러옴 A.x
A에 'x'속성이 없네? -> B에 'x'속성이 있는지 확인
있으면 B.x를 사용

upgrade = function(){} 이런식으로 쓰면
객체 자체에 upgrade라는 속성이 생김

upgrade(){} 이런식으로 쓰면
객체의 프로토타입에 upgrade라는 속성이 생김


class G extends H
H: 부모 클래스
G: 자식 클래스
super는 부모클래스를 가리킴
*/

