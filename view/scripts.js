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
        }).then(response => response.json());

    if (response.message) {
        alert(response.message);
    }

    else {
        console.log(response)
        //show_app_results(response)
    }

}

//const show_app_results = (response) =>{
var strTable = `<h2 class="text-white">Search Results</h2>
                    <table class="table table-striped">
                        <thead>
                            <th>App Name/th>
                            <th> Name </th>
                            <th> Country </th>
    </thead>
    
    <tbody>`;

//}