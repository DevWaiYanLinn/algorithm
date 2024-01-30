function dontGiveMeFive(start, end)
{
   return Array(end-start+1).fill(null).filter((a,b) => {
        return !`${b + start}`.includes('5')
   }).length
}

console.log(dontGiveMeFive(1,90))