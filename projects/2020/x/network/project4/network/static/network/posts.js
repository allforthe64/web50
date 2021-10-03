document.addEventListener('DOMContentLoaded', function () {

    var currentUser = document.querySelector('#currentUser').innerHTML;
    var holder = document.querySelector('#username').innerHTML;
    var profileViewing = holder.split("'");

    //query the api to see if the user is currently following the page
    fetch(`/search/${profileViewing[0]}/${currentUser}`)
        .then(response => response.json())
        .then(result => {

            var isFollowing = result;

            if (isFollowing == true) {
                var button = document.querySelector("#follow");

                button.innerHTML = "Unfollow";
                button.style.backgroundColor = "grey";
            }
            
        })

    if (currentUser == profileViewing[0]) {
        //get the div with the button
        var buttonContainer = document.querySelector('#buttonContainer');

        //hide element
        buttonContainer.style.display = "none";

        //query for like buttons and hide them 
        document.querySelectorAll('#like').forEach(item => {
            item.style.display = "none";
        })
    }
    else {

        //add event listener 
        document.querySelector('#follow').addEventListener("click", function () {
            
            if (this.style.backgroundColor == "blue")
            {
                //call the api
                fetch(`/follow/follow/${profileViewing[0]}`, {
                    method: "PUT",
                    body: JSON.stringify({
                        following: profileViewing[0],
                        followedBy: currentUser
                    })
                })

                //update the elements displaying followers
                fetch(`/number/${profileViewing[0]}`)
                    .then(response => response.json())
                    .then(result => {
                        result += 1;
                        var display = document.querySelector("#followers");
                        display.innerHTML = `Follower: ${result}`;
                    })

                //adjust styling
                this.innerHTML = "Unfollow";
                this.style.backgroundColor = "grey";
            }
            else {
                
                //call the api
                fetch(`/follow/unfollow/${profileViewing[0]}`, {
                    method: "PUT",
                    body: JSON.stringify({
                        following: profileViewing[0],
                        followedBy: currentUser
                    })
                })

                //update the elements displaying followers
                fetch(`/number/${profileViewing[0]}`)
                    .then(response => response.json())
                    .then(result => {
                        result -= 1;
                        var display = document.querySelector("#followers");
                        display.innerHTML = `Follower: ${result}`;
                    })

                //adjust styling
                this.innerHTML = "Follow";
                this.style.backgroundColor = "blue";
            }

        })
    }

    //add event listeners
    document.querySelectorAll('#like').forEach(item => {
        item.addEventListener('click', event => {

            if (item.style.backgroundColor == 'blue') {
                
                like(item.value);

                var target = event.target;

                // select the parent div
                if (!(target.tagName == 'DIV')) {
                    target = target.parentElement;
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
            } else{
                
                dislike(item.value);

                var target = event.target;

                // select the parent div
                if (!(target.tagName == 'DIV')) {
                    target = target.parentElement;
                }

                // get the parent div's children 
                var children = target.children;

                //change the inner html
                fetch(`/like/${item.value}`)
                    .then(response => response.json())
                    .then(entry => {
                        children[1].innerHTML = `${entry["likes"] - 1} Likes`;
                    })
                    
                item.innerHTML = 'Like';
                item.style.width = "60px";
                item.style.backgroundColor = "blue";
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

            console.log(`current likes: ${currentLikes}`);
            console.log(`new likes: ${newLikes}`);
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
            
            console.log(`current likes: ${currentLikes}`);
            console.log(`new likes: ${newLikes}`);

            //make put request and update the number of likes
            fetch(`/like/${post_id}`, {
                method: 'PUT',
                body: JSON.stringify({
                    likes: newLikes
                })
            })

        })
}