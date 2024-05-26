// const message = document.getElementByClassName('notification')
const message = document.querySelector('.notification')

window.addEventListener('load',()=>{
    setTimeout(()=>{
        message.style.display= 'none';
    }, 4000)
})




