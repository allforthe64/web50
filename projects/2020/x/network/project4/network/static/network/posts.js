document.addEventListener('DOMContentLoaded', function () {

    var currentUser = document.querySelector('#currentUser').innerHTML;
    var holder = document.querySelector('#username').innerHTML;
    var profileViewing = holder.split("'");

    console.log(currentUser);
    console.log(profileViewing[0]);

    if (currentUser == profileViewing[0]) {

        //get the div with the button
        var buttonContainer = document.querySelector('#buttonContainer');

        //hide element
        buttonContainer.style.display = "none";
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
                var fHolder = document.querySelector("#followers").innerHTML;
                var followers = fHolder.split(" ");

                fHolder.innerHTML = `Followers: ${followers[1] + 1}`;

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
                var fHolder = document.querySelector("#followers").innerHTML;
                var followers = fHolder.split(" ");

                fHolder.innerHTML = `Followers: ${followers[1] - 1}`;

                //adjust styling
                this.innerHTML = "Follow";
                this.style.backgroundColor = "blue";
            }

        })
    }

})