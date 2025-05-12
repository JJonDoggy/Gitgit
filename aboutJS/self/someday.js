class raechi{
    intro = '굿모닝!';
    
    name;
    constructor(name){
        this.name = name;
    }

    hi(){
        console.log(this.name, '우앙뇽~')
    }
}

Goraechi = new raechi('현석이')
Goraechi.hi()