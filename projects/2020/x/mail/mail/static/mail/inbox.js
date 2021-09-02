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
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3><br>`;

  // Get request
  fetch(`/emails/${mailbox}`)
    .then(response => response.json())
    .then(emails => {

      console.log(emails)

      if (emails.length == 0) {
        document.querySelector('#emails-view').innerHTML = '<p style = "font-size: large; font-weight: bold;">Nothing to see here :(</p>';
      }
      else{
        emails_view = document.querySelector('#emails-view');
        for (email in emails) {

          //establish variables
          var mail = document.createElement("div");
          var sender = document.createElement("h5");
          var subject = document.createElement('p');
          var time = document.createElement('p');
          var id = document.createElement('p');

          // turn off id display
          id.innerHTML = emails[email]['id'];
          id.style.display = 'none';

          // if message has no subject, set subject to equal no subject and make the color red
          sender.innerHTML = emails[email]['sender']
          if (emails[email]['ubject'] == '') {
            subject.innerHTML = 'No Subject';
            subject.style.color = 'red';
          }
          else {
            subject.innerHTML = emails[email]['subject'];
          }
          time.innerHTML = emails[email]['timestamp'];
          
          // set border styling for the div
          mail.style.borderStyle = 'solid';
          mail.style.borderColor = 'black';
          mail.style.borderWidth = '1px';
          mail.style.marginBottom = '10px';
          
          // if an email has been read or not
          if (emails[email].read == true) {
            mail.style.backgroundColor = "lightgray"
            mail.style.borderStyle = 'dashed'
          }
          else {
            mail.style.backgroundColor = 'white';
          }

          // add classes
          mail.classList.add('container');
          mail.classList.add('mail')

          // style sender
          sender.style.display = 'inline-block';
          sender.style.margin = '15px';
          
          // style sub
          subject.style.display = 'inline-block';
          subject.style.marginLeft = '5px';

          //style time
          time.style.display = 'inline-block';
          time.style.margin = '15px';
          time.style.float = 'right';
          time.style.color = 'black';

          // append mail div to email view and append elements into mail div
          emails_view.appendChild(mail);
          mail.appendChild(sender);
          mail.appendChild(subject);
          mail.appendChild(time);
          mail.appendChild(id);

          // what to do if something is clicked
          mail.addEventListener('click', () => load_email());
          subject.addEventListener('click', () => load_email());
          time.addEventListener('click', () => load_email());
          sender.addEventListener('click', () => load_email());
        }
      }
    }
    );

}

// shows the email you clicked on from mailbox
function load_email() {
  
  //shutoff any other event listeners that may have been called
  event.stopImmediatePropagation();

  // hiding everything but the email view
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'none';
  mail_view = document.querySelector('#email-view');
  mail_view.style.display = 'block';

  var target = event.target;
  console.log(target.children);

  // make sure the parent element is selected
  if (!(target.tagName == 'DIV')) {
    target = target.parentElement;
  }

  // extract id out of child elements
  var children = target.children;
  var id = children[3].innerHTML;

  // clearing old content
  mail_view.innerHTML = '';

  // Get request
  fetch(`/emails/${id}`)
    .then(response => response.json())
    .then(email => {

      // creating divs for each email in the sent box 
      var div = document.createElement('div');

      // add classes to the div
      div.classList.add('container');

      // creating elements
      var sender = document.createElement('h3');
      sender.innerText = `From: ${email['sender']}`;
      var subject = document.createElement('h5');
      subject.innerText = `Subject: ${email['subject']}`;
      var body = document.createElement('p');
      body.innerText = email['body'];
      var time = document.createElement('p');
      time.innerText = email['timestamp'];

      // styling for timestamp
      time.style.color = 'black';

      // styling for body text
      body.style.padding = '20px';
      body.style.borderStyle = 'solid';
      body.style.borderWidth = '1px';
      body.style.borderColor = 'black';

      // adding the elements to the smaller div
      div.appendChild(sender);
      div.appendChild(subject);
      div.appendChild(time);

      // adding elements to the main div
      mail_view.appendChild(div);
      mail_view.appendChild(body);

      // making sure read variable is set to true
      if (email['read'] == false) {
        // setting read atribute
        fetch(`/emails/${id}`, {
          method: 'PUT',
          body: JSON.stringify({
            read: true
          })
        })
      }


      var archive = email['archived'];

      // archive and reply buttons
      var btn = document.createElement('button');
      var reply = document.createElement('button');

      reply.style.marginLeft = "20px";

      // if the email is already archived
      if (archive) {
        btn.innerText = 'Remove From Archive';
      }
      else {
        btn.innerText = 'Archive';
      }
      reply.innerText = 'Reply';

      // add bootstrap classes
      btn.classList.add('btn-primary');
      btn.classList.add('btn');
      reply.classList.add('btn-primary');
      reply.classList.add('btn');

      // adding event listeners to both buttons

      // archive toggle
      btn.addEventListener('click', () => {
        fetch(`/emails/${id}`, {
          method: 'PUT',
          body: JSON.stringify({
            archived: !archive
          })
        });
        // loading inbox after toggling archive property
        load_mailbox('inbox');
      });

      // reply button function
      reply.addEventListener('click', () => {

        // opens the compose mail section and hides all the others
        compose_email();

        // set default values
        document.querySelector('#compose-recipients').value = email['sender'];
        document.querySelector('#compose-body').value = `${email['sender']} wrote: ${email['body']}`;

        // subject checking
        if (email['subject'].search('Re:')) {
          document.querySelector('#compose-subject').value = email['subject'];
        }
        else {
          document.querySelector('#compose-subject').value = `Re: ${email['subject']}`;
        }
      });

      // adding the buttons to page
      mail_view.appendChild(btn);
      mail_view.appendChild(reply);
    });
}

