function myFunction(inp) {
    switch(inp) {
        case "w":
          // code block
         
          
          var audio = new Audio('sounds/tom-2.mp3');
          audio.loop = false;
          audio.play(); 
          

          break;
        case "a":
          // code block
          var audio = new Audio('sounds/tom-1.mp3');
          audio.loop = false;
          audio.play(); 

          break;
          case "s":
            var audio = new Audio('sounds/tom-3.mp3');
            audio.loop = false;
            audio.play(); 
  
            // code block
           
          break;
          case "d":
            var audio = new Audio('sounds/tom-4.mp3');
            audio.loop = false;
            audio.play(); 
  
          // code block
         
          break;
          case "j":
            var audio = new Audio('sounds/kick-bass.mp3');
            audio.loop = false;
            audio.play(); 
  
          // code block
         
          break;
          case "k":
            var audio = new Audio('sounds/crash.mp3');
            audio.loop = false;
            audio.play(); 
  
          // code block
         
          break;
          case "l":
            var audio = new Audio('sounds/crash.mp3');
            audio.loop = false;
            audio.play(); 
  
          // code block
         
          break;
            
        default:
          // code block
         
        
      } 
  }



  document.addEventListener("keypress", function(event) {
    if(event.key){
      
      
      myFunction(event.key);
    }
   
  });