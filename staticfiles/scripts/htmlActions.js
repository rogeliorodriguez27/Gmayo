


function stopDefAction(evt) {
    evt.preventDefault();
  }
  
  
  
  // Function to add event listener to pdf 
  function load() {
    var pdf = document.getElementById("pdf");
    let link = pdf.getAttribute("href");
    
    pdf.addEventListener("click", print, false);
    return link;
  }
  
  document.addEventListener("DOMContentLoaded", load, false);
  
  
    
  
  // Function to print
  function print() {
    link = load()
      console.log(link)
    window.open(`../../media/${link}`);
   
  }
    
  