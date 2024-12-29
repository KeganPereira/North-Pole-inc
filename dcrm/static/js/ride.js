console.log('reading');
function update_cost(){ 

   let arrive = document.getElementById('id_ride_booking_date_arrive').value 
   let leave = document.getElementById('id_ride_booking_date_leave').value

   arrive= new Date(arrive)  
   leave= new Date(leave) 
   diff= leave.getTime()- arrive.getTime(); 
   days = Math.round(Math.abs(diff/(1000*60*60*24))); 

   if(String(days) == "NaN"){ 
       let price = document.getElementById('ride_output') 
       price.innerHTML= "Ticket cost: Date has not been chosen" 


} else{ 

   let total=parseInt(adults.value)*65 
              +parseInt(children.value)*35 
              +parseInt(oaps.value)*45  


           
   total = total * days 

   let price = document.getElementById('ride_output') 

   price.innerHTML= "Ticket cost: $"+ String(total)  


} 
// Disable the booking button if negative numbers are entered
let bookBtn = document.getElementById("book-btn");
if (adultsValue < 0) {
   bookBtn.disabled = true;
} else if (childrenValue < 0) {
   bookBtn.disabled = true;
} else if (oapsValue < 0) {
   bookBtn.disabled = true;
} else {
    bookBtn.disabled = false;
}

}
let adults = document.getElementById("id_ride_booking_adults"); 
adults.addEventListener("change", update_cost) 
let children= document.getElementById("id_ride_booking_children"); 
children.addEventListener("change", update_cost) 
let oaps= document.getElementById("id_ride_booking_oap"); 
oaps.addEventListener("change", update_cost)