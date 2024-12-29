console.log('reading');
function update_cost() { 
    let arrive = document.getElementById('id_ride_booking_date_arrive').value; 
    let leave = document.getElementById('id_ride_booking_date_leave').value;

    arrive = new Date(arrive);  
    leave = new Date(leave); 
    let diff = leave.getTime() - arrive.getTime(); 
    let days = Math.round(Math.abs(diff / (1000 * 60 * 60 * 24))); 

    let adults = document.getElementById("id_ride_booking_adults");
    let children = document.getElementById("id_ride_booking_children");
    let oaps = document.getElementById("id_ride_booking_oap");
    
    let adultsValue = parseInt(adults.value);
    let childrenValue = parseInt(children.value);
    let oapsValue = parseInt(oaps.value);
    
    // Validate that the number is not less than 0
    if (adultsValue < 0 || childrenValue < 0 || oapsValue < 0) {
        alert("Number of people cannot be less than 0.");
        return;
    }

    if (String(days) == "NaN") { 
        let price = document.getElementById('ride_output'); 
        price.innerHTML = "Ticket cost: Date has not been chosen"; 
    } else { 
        let total = adultsValue * 65 + childrenValue * 35 + oapsValue * 45; 
        total = total * days; 

        let price = document.getElementById('ride_output'); 
        price.innerHTML = "Ticket cost: $" + String(total); 
    }
    
    // Disable the booking button if negative numbers are entered
    let bookBtn = document.getElementById("book-btn");
    if (adultsValue < 0 || childrenValue < 0 || oapsValue < 0) {
        bookBtn.disabled = true;
    } else {
        bookBtn.disabled = false;
    }
}

let adults = document.getElementById("id_ride_booking_adults"); 
adults.addEventListener("change", update_cost); 
let children = document.getElementById("id_ride_booking_children"); 
children.addEventListener("change", update_cost); 
let oaps = document.getElementById("id_ride_booking_oap"); 
oaps.addEventListener("change", update_cost);