#!/usr/bin/node
const args = process.argv;
if (args.length <= 3) {
  console.log(0);
} else {
  const argList = [];
  for (let i = 2; i < args.length; i++) {
    argList.push(args[i]);
  }
  argList.sort((a, b) => a - b);
  console.log(argList[argList.length - 2]);
}

// for (let i = 0; i < argList.length; i++) {
//     // let large = args[i];
//     if (i + 1 !== argList.length) {
//         if (argList[i] > argList[i + 1]) {
//             let temp = argList[i];
//             argList[i] = argList[i + 1];
//             argList[i + 1] = temp;
//         }
//     } else {
//         console.log(argList[i])
//         break;
//     }
// }
