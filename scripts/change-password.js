const visibilityIcon1 = document.querySelector(".visibility-icon1");
    const visibilityIcon2 = document.querySelector(".visibility-icon2");
    const visibilityIcon3 = document.querySelector(".visibility-icon3");
    const currentPassword= document.querySelector("#currentPassword");
    const newPassword = document.querySelector("#newPassword");
    const confirmPassword = document.querySelector("#confirmPassword")

    var passwordVisible = true;


    visibilityIcon1.addEventListener('click', function() {
      if (passwordVisible){
        currentPassword.setAttribute('type', 'text');
        visibilityIcon1.setAttribute('class', "bi-eye");
      }else{
        currentPassword.setAttribute('type', 'password')
        visibilityIcon1.setAttribute('class', 'bi-eye-slash')
      }
      passwordVisible = !passwordVisible

    });

    visibilityIcon2.addEventListener('click', function() {
      if (passwordVisible){
        newPassword.setAttribute('type', 'text');
        visibilityIcon2.setAttribute('class', "bi-eye");
      }else{
        newPassword.setAttribute('type', 'password')
        visibilityIcon2.setAttribute('class', 'bi-eye-slash')
      }
      passwordVisible = !passwordVisible

    });

    visibilityIcon3.addEventListener('click', function() {
      if (passwordVisible){
        confirmPassword.setAttribute('type', 'text');
        visibilityIcon3.setAttribute('class', "bi-eye");
      }else{
        confirmPassword.setAttribute('type', 'password')
        visibilityIcon3.setAttribute('class', 'bi-eye-slash')
      }
      passwordVisible = !passwordVisible

    });

  

function validatePassword(){
  if(newPassword.value != confirmPassword.value) {
    confirmPassword.setCustomValidity("Passwords do not Match");
  } else {
confirmPassword.setCustomValidity("")
    
  }
}

newPassword.onchange = validatePassword;
confirmPassword.onkeyup = validatePassword;




    
 