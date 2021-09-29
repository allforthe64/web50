document.addEventListener('DOMContentLoaded', function() {

    //add event listeners
    document.querySelector('Like').addEventListener('click', () => like);

})

//like function
function like() {
    alert("Someone liked a post!")
}