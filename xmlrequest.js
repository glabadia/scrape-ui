const request = (method, url) => {
 return new Promise((resolve, reject) => {
  const xhr = new XMLHttpRequest();
  xhr.open(method, url);
  xhr.onload = resolve;
  xhr.onerror = reject;
  xhr.send();
 });
};

const runAPI = () => {
 let exchange = document.getElementById("exchange").value;
 if (exchange === "context") {
  request("GET", 'https"//api.jw.org')
   .then(d1 => {
    console.log(d1.target.responseText);
   })
   .catch(err => {
    console.log(err);
   });
 }
};
