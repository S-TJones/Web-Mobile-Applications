

// // Driver function
// var driver = function(){
//     console.log('load window');
//     let b1 = document.getElementById("view-all");
//     let b2 = document.getElementById("view-one");

//     b1.addEventListener("click", veiwAllTasks);
//     b2.addEventListener("click", viewSpecificTask);
// }

// // Functions for each route
// function veiwAllTasks() {
//     fetch(`/todo/api/v1.0/tasks`, {
//         headers: {
//             method: 'GET'
//         }
//     })
//     .then(function (response) {
//         return response.json();
//     }).then(function (jsonResponse) {
//         console.log('GET response:', jsonResponse);
//     });
// }

// function viewSpecificTask() {
//     let id = 1;
//     fetch(`/todo/api/v1.0/tasks/${id}`, {
//         headers: {
//             method: 'GET',
//             headers: {
//                 'Accept': 'application/json, text/plain, */*',
//                 //'Content-Type': 'application/json'
//                 "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8" // otherwise $_POST is empty
//             }
//         }
//     })
//     .then(function (response) {
//         return response.json();
//     }).then(function (jsonResponse) {
//         console.log('JSONresponse:', jsonResponse);
//     });
// }

// // Runs this function on startup
// window.onload = driver;