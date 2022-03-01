$(function() {

  $("#contactForm input,#contactForm textarea").jqBootstrapValidation({
    preventSubmit: true,
    submitError: function($form, event, errors) {
      // additional error messages or events
    },
    submitSuccess: function($form, event) {
      event.preventDefault(); // prevent default submit behaviour
      // get values from FORM
      var name = $("input#name").val();
      var email = $("input#email").val();
      var phone = $("input#phone").val();
      var message = $("textarea#message").val();
      var firstName = name; // For Success/Failure Message
      // Check for white space in name for Success/Fail message
      if (firstName.indexOf(' ') >= 0) {
        firstName = name.split(' ').slice(0, -1).join(' ');
      }
      $this = $("#sendMessageButton");
      $this.prop("disabled", true); // Disable submit button until AJAX call is complete to prevent duplicate messages
      Email.send({
        Host:"smtp.gmail.com",
        Username:"contactforestcare@gmail.com",
        Password:"forestcare@srm",
        To:"contactforestcare1@gmail.com",
        From:"contactforestcare@gmail.com",
        Subject:`New message from ${name}`,
        Body:`
          <h4>Name: ${name}</h4>
          <h4>Phone: ${phone}</h4>
          <h4>Email: ${email}</h4>

          <p style="font-size:15px">${message}</p>
        `
      }).then(function(message){
        console.log(message)
        $('#success').html("<div class='alert alert-success'>");
        $('#success > .alert-success').html("<button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;")
          .append("</button>");
        $('#success > .alert-success')
          .append("<strong>Your message has been sent. </strong>");
        setTimeout(function(){
          document.querySelector('.alert-success').style.display = 'none';
        },3000);
        $('#success > .alert-success')
          .append('</div>');
        //clear all fields
        $('#contactForm').trigger("reset");
      }).catch(function(err){
          $('#success').html("<div class='alert alert-danger'>");
          $('#success > .alert-danger').html("<button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;")
            .append("</button>");
          $('#success > .alert-danger').append($("<strong>").text("Sorry " + firstName + ", it seems that my mail server is not responding. Please try again later!"));
          setTimeout(function(){
            document.querySelector('.alert-danger').style.display = 'none';
          },3000);
          $('#success > .alert-danger').append('</div>');
          //clear all fields
          $('#contactForm').trigger("reset");
      })
    },
    filter: function() {
      return $(this).is(":visible");
    },
  });

  $("a[data-toggle=\"tab\"]").click(function(e) {
    e.preventDefault();
    $(this).tab("show");
  });
});

$('#name').focus(function() {
  $('#success').html('');
});
