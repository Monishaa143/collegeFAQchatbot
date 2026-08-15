function getTime(){
    const d=new Date();
    return d.getHours()+":"+String(d.getMinutes()).padStart(2,'0');
}

function sendMessage(){

    let input=document.getElementById("user-input");
    let message=input.value;

    if(message=="") return;

    let chat=document.getElementById("chat-box");

    chat.innerHTML+=`
    <div class="user">
        ${message}
        <div class="time">${getTime()}</div>
    </div>`;

    fetch("/chat",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({message:message})
    })
    .then(response=>response.json())
    .then(data=>{

        chat.innerHTML+=`
        <div class="bot">
            ${data.reply}
            <div class="time">${getTime()}</div>
        </div>`;

        chat.scrollTop=chat.scrollHeight;
    });

    input.value="";
}
