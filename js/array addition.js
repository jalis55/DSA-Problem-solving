let arr=[4, 6, 23, 10, 1, 3]

let max_value=arr[0];
let max_idx=0

for(let i=0;i<arr.length;i++){
    if (arr[i]>max_value){
        max_value=arr[i]
        max_idx=i
    }
    
}
console.log(max_value)
arr.splice(max_idx,1)

let sum=0
for(let i=0;i<arr.length;i++){
    sum +=arr[i]
}
console.log(sum)
if(sum==max_value){
    console.log("True")
}
else{
    console.log("False")
}