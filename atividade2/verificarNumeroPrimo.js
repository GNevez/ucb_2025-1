function verificarNumeroPrimo(n){
    if(n <= 1){
        return false;
    }

    if(n % 2 == 0 && n != 2){
        return false;
    }

    for(let i = 3; i < n; i += 2){
        if(n % i == 0){
            return false;
        }
    }

    return true;
}

console.log(`verificarNumeroPrimo(756)=${verificarNumeroPrimo(756)}`);
console.log(`verificarNumeroPrimo(34)=${verificarNumeroPrimo(34)}`);
console.log(`verificarNumeroPrimo(3)=${verificarNumeroPrimo(3)}`);
console.log(`verificarNumeroPrimo(7)=${verificarNumeroPrimo(7)}`);
console.log(`verificarNumeroPrimo(9)=${verificarNumeroPrimo(9)}`);
console.log(`verificarNumeroPrimo(83)=${verificarNumeroPrimo(83)}`);
console.log(`verificarNumeroPrimo(100)=${verificarNumeroPrimo(100)}`);
console.log(`verificarNumeroPrimo(543)=${verificarNumeroPrimo(543)}`);
console.log(`verificarNumeroPrimo(2047)=${verificarNumeroPrimo(2047)}`);
console.log(`verificarNumeroPrimo(3429874)=${verificarNumeroPrimo(3429874)}`);