let swarupName = document.querySelector('#swarup-name')
let swarupNo = document.querySelector('#swarup-no')
let siddhiName = document.querySelector('#siddhi-name')
let siddhiNo = document.querySelector('#siddhi-no')
let dineshName = document.querySelector('#dinesh-name')
let dineshNo = document.querySelector('#dinesh-no')

function swarupOn() {
    swarupNo.classList.remove('passive')
}

function swarupOff() {
    swarupNo.classList.add('passive')
}

function siddhiOn() {
    siddhiNo.classList.remove('passive')
}

function siddhiOff() {
    siddhiNo.classList.add('passive')
}

function dineshOn() {
    dineshNo.classList.remove('passive')
}

function dineshOff() {
    dineshNo.classList.add('passive')
}