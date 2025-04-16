// let a = prompt("Введите слово"); //всплывающее окно с прозьбойввести текст
// console.log(a);

let btn = document.querySelector(".info-companu-btn");// ищем кнопку
let modal = document.querySelector(".feedback");
let cross = document.querySelector('.feedback-close')
console.log(btn);//выводим в консоль
btn.addEventListener('click', function () { // проверяем клик на кнопку
    console.log('кнопка нажата') // по итогам проверки выводим в консоль кнопка нажата
    // document.body.style.backgroundColor='blue'
    // document.body.classList.add('body-color')
    // document.body.classList.toggle('body-color')
    modal.classList.add('feedback-show')
});

cross.addEventListener('click', function () {
    modal.classList.remove('feedback-show')
})

let slidebtn1 = document.querySelector('.slider-button-left');
let slidebtn2 = document.querySelector('.slider-button-right');
let slide1 = document.querySelector('.slide1');
let slide2 = document.querySelector('.slide2');

slidebtn1.addEventListener('click', function () {
    slide2.classList.remove('slide-active')
    slide1.classList.add('slide-active')
})

slidebtn2.addEventListener('click', function () {
    slide1.classList.remove('slide-active')
    slide2.classList.add('slide-active')
})

let servisesbtn1 = document.querySelector('#servisesbtn1')
let servisesbtn2 = document.querySelector('#servisesbtn2')
let servisesbtn3 = document.querySelector('#servisesbtn3')
let serviseslide1 = document.querySelector('#servises1')
let serviseslide2 = document.querySelector('#servises2')
let serviseslide3 = document.querySelector('#servises3')


servisesbtn1.addEventListener('click', function () {
    servisesbtn1.classList.add('servises-button-active')
    servisesbtn2.classList.remove('servises-button-active')
    servisesbtn3.classList.remove('servises-button-active')
    serviseslide1.classList.add('servises-item-active')
    serviseslide2.classList.remove('servises-item-active')
    serviseslide3.classList.remove('servises-item-active')
})

servisesbtn2.addEventListener('click', function () {
    servisesbtn1.classList.remove('servises-button-active')
    servisesbtn2.classList.add('servises-button-active')
    servisesbtn3.classList.remove('servises-button-active')
    serviseslide1.classList.remove('servises-item-active')
    serviseslide2.classList.add('servises-item-active')
    serviseslide3.classList.remove('servises-item-active')
})

servisesbtn3.addEventListener('click', function () {
    servisesbtn1.classList.remove('servises-button-active')
    servisesbtn2.classList.remove('servises-button-active')
    servisesbtn3.classList.add('servises-button-active')
    serviseslide1.classList.remove('servises-item-active')
    serviseslide2.classList.remove('servises-item-active')
    serviseslide3.classList.add('servises-item-active')
})