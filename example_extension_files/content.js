
// Content Script for: ['https://www.example.com/']
setTimeout(() => { 
document.querySelector('h1').innerText = `Modified by PyChromeExt!`;
  }, 1000);

