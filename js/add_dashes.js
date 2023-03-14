let str="454793"
console.log(str.slice(-1))


let newStr=str[0]

for(let i=1;i<str.length;i++){
    if((newStr.slice(-1)%2 ===1) && (str[i]%2===1)){
       newStr +='-'
       newStr +=str[i]
    }
    else{
        newStr +=str[i]
    }
}
console.log(newStr)