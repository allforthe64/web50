document.addEventListener('DOMContentLoaded', function() {

    //add event listeners
    document.querySelectorAll('#like').forEach(item => {
        item.addEventListener('click', event => {
            like(item.value);
        })
    })

})

//like function
function like(post_id) {
    alert(post_id);
}