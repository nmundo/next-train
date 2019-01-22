
const showClosestStation = station => {
    document.getElementById('closestStation').innerText = `${station[1]} Station`;
    document.getElementById('closestStationLink').href = window.location.href + station[0];
};

const getClosestStation = (lat, long) => {
    fetch(`http://127.0.0.1:5000/next_train/api/closest_station?lat=${lat}&long=${long}`)
        .then(response => {
            return response.json();
        })
        .then(json => {
            showClosestStation(json);
        });
};


navigator.geolocation.getCurrentPosition(position => {
  getClosestStation(position.coords.latitude, position.coords.longitude);
});
