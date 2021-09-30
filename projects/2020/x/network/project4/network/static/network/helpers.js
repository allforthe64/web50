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


    // fetch the api url
    fetch(`/like/${post_id}`)
        .then(response => response.json())
        .then(entry => {

            //setup current likes variable
            let currentLikes = entry["likes"];
            
            alert(currentLikes)
        })
}