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

const observer_hor = new IntersectionObserver(function(entries){
  entries.forEach((entry)=>{
    if(entry.isIntersecting){
      entry.target.classList.add('show-horizontal');
    }
    else entry.target.classList.remove('show-horizontal');
  });
});
hidden_hor=document.querySelectorAll('.hidden-horizontal')
hidden_hor.forEach((el)=>{observer_hor.observe(el)});


$(document).ready(function() {             $('#loginModal').modal('show');
  $(function () {
    $('[data-toggle="tooltip"]').tooltip()
  })
});