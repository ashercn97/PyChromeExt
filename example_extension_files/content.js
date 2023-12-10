
// Content Script for: ['https://ashercn97.github.io/WebsiteForRasppi/']
setTimeout(() => { 
document.getElementById('yay').innerText = `Hello world!`;

        var xhr = new XMLHttpRequest();
        xhr.open("POST", 'http://localhost:5000/receive_data', true);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.send(JSON.stringify({ 'data': document.getElementById('yay').innerText }));
        
  }, 1000);

