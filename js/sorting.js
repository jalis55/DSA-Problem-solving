let str=["hello", "world", "before", "all"]

//asscending
str.sort((a,b)=>a.length-b.length)
//desecending
str.sort((a,b)=>b.length-a.length)
console.log(str)