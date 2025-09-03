
let res = document.getElementById("result")

async function add(){
    const num1 = parseInt(document.getElementById("num1").value)
    const num2 = parseInt(document.getElementById("num2").value)
    const result = await fetch("http://localhost/add", {
        method: 'POST',
        headers: {'Content-Type' : 'application/json'},
        body: JSON.stringify({num1, num2})
    })
    const data = await result.json()
    console.log(data)
    document.getElementById("num1").value = ""
    document.getElementById("num2").value = ""
    res.textContent = data.sum
}