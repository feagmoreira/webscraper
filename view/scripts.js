get_app = async () => {
    let aptoide_url = document.getElementById('url').value;

    // Validating if input is not empty
    if (aptoide_url == '') {
        alert('Url information is missing');
        return;
    }
    let url = `http://localhost:8000/aptoideapp/?url=${aptoide_url}`

    let response = await fetch(url,
        {
            method: "GET",
            headers: {
                Accept: "application/json",
                "Content-Type": "application/json",
            }
        })
    if (response.status == 200) {
        let app = await response.json()
        show_app_results(app)
        return
    }
    else {
        let status = response.status
        let statusText = response.statusText
        let message = await response.json()
        alert(`Http Code: ${status} - ${statusText}.\nScraper Error: ${message.error}`);
        return
    }

}

const show_app_results = (app) => {
    let card = `<div class="card">
                    <div class="card-body">
                        <h5 class="card-title">${app.name}</h5>
                        <p class="card-text"><strong>Description</strong></p>
                        <p class="card-text">${app.description}</p>
                        </div>
                        <ul class="list-group list-group-flush">
                        <li class="list-group-item"><strong>Downloads: </strong>${app.downloads}</li>
                        <li class="list-group-item"><strong>Version: </strong>${app.version}</li>
                        <li class="list-group-item"><strong>Release Date: </strong>${app.release_date}</li>
                        </ul>
                    </div>`
    document.getElementById("placeHolder").innerHTML = card;
}