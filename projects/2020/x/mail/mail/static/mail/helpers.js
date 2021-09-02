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
        console.log(result);
    })
  }

  