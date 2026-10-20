const options = Array.from(document.querySelectorAll('.options'))

function handleEvent(ev) {
  ev.preventDefault()
  
  options.forEach((o)=>{
    const ps = Array.from(options.map((o)=>o.querySelectorAll('.p')));
    console.log(ps[0])
    Array.from(ps[0])[0].classList.toggle('hidden');
    Array.from(ps[1])[1].classList.toggle('hidden');
    });
};

options.forEach((o)=>{
  o.addEventListener('mouseenter', handleEvent)});
options.forEach((o)=>{
  o.addEventListener('mouseleave', handleEvent)});
