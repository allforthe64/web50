document.addEventListener('DOMContentLoaded', function() {

    //add event listeners
    document.querySelector('#like').addEventListener('click', function() {
        id = document.querySelector('#like').value;
        console.log(id)
        like(id)
    });

})

//like function
function like(post_id) {
    alert("Someone liked a post!")
}