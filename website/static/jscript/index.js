
// Animation for blur and position

const observer = new IntersectionObserver(function(entries){
  entries.forEach((entry)=>{
    if(entry.isIntersecting){
      entry.target.classList.add('show');
    }
    else entry.target.classList.remove('show');
  });
});

hidden = document.querySelectorAll('.hidden')
hidden.forEach((el)=>{observer.observe(el)});

// Animation for brightness

const observer_brght = new IntersectionObserver(function(entries){
  entries.forEach((entry)=>{
    if(entry.isIntersecting){
      entry.target.classList.add('show-brightness');
    }
    else entry.target.classList.remove('show-brightness');
  });
});
hidden_brght=document.querySelectorAll('.hidden-brightness')
hidden_brght.forEach((el)=>{observer_brght.observe(el)});

// Animation for xmovement

const observer_hor = new IntersectionObserver(function(entries){
  entries.forEach((entry)=>{
    if(entry.isIntersecting){
      entry.target.classList.add('show-horizontal');
    }
    else entry.target.classList.remove('show-horizontal');
  });
});

hidden_hor = document.querySelectorAll('.hidden-horizontal')
hidden_hor.forEach((el)=>{observer_hor.observe(el)});


//                                                       customer
// appointment form jscript

$(".dashboard #appointment").click(function(){
  if(!$(".payment-input").hasClass("appoint-form-none")){
    $(".payment-input").toggleClass("appoint-form-none");
  }
  else if(!$(".bill-js").hasClass("appoint-form-none")){
    $(".bill-js").toggleClass("appoint-form-none")
  }
  // else if(!$("#request-alert").hasClass("appoint-form-none"))
  // {
  //   $("#request-alert").toggleClass("appoint-form-none")
  // }
  else{
    $("#request-alert").toggleClass("appoint-form-none");
  }
  $(".request-form").toggleClass("appoint-form-none");
  

})


// for view bill in customer
$(".dashboard #bill").click(function(){
  if(!$(".request-form").hasClass("appoint-form-none")){
    $(".request-form").toggleClass("appoint-form-none");
  }
  else if(!$(".payment-input").hasClass("appoint-form-none")){
    $(".payment-input").toggleClass("appoint-form-none")
  }
  else{
    $("#request-alert").toggleClass("appoint-form-none");
  }

  $(".bill-js").toggleClass("appoint-form-none");
  

})



// for payment customer in customer
$(".dashboard #payment-dash").click(function(){
  if(!$(".request-form").hasClass("appoint-form-none")){
    $(".request-form").toggleClass("appoint-form-none");
  }
  else if(!$(".bill-js").hasClass("appoint-form-none")){
    $(".bill-js").toggleClass("appoint-form-none")
  }
  else{
    $("#request-alert").toggleClass("appoint-form-none");
  }

  $(".payment-input").toggleClass("appoint-form-none");
  

})


//                                                               staff

// for generating bill in staff
$(".dashboard #gen-bill").click(function(){
  if(!$("#cust-req").hasClass("appoint-form-none")){
    $("#cust-req").toggleClass("appoint-form-none")
  }
  
  $("#bill-form").toggleClass("appoint-form-none");
  

})



// for customer service request in staff
$(".dashboard #from-cust-req").click(function(){
  if(!$("#bill-form").hasClass("appoint-form-none")){
    $("#bill-form").toggleClass("appoint-form-none")
  }
  
  $("#cust-req").toggleClass("appoint-form-none");
  

})



//                                                                        admin

// for customer list in admin
$(".dashboard #cust-all").click(function(){
  if(!$("#staff-detail").hasClass("appoint-form-none")){
    $("#staff-detail").toggleClass("appoint-form-none")
  }
  else if(!$("#st-req").hasClass("appoint-form-none")){
    $("#st-req").toggleClass("appoint-form-none")
  }
  $("#cust-detail").toggleClass("appoint-form-none");
  

})



// for staff list in admin
$(".dashboard #staff-all").click(function(){
  if(!$("#cust-detail").hasClass("appoint-form-none")){
    $("#cust-detail").toggleClass("appoint-form-none")
  }
  else if(!$("#st-req").hasClass("appoint-form-none")){
    $("#st-req").toggleClass("appoint-form-none")
  }
  

  $("#staff-detail").toggleClass("appoint-form-none");
  

})

// for staff request in admin
$(".dashboard #staff-signup-req").click(function(){
  if(!$("#staff-detail").hasClass("appoint-form-none")){
    $("#staff-detail").toggleClass("appoint-form-none");
  }
  else if(!$("cust-detail").hasClass("appoint-form-none")){
    $("cust-detail").toggleClass("appoint-form-none")
  }
  

  $("#st-req").toggleClass("appoint-form-none");
  

})



// msgp-popup

$("#loginmsg button").click(function(){
  document.querySelector("#loginmsg")
}
)

$("#loginmsgcust button").click(function(){
  document.querySelector("#loginmsgcust")
}
)

$("#loginmsgstaff button").click(function(){
  document.querySelector("#loginmsgstaff")
}
)

$("#loginmsgadmin button").click(function(){
  document.querySelector("#loginmsgadmin")
}
)

// form-slot






