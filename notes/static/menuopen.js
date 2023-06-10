let submenu = document.querySelector('.submenu')
let notes = document.querySelectorAll('.note')
var colors = ["00FFFF","adff2f", "FFFF00", "FFC0CB", "FFA500"]
function getrand() {
    let choice = Math.floor(Math.random()*5);
    console.log(choice);
    return "#" + colors[choice];
}

function changecolor(){
    for(let i = 0; i<notes.length; i++){
        notes[i].style.backgroundColor = getrand()
    }
}


function onmenu(){
    if(submenu.classList.contains('active')){
        submenu.classList.remove('active')
    }
    else{
        submenu.classList.add('active')
    }
}

 var modal = document.getElementById('id01');

        window.onclick = function (event) {
            if (event.target == modal) {
                modal.style.display = "none";
            }
        }