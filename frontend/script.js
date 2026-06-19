function signup(signupcallback){
    
    let name=document.getElementById("username").value;
    let email=document.getElementById("email").value;
    let password=document.getElementById("password").value;

    fetch("http://127.0.0.1:5000/signup",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({
            username:name,
            email:email,
            password:password
        })
    }
)
.then(function(response){

    if(!response.ok){
        return response.json().then(function(data){
            throw new Error(data.message);
        });
    }

    return response.json();
})
.then(function(data){

    console.log(data);
    signupcallback();

})
.catch(function(error){

    alert(error.message);

});
}

let signupform=document.getElementById("id6");
if(signupform){
    signupform.addEventListener("submit",function(event){

        event.preventDefault();

        signup(function(){
            window.location.href="login.html";
        });
    });
}


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

let loginform=document.getElementById("id1");
if(loginform){
    loginform.addEventListener("submit",function(event){

    event.preventDefault();

    login(function(){
        window.location.href="shortenurl.html";
    });
});
}


function shortenurl(){

    let url=document.getElementById("id3").value;
                                 
    fetch("http://127.0.0.1:5000/urlshorten",{
        method:"POST",
        credentials: "include",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({
            url:url
        })
    }
    )
    .then(function(response){
        if(!response.ok){
            throw new Error("login failed");
        }
        return response.json();
    })
    .then(function(data) {

    console.log(data);
})
.catch(function(error) {
    console.log(error);
});
}

let shortenurlform=document.getElementById("id2");
if(shortenurlform){
    addEventListener("submit",function(event){

    event.preventDefault()

    shortenurl();
});
}

function logout(){

    fetch("http://127.0.0.1:5000/logout",{
        method:"POST",
        credentials:"include"
    })
    .then(function(response){
        if(!response.ok){
            throw new Error("logout failed");
        }

        return response.json();
    })
    .then(function(data){
        console.log(data);
        window.location.href="login.html";
    })
}
let logoutbutton=document.getElementById("id5");
if(logoutbutton){
    logoutbutton.addEventListener("click",function(){
    
    logout();
});
}