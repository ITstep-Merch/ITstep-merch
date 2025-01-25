import {initializeLikesCounter} from '../popUpCartLikeInitializeCounter/popUpinitializeLikesCouner.js' //!!!! буква і

export function animateLike(ID){
    initializeLikesCounter()
    const likeButton = document.querySelector('.like-good-catalog');
    const likeButtonID = document.getElementById(ID);
        
    likeButtonID.classList.add('animate');
    setTimeout(() => {
        likeButtonID.classList.remove('animate');
    }, 450); 
}
window.animateLike = animateLike;