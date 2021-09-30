document.addEventListener('DOMContentLoaded', function() {

    alert("Loaded!")

    //add event listeners
    document.querySelector('#like').addEventListener('click', function() {
        id = document.querySelector('#like').value;
        alert(id)
    });

})

//like function
function like() {
    alert("Someone liked a post!");
}