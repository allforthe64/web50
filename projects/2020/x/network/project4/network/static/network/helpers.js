document.addEventListener('DOMContentLoaded', function() {

    //add event listeners
    document.querySelectorAll('#like').forEach(item => {
        item.addEventListener('click', event => {

            if (item.backgroundColor = "Blue") {

                like(item.value);
                
                var target = event.target;

                // select the parent div
                if (!(target.tagName == 'DIV')) {
                    target = target.parentElement
                }

                // get the parent div's children 
                var children = target.children;

                //change the inner html
                fetch(`/like/${item.value}`)
                    .then(response => response.json())
                    .then(entry => {
                        children[1].innerHTML = `${entry["likes"] + 1} Likes`;
                    })
                    
                item.innerHTML = 'Unlike';
                item.style.width = "75px";
                item.style.backgroundColor = "Grey";
            }
            
            if (item.backgroundColor = "Grey") {

                alert("dislike activated");
                
                dislike(item.value);

                var target = event.target;

                if (!(target.tagName == 'DIV')) {
                    target = target.parentElement;
                }

                var children = target.children;

                //chagne the inner html
                fetch(`/like/${item.value}`)
                    .then(response => response.json())
                    .then(entry => {
                        children[1].innerHTML = `${entry["likes"] - 1} Likes`;
                    })

                item.innerHTML = 'Like';
                item.style.width = "60px";
                item.style.backgroundColor = "Blue";
            }
        })
        
    })

})

//like function
function like(post_id) {

    // fetch the api url
    fetch(`/like/${post_id}`)
        .then(response => response.json())
        .then(entry => {

            //establish the current number of likes and update the value
            let currentLikes = entry["likes"];
            let newLikes = currentLikes + 1;

            //make put request and update the number of likes
            fetch(`/like/${post_id}`, {
                method: 'PUT',
                body: JSON.stringify({
                    likes: newLikes
                })
            })

        })
}

//dislike function
function dislike(post_id) {

    // fetch the api url
    fetch(`/like/${post_id}`)
        .then(response => response.json())
        .then(entry => {

            //establish the current number of likes and update the value
            let currentLikes = entry["likes"];
            let newLikes = currentLikes - 1;

            //make put request and update the number of likes
            fetch(`/like/${post_id}`, {
                method: 'PUT',
                body: JSON.stringify({
                    likes: newLikes
                })
            })

        })
}