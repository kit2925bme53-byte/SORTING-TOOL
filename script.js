async function sortNumbers() {
    const input = document.getElementById("numbers").value;
    const method = document.getElementById("method").value;

    const numbers = input.split(",").map(Number);

    const response = await fetch("http://localhost:8000/sort", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            numbers: numbers,
            method: method
        })
    });

    const data = await response.json();

    document.getElementById("result").innerText = data.result.join(", ");
}