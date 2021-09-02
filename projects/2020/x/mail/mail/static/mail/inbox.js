document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#email-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';


}

function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#email-view').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  // Get request
  fetch(`/emails/${mailbox}`)
    .then(response => response.json())
    .then(emails => {

      console.log(emails)

      if (emails.length == 0) {
        document.querySelector('#emails-view').innerHTML = '<p style = "font-size: large; font-weight: bold;">Nothing to see here :(</p>';
      }
      else{
        email_view = document.querySelector('#emails-view');
        for (email in emails) {

          //establish variables
          var mail = document.createElement("div");
          var sender = document.createElement("h5");
          var sub = document.createElement('p');
          var time = document.createElement('p');
          var id = document.createElement('p');

          // turn off id display
          id.innerHTML = emails[email]['id'];
          id.style.display = 'none';

          // if message has no subject, set subject to equal no subject and make the color red
          sender.innerHTML = emails[email]['sender']
          if (emails[email]['ubject'] == '') {
            sub.innerHTML = 'No Subject';
            sub.style.color = 'red';
          }
          else {
            sub.innerHTML = emails[email]['subject'];
          }
          time.innerHTML = emails[email]['timestamp'];
          
          // set border styling for the div
          mail.style.borderStyle = 'solid';
          mail.style.borderColor = 'black';
          mail.style.borderWidth = '0.1rm';
          mail.style.marginBottom = '0.2rem';
          
          // if an email has been read or not
          if (emails[email].read == true) {
            mail.style.backgroundColor = "lightgray"
          }
          else {
            mail.style.backgroundColor = 'white';
          }

          // add classes
          mail.classList.add('container');
          mail.classList.add('mail')

          // style sender
          sender.style.display = 'inline-block';
          sender.style.margin = '1rem';
          
          // style sub
          sub.style.display = 'inline-block';
          sub.style.margin = '1rem';

          //style time
          time.style.display = 'inline-block';
          time.style.margin = '1rem';
          time.style.float = 'right';
          time.style.color = 'blue';

          // append mail div to email view and append elements into mail div
          email_view.appendChild(mail);
          mail.appendChild(sender);
          mail.appendChild(sub);
          mail.appendChild(time);
          mail.appendChild(id);

          // what to do if something is clicked
          mail.addEventListener('click', () => load_email());
          sub.addEventListener('click', () => load_email());
          time.addEventListener('click', () => load_email());
          sender.addEventListener('click', () => load_email());
        }
      }
    }
    );

}

//shows the email you clicked on from mailbox
function load_email() {
  event.stopImmediatePropagation();
  //keeping only the email-view and hiding the rest
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'none';
  mail_view = document.querySelector('#email-view');
  mail_view.style.display = 'block';

  var tar = event.target;
  console.log(tar.children);

  //if the element clicked on is not div, we choose its parent (which is the div)
  if (!(tar.tagName == 'DIV')) {
    tar = tar.parentElement;
  }

  //we take the div's children elements and extract the id (we know that it is the fourth (third index) element as we checked using console.log)
  var c = tar.children;
  var id = c[3].innerHTML;

  //clearing old content
  mail_view.innerHTML = '';

  //we make a GET request to get everything we need about the email
  fetch(`/emails/${id}`)
    .then(response => response.json())
    .then(email => {

      //creating a div for each email in mailbox in which we will include sender, timestamp and subject 
      var div = document.createElement('div');

      //adding classes to that div, bootstrap sheeyit
      div.classList.add('container');
      div.classList.add('jumbotron');

      //creating the needed elements for subject, sender, etc.
      var sub = document.createElement('h3');
      sub.innerText = email['subject'];
      var sender = document.createElement('h5');
      sender.innerText = `From: ${email['sender']}`;
      var body = document.createElement('p');
      body.innerText = email['body'];
      var time = document.createElement('p');
      time.innerText = email['timestamp'];

      //styling for timestamp
      time.style.color = 'blue';

      //styling for body
      body.style.padding = '2rem';
      body.style.backgroundColor = 'lightgray';

      //adding the elements to the div we created
      div.appendChild(sub);
      div.appendChild(sender);
      div.appendChild(time);

      //adding the div and body to the main div
      mail_view.appendChild(div);
      mail_view.appendChild(body);

      //making the read attribute true in case it was false
      if (email['read'] == false) {
        //making the read attribute true
        fetch(`/emails/${id}`, {
          method: 'PUT',
          body: JSON.stringify({
            read: true
          })
        })
      }

      //Adding buttons from here on
      var archive = email['archived'];

      //archive toggle and reply button
      var btn = document.createElement('button');
      var reply = document.createElement('button');

      //setting buttons' inner text
      //if the email is already archived
      if (archive) {
        btn.innerText = 'Unarchive';
      }
      else {
        btn.innerText = 'Archive';
      }
      reply.innerText = 'Reply';

      //bootstrap sheeyit
      btn.classList.add('btn-primary');
      btn.classList.add('btn');
      reply.classList.add('btn-primary');
      reply.classList.add('btn');

      //adding event listeners to both buttons

      //first the archive toggle
      btn.addEventListener('click', () => {
        //got this from the API documentation
        fetch(`/emails/${id}`, {
          method: 'PUT',
          body: JSON.stringify({
            archived: !archive
          })
        });
        //loading inbox after done toggling archive property
        load_mailbox('inbox');
      });

      //reply button function
      reply.addEventListener('click', () => {

        //opens the compose mail section and hides all the others
        compose_email();

        //setting default values as specified
        document.querySelector('#compose-recipients').value = email['sender'];
        document.querySelector('#compose-body').value = `On ${email['timestamp']}, ${email['sender']} wrote: ${email['body']}`;
        //checking for subject
        if (email['subject'].search('Re:')) {
          document.querySelector('#compose-subject').value = email['subject'];
        }
        else {
          document.querySelector('#compose-subject').value = `Re: ${email['subject']}`;
        }
      });

      //adding the buttons to our HTML
      mail_view.appendChild(btn);
      mail_view.appendChild(reply);
    });
}

