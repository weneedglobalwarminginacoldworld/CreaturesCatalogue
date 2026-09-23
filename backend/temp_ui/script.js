const books = [
  { title: "Dune", author: "Frank Herbert", pages: 412, read: true },
  { title: "The Hobbit", author: "J.R.R. Tolkien", pages: 310, read: true },
  { title: "Neuromancer", author: "William Gibson", pages: 271, read: false },
  { title: "Foundation", author: "Isaac Asimov", pages: 255, read: false },
  { title: "1984", author: "George Orwell", pages: 328, read: true }
];

/* async function getData() {
  const response =  await fetch('https://jsonplaceholder.typicode.com/todos/1')
  const data = response.json()
  console.log(data)
}; */

async function checkStatus(response) {
  if (!response.ok) {
    throw new Error(`Get Failed: ${response.status}`)
  }
};
async function transferPosts() {
  const sourceUrl = 'https://jsonplaceholder.typicode.com/posts?userId=1'
  const destUrl = 'https://jsonplaceholder.typicode.com/posts'
  const responseOne = await fetch(sourceUrl)
  await checkStatus(responseOne)
  const data = await responseOne.json()
  const aTitled = data.filter(x => x.title.includes('s')).map(x => {`'OriginalId': ${x.id}`,`'title': ${x.title}`, `'titleLength': ${x.title.length}`})
  console.log(aTitled)
  const postResponse = await fetch(destUrl, {method: 'POST', headers: {'Content-type': 'application/json'}, body: JSON.stringify(aTitled)});

};
transferPosts()
const getBooks = b => {
  titles = [];
  for (let i of b){
    titles.push(i.title)
  };
  console.log(titles) 
};

// getData()
// getBooks(books);

