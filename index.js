import express from 'express';

const app = express();

app.get('/', (req, res) => {
    res.sendFile(import.meta.dirname + '/index.html')
})
// 여기까지 지우지 마세요

app.use('/add', express.urlencoded({extended: false}))
app.post('/add', (req, res) => {
    res.setHeader('Content-Type', 'text/plain; charset=UTF-8');
    console.log(req.body);
    
    const num1 = Number(req.body.number1)
    const num2 = Number(req.body.number2)
    res.end(`더한 값 : ${num1 + num2}`);
})

// 여기부터 지우지 마세요
app.listen(3000);