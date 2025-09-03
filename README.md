Perfect 👍 Let’s add a **sample `haproxy.cfg`** snippet to the README so that anyone reading it understands how the load balancing works. Here’s the updated doc:

---

# HAProxy Load Balancer Demo

This project shows how to set up a simple load-balanced application using **Docker Compose** and **HAProxy**.

We have:

* Two backend servers (FastAPI) that handle the logic of adding two numbers.
* A frontend (simple UI with JS) that sends requests to the backend through HAProxy.
* HAProxy, which distributes traffic between the backend servers.

---

## Project Structure

```
.
├── backend/       # FastAPI backend logic
├── frontend/      # Simple frontend (HTML/JS)
├── haproxy.cfg    # HAProxy configuration
├── docker-compose.yml
```

---

## How It Works

1. The **Frontend** (React/HTML+JS) runs on port `3000`.

   * It takes two numbers from the user.
   * Sends them in a POST request to `http://localhost/add`.

2. **HAProxy** listens on port `80`.

   * It forwards requests to one of the backend servers (`backend1` or `backend2`).
   * This way, requests are load-balanced between both backend containers.

3. The **Backends** (FastAPI servers) receive the numbers and return the sum as JSON.

---

## Flow Diagram

![Load Balancer Diagram](A_diagram_in_the_image_illustrates_a_load-balanced.png)

---

## HAProxy Config (`haproxy.cfg`)

Here’s a simple config for round-robin load balancing:

```cfg
global
    log stdout format raw daemon

defaults
    log global
    mode http
    option httplog
    option dontlognull
    timeout connect 5000
    timeout client  50000
    timeout server  50000

frontend http-in
    bind *:80
    default_backend servers

backend servers
    balance roundrobin
    server backend1 backend1:8000 check
    server backend2 backend2:8000 check
```

* `frontend http-in`: listens on port 80 for incoming requests.
* `backend servers`: defines the pool of backend servers.
* `balance roundrobin`: distributes requests evenly across backends.

---

## Backend Logic (FastAPI)

```python
@app.post("/add")
async def add_numbers(numbers: Numbers):
    return {"sum": numbers.num1 + numbers.num2}
```

The backend exposes a single endpoint `/add` that takes two numbers and returns their sum.

---

## Frontend Logic (JS)

```javascript
const num1 = parseInt(document.getElementById("num1").value)
const num2 = parseInt(document.getElementById("num2").value)

const result = await fetch("http://localhost/add", {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ num1, num2 })
})

const data = await result.json()
console.log(data)
```

The frontend grabs user input, sends it to the backend, and logs the result.

---

## Running the Project

1. Clone the repo.
2. Run Docker Compose:

```bash
docker-compose up --build
```

3. Open your browser at:

   * **Frontend:** [http://localhost:3000](http://localhost:3000)
   * **HAProxy (API Gateway):** [http://localhost](http://localhost)

---

## What You’ll See

* Enter two numbers in the frontend UI.
* The request goes to **HAProxy** on port `80`.
* HAProxy forwards the request to either **backend1** or **backend2**.
* Backend calculates the sum and sends it back.

---

## Why Use HAProxy?

* Distributes traffic across multiple backend servers.
* Improves reliability and availability.
* Helps scale services easily.

---

👉 That’s it! You now have a **working load balancer setup** with Docker, HAProxy, FastAPI, and a simple frontend.

---

Got it ✅ Here’s the extra section you can drop at the end of your README for **testing the load balancing**:

---

## Testing Load Balancing

To confirm that HAProxy is actually distributing requests between backends:

1. Start the project with:

   ```bash
   docker-compose up --build
   ```

2. Open the frontend at [http://localhost:3000](http://localhost:3000).

   * Enter two numbers and submit them a few times.
   * Each request will be routed to either `backend1` or `backend2`.

3. To see which backend handled the request, you can:

   * Check the container logs:

     ```bash
     docker logs backend1
     docker logs backend2
     ```

     You’ll notice requests hitting both backends alternately.

   * Or, add a simple print/log statement in the backend (e.g., `print("Request served by backend1")`) to make it obvious.

4. You can also watch HAProxy logs:

   ```bash
   docker logs haproxy
   ```

   This shows the traffic being routed.

By refreshing multiple times or sending multiple requests, you’ll see HAProxy **load balancing traffic between both backend containers**.

---
