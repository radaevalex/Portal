function color_value() {

     let values = document.getElementsByClassName("res_val");
     for(let i = 0; i < values.length; i++ ) {
         elem = values[i];
         val = parseInt(elem.textContent);
         if (val < 100) {
             elem.style.color  = "#993333";
         }
         else if (val > 100) {
             elem.style.color  = "#1c7430";
         }
         else {
             elem.style.color  = "#4e555b";
         }
     }

}

document.addEventListener("DOMContentLoaded", function() {
    color_value()
});