

// Functions for each route
function veiwAllTasks() {
    fetch('/todo/api/v1.0/tasks', {
        headers: {
            method: 'GET'
        }
    })
    .then(function (response) {
        return response.json();
    }).then(function (jsonResponse) {
        console.log('GET response:', jsonResponse);
    });
}