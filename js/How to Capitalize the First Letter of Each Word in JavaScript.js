let str="this is practical"

let newStr=str.split(" ")

console.log(newStr)

for(let i=0;i<newStr.length;i++){
    newStr[i]=newStr[i][0].toUpperCase()+newStr[i].substr(1)
}

console.log(newStr)

newStr=newStr.join(" ")

console.log(newStr)