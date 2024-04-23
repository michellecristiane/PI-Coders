const txtEmail = document.getElementById("txtEmail")//armazenar um valor em uma varuiavel(const)
const msgdFeedback = document.getElementById("newsletterFeedback")
console.log(txtEmail.value)//


function cadastrarEmail() {
    let email = txtEmail.value
    //msgFeeedback.innerHTML = 'O email $(email) foi cadastrado com sucesso'
    alert(`O email ${email} foi cadastrado co sucesso`);
}