function swap(referTo){//referTo refers to the current div where this function is defined
    if(referTo.getAttribute("data-tab")=="login"){
        document.getElementById("form-body").classList.remove("active");
        referTo.parentNode.classList.remove("signup");//removes/hides the signup form
    }
    else{
        document.getElementById("form-body").classList.add("active");
        referTo.parentNode.classList.add("signup");//adds the signup form
    }
}