let str="this is practical"

let newStr=str.split(" ")

console.log(newStr)

for(let i=0;i<newStr.length;i++){
    newStr[i]=newStr[i][0].toUpperCase()+newStr[i].substr(1)
}

console.log(newStr)

newStr=newStr.join(" ")

console.log(newStr)
//make first letter lower and others capital

let newStr2=str.split(" ")
console.log(newStr2)

for(let i=0;i<newStr2.length;i++){
    newStr2[i]=newStr2[i][0].toLowerCase()+(newStr2[i].substr(1)).toUpperCase()
}
console.log(newStr2)
newStr2=newStr2.join(" ")
console.log(newStr2)