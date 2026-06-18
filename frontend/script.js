function login(successcallback){

    let email=document.getElementById("email").value;
    let password=document.getElementById("password").value;

    fetch("http://127.0.0.1:5000/login",{
        method:"POST",
        credentials:"include",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({
            email:email,
            password:password
        }) 
    }
    )
.then(function(response) {

    if (!response.ok) {
        throw new Error("Login failed");
    }

    return response.json();
})
.then(function(data) {

    console.log(data);

    successcallback();
})
.catch(function(error) {
    console.log(error);
});
}

document.getElementById("id1").addEventListener("submit",function(event){

    event.preventDefault();

    login(function(){
        window.location.href="shortenurl.html";
    });
});