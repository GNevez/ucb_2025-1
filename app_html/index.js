const express = require('express');
const app = express();

app.get('/ola/:nome', (req, res) => {
    let nome = req.params.nome;
    res.send(`Olá, ${nome}`);

})

const PORT = 3000;
app.listen(PORT, () => {
    console.log("Servidor rodando na porta: " + PORT);
})