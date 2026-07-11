// ======================================================
// CREDITWISE AI
// Premium JavaScript
// ======================================================

// Smooth Scroll

document.querySelectorAll('a[href^="#"]').forEach(anchor => {

    anchor.addEventListener("click", function(e){

        e.preventDefault();

        document.querySelector(this.getAttribute("href"))
        .scrollIntoView({

            behavior:"smooth"

        });

    });

});

// =============================================
// Loading Screen
// =============================================

const form=document.querySelector(".prediction-form");

const loading=document.getElementById("loading-screen");

if(form){

form.addEventListener("submit",()=>{

loading.style.display="flex";

});

}

// =============================================
// Counter Animation
// =============================================

const counters=document.querySelectorAll(".stat-card h2");

counters.forEach(counter=>{

const update=()=>{

const target=counter.innerText;

if(!isNaN(target)){

let current=0;

const interval=setInterval(()=>{

current++;

counter.innerText=current;

if(current>=target){

clearInterval(interval);

}

},25);

}

}

update();

});

// =============================================
// Fade Animation on Scroll
// =============================================

const observer=new IntersectionObserver(entries=>{

entries.forEach(entry=>{

if(entry.isIntersecting){

entry.target.style.opacity=1;

entry.target.style.transform="translateY(0px)";

}

});

});

document.querySelectorAll(".feature-card,.stat-card,.tech-card").forEach(el=>{

el.style.opacity=0;

el.style.transform="translateY(40px)";

observer.observe(el);

});

// =============================================
// Button Ripple Effect
// =============================================

document.querySelectorAll("button").forEach(button=>{

button.addEventListener("click",function(e){

const circle=document.createElement("span");

const diameter=Math.max(

button.clientWidth,

button.clientHeight

);

circle.style.width=diameter+"px";

circle.style.height=diameter+"px";

circle.style.left=e.offsetX-diameter/2+"px";

circle.style.top=e.offsetY-diameter/2+"px";

circle.classList.add("ripple");

const ripple=button.getElementsByClassName("ripple")[0];

if(ripple){

ripple.remove();

}

button.appendChild(circle);

});

});

// =============================================
// Input Validation
// =============================================

document.querySelectorAll("input[type='number']").forEach(input=>{

input.addEventListener("input",()=>{

if(input.value<0){

input.value=0;

}

});

});

// =============================================
// Navbar Shadow
// =============================================

window.addEventListener("scroll",()=>{

const nav=document.querySelector("header");

if(window.scrollY>60){

nav.style.boxShadow="0 15px 35px rgba(0,0,0,.15)";

}else{

nav.style.boxShadow="none";

}

});

// =============================================
// Typewriter Hero Text
// =============================================

const title=document.querySelector(".hero-left h1");

if(title){

const text=title.innerHTML;

title.innerHTML="";

let i=0;

function typing(){

if(i<text.length){

title.innerHTML+=text.charAt(i);

i++;

setTimeout(typing,25);

}

}

typing();

}

// =============================================
// Back To Top Button
// =============================================

const topBtn=document.createElement("button");

topBtn.innerHTML="↑";

topBtn.id="topButton";

document.body.appendChild(topBtn);

topBtn.style.position="fixed";

topBtn.style.bottom="30px";

topBtn.style.right="30px";

topBtn.style.display="none";

topBtn.style.width="55px";

topBtn.style.height="55px";

topBtn.style.borderRadius="50%";

topBtn.style.border="none";

topBtn.style.background="#2563eb";

topBtn.style.color="white";

topBtn.style.fontSize="22px";

topBtn.style.cursor="pointer";

topBtn.style.zIndex="999";

window.addEventListener("scroll",()=>{

if(window.scrollY>400){

topBtn.style.display="block";

}else{

topBtn.style.display="none";

}

});

topBtn.onclick=()=>{

window.scrollTo({

top:0,

behavior:"smooth"

});

};

// =============================================
// Random Floating Animation
// =============================================

setInterval(()=>{

document.querySelectorAll(".feature-card").forEach(card=>{

card.style.transform=`translateY(${Math.random()*8}px)`;

});

},4000);

// =============================================
// END
// =============================================