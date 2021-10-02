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
                this.style.backgroundColor = "grey";
            }
            else {
                this.style.backgroundColor = "blue";
            }

        })
    }

})