const slider = document.getElementById("slider");
const temp = document.getElementById("temp");

slider.oninput = () => {
    temp.value = slider.value;
};

temp.oninput = () => {
    slider.value = temp.value;
};

async function predictSales(){

    document.getElementById("loading").style.display="block";

    const response = await fetch("/predict",{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({
            temp:temp.value
        })

    });

    const data = await response.json();

    document.getElementById("loading").style.display="none";

    animateValue(
        document.getElementById("sales"),
        data.sales
    );
}

function animateValue(element,value){

    let current=0;

    const increment=value/50;

    const interval=setInterval(()=>{

        current+=increment;

        if(current>=value){

            current=value;

            clearInterval(interval);

        }

        element.innerHTML="$"+current.toFixed(2);

    },20);

}