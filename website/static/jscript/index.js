
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

// modal jscript



$(".dashboard a").click(function(){
  document.querySelector(".appoint-form").classList.toggle("appoint-form-none");
})