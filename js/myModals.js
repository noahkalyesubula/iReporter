//Modal for the red flags
// Get the modal
var modal = document.getElementById('AddRedFlagModal');

// Get the button that opens the modal
var modalBtn  = document.getElementById("red-flag-btn");

// Get the <span> element that closes the modal
var closeBtn = document.getElementsByClassName("closeBtn")[0];

//listen for click
modalBtn.addEventListener('click', openModal);

//listen for close click
closeBtn.addEventListener('click', closeModal);

//listen for outside click
window.addEventListener('click', clickOutside);

// When the user clicks the button, open the modal
function openModal(){
	modal.style.display = "block";
} 

//function to close modal
function closeModal(){

	modal.style.display = 'none';
}

//function to close modal if outside click

function clickOutside(e){
   if(e.target == modal){
   	modal.style.display = 'none';
   }
	
}


//Modal for the intervention
// Get the modal
var modal = document.getElementById('AddInterventionModal');

// Get the button that opens the modal
var modalBtn  = document.getElementById("intervention-btn");

// Get the <span> element that closes the modal
var closeBtn = document.getElementsByClassName("closeBtn2")[0];

//listen for click
modalBtn.addEventListener('click', openModal);

//listen for close click
closeBtn.addEventListener('click', closeModal);

//listen for outside click
window.addEventListener('click', clickOutside);

// When the user clicks the button, open the modal
function openModal(){
	modal.style.display = "block";
} 

//function to close modal
function closeModal(){

	modal.style.display = 'none';
}

//function to close modal if outside click

function clickOutside(e){
   if(e.target == modal){
   	modal.style.display = 'none';
   }
	
}







//Modal for edit red flags
var modal2 = document.getElementById('EditRedFlagModal');

// Get the button that opens the modal
var modalBtn  = document.getElementById("editRedflagBtn");

// Get the <span> element that closes the modal
var closeEditBtn = document.getElementsByClassName("closeEditBtn")[0];

//listen for click
modalBtn.addEventListener('click', openRedflaagEditModal);

//listen for close click
closeEditBtn.addEventListener('click', closeRedflagEditModal);

//listen for outside click
window.addEventListener('click', clickOutside);

// When the user clicks the button, open the modal
function openRedflaagEditModal(){
	modal2.style.display = "block";
} 

//function to close modal
function closeRedflagEditModal(){

	modal2.style.display = 'none';
}

//function to close modal if outside click

function clickOutside(e){
   if(e.target == modal){
   	modal2.style.display = 'none';
   }
	
}



//Modal for edit intervention
var modal3 = document.getElementById('EditInterventionModal');

// Get the button that opens the modal
var modalBtn  = document.getElementById("editInterventionBtn");

// Get the <span> element that closes the modal
var closeEditBtn = document.getElementsByClassName("closeEditBtn2")[0];

//listen for click
modalBtn.addEventListener('click', openInterventionEditModal);

//listen for close click
closeEditBtn.addEventListener('click', closeInterventionEditModal);

//listen for outside click
window.addEventListener('click', clickOutside);

// When the user clicks the button, open the modal
function openInterventionEditModal(){
	modal3.style.display = "block";
} 

//function to close modal
function closeInterventionEditModal(){

	modal3.style.display = 'none';
}

//function to close modal if outside click

function clickOutside(e){
   if(e.target == modal){
   	modal3.style.display = 'none';
   }
	
}





function mydeleteFunction() {
      confirm("Are you sure you want to delete this incident!");
  }

 