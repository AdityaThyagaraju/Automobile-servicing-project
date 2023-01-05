const observer = new IntersectionObserver(function(entries){
    entries.forEach((entry) => {
      if(entry.isIntersecting){
        entry.target.classList.add('show');
      }
      else{
        entry.target.classList.remove('show');
      }
    });
  
  })
  
  const hiddenElements = document.querySelectorAll(".hidden");
  hiddenElements.forEach((el) => observer.observe(el));

function delete_note(note_id){
    fetch('/delete-note',{
        method:'POST',
        body: JSON.stringify({noteId : note_id})
    }).then(res=>{
        window.location.href = "/"
    })
}