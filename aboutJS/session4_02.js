/*
Character라는 클래스 만들기
• x좌표와 y좌표를 나타내는 속성이 존재(기본값 0)
• move 메소드 존재, 파라미터 2개, 각각 x변화량 y변화량 나타냄
• 체력을 나타내는 속성 존재 (기본값 100)
• 체력을 깎는 메소드 존재, 파라미터로 깎는 양을 넣음
*/

class Character{
    hp = 100;
    x;
    y;
    type = 'normal';

    constructor(name){
        this.name = name;
    }

    move(x, y){
        this.x += x;
        this.y += y;
    }

    hurt(damage){
        this.hp -= damage;
    }

    hit(target, damage){
        target.hurt(damage);
    }
}
/* type마다 주는 데미지를 다르게 하는 것도 구현해보기
각 클래스에 데미지 계산을 넣어주자자
*/
class Warrior extends Character{
    type = 'Warrior';

    hurt(damage){
        this.hp -= damage * 0.8;
    }
}

class Thief extends Character{
    type = 'Thief';

    hurt(damage){
        this.hp -= (damage + 5);
    }
}