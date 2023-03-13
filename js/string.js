//concat string

let a='hello'
let b='world'

let c=a+' '+b
console.log(c)
console.log(`after concatination ${c}`)

var text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
console.log(`The lengt of the text is:${text.length}`)

var text = "Apple, Banana, Kiwi";
console.log(text.slice(7,13))
console.log(text.slice(7))
console.log(text.slice(-12))
console.log(text.slice(-12, -6))

let str = "Apple, Banana, Kiwi";
console.log(str.substring(7))

//substr
//substring
let text1 = "a,b,c,d,e,f";
console.log(text1.replace('a','x'))
console.log(text1.split(","))