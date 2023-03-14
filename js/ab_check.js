let str="lane borrowed"

for(let i=0;i<str.length-4;i++){
    if(str[i]=='a' && str[i+4]=='b')
    {
        console.log(true)
    }
    if(str[i]=='b' && str[i+4]=='a'){
        console.log(true)
    }
}