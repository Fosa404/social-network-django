const message = document.getElementByClassName('notification')
const main = document.getElementByClassName('main')

function hide() {
    message.setAttribute('visivility', 'hidden')
}

console.log(main);


message.addEventListener('click',
    console.log(message),
    setTimeout(() => {
        hide();
    }, 4000)
)