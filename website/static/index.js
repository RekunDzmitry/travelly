function deleteTravel(id) {
    // send delete request to server
    fetch("/delete-travel", {
        method: 'POST',
        body: JSON.stringify({ travelId: id })
    }).then((_res) => {
        window.location.href = '/';
    })
}