function send() {
    fetch('/emails', {
        method: 'POST',
        body: JSON.stringify({
            recipients: document.getElementById('compose-recipients').value,
            subject: document.getElementById('compose-subject').value,
            body: document.getElementById('compose-body').value
        })
    })
    .then(response => response.json())
    .then(result => {
        //print result
        console.log(result)
    })
  }

  function emails_in_inbox () {
      fetch('/emails/inbox')
      .then(response => response.json())
      .then(emails => {
          //print emails to log
          console.log(emails)
      })
  }