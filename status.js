const form = document.querySelector("#status-form")

form.addEventListener("submit",
    async (event) => {
    event.preventDefault()

    const data = {

        status:
        document.querySelector("#status").
            value,

        location:
        document.querySelector("#location").
            value,

        reason:
        document.querySelector("#reason").
            value,

    };

    const response = await
    fetch("/", {
        method: "POST",
        headers: { "Content-Type":
        "application/json"
    },
        body: JSON.stringify(data)

    });

    const result = await
        response.json()

    document.querySelector("#current-status").textContent =
        result.status;
    document.querySelector("#current-location").textContent=
        result.location;
    document.querySelector("#current-reason").textContent=
        result.reason;
    document.querySelector("#last-updated").textContent=
        result.time;

    console.log(result);

})


