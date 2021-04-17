const fs = require('fs');

fs.readFile('analogData.txt', 'utf8', (err, data) => {
    if (err){
        console.log(err);
    }
    else console.log(data);
});

// fs.writeFile('analog.txt',"91" , () =>{

// });

// console.log(fs);