//  define variables

let resultContainer = document.querySelector('.result');
let result = document.getElementById('lable');
let btn = document.querySelector('form button');
let form = document.querySelector('form');
if(result.innerHTML === 'POSITIVE'){
    resultContainer.classList.add('positive');
}else if(result.innerHTML === 'NEGATIVE'){
    resultContainer.classList.add('negative');

}



btn.addEventListener('click', function(){
    if(result.innerHTML === 'POSITIVE'){
        resultContainer.classList.add('positive');
    }else{
        resultContainer.classList.add('negative');

    }
})

