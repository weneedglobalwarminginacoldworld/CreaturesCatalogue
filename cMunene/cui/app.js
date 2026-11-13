let start;
const posters = Array.from(document.querySelectorAll('.p'))
let index = posters.findIndex((e)=>{
  const test = ['p']
  return arrayCompare(Array.from(e.classList), test)
})

function loadNext() {
  posters.some()
}

function posterSwipe() {
  posters[index].animate(
    [
      {transform: 'translate(10px)'},
      {transform: 'translate(5px)'},
      {transform: 'translate(-300px)'}
    ],
    {
      duration: 500,
      easing: 'cubic-bezier(0.42, 0.58, 0, 1)',
      iterations: 1
    }
  )
  loadNext()
};
posters[index].addEventListener('click', posterSwipe)

function arrayCompare(a, b){
  if (typeof a === typeof b) {
    if (a.length === b.length) {
      let zipped = a.map((v, i)=>[v, b[i]]);
      const isEqual = zipped.every((z)=>{
        if (z[0] === z[1]) {
          return true
        } else return false
      })
    return isEqual;
    }
  }
};
