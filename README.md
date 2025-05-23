

---

# 🧭 Multi-Objective Route Optimization using QAOA vs Dijkstra

This project demonstrates a quantum-inspired approach to route optimization using **QAOA (Quantum Approximate Optimization Algorithm)** and compares it with the classical **Dijkstra’s algorithm**. It visualizes optimized travel routes on an interactive map and compares execution time vs cost.

---

## 📌 Features

* 🌍 Interactive live map interface for waypoint selection.
* ⚛️ Route optimization using **QAOA**.
* 🧠 Classical baseline with **Dijkstra’s algorithm**.
* 📈 Real-time execution time vs cost graph.
* 🔍 Comparative performance analysis of quantum and classical approaches.

---

## 🛠️ Technologies Used

* **Flask** – Backend web framework (Python)
* **Qiskit** – Quantum optimization library
* **Mapbox** – Map visualization and live data
* **NumPy**, **Docplex**, **Matplotlib** – Scientific computation and modeling
* **HTML/CSS/JS** – Frontend with modal popup and graph/chart UI

---

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/quantum-route-optimizer.git
cd quantum-route-optimizer
```

### 2. Install Required Libraries

```bash
pip install -r requirements.txt
```

> Make sure you also have [Qiskit](https://qiskit.org/) and [Mapbox API Key](https://www.mapbox.com/) if used.

### 3. Run the Flask App

```bash
python app.py
```

### 4. Access the Application

Go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📊 Screenshots

### 🔷 Execution Time vs Cost Chart

![Time vs Cost](screenshots/time-vs-cost.png)

### 🌐 Interactive Map with Optimized Routes

![Map Visualization](screenshots/optimized-map.png)

---

## 📁 Project Structure

```bash
quantum-route-optimizer/
│
├── app.py                  # Flask backend and QAOA logic
├── templates/
│   └── index.html          # Frontend UI
├── static/
│   └── styles.css          # (Optional) Custom styles
├── screenshots/
│   ├── time-vs-cost.png
│   └── optimized-map.png
├── requirements.txt        # Python dependencies
└── README.md
```

---

## ⚖️ Comparison Metrics

| Algorithm  | Optimized for | Avg Execution Time  | Complexity                              |
| ---------- | ------------- | ------------------- | --------------------------------------- |
| QAOA       | Cost/Distance | Lower (Quantum Sim) | Lower on large inputs (NP-Hard support) |
| Dijkstra's | Distance Only | Higher              | Polynomial but higher overhead          |

---

## 🧪 Sample Output

* Optimized Route: JSON of best path
* Execution Time: Array showing step-wise execution time
* Interactive graph: Displays execution time vs cost

---

## 📌 Future Enhancements

* Integrate **live traffic** data.
* Use **IBM Q** or **D-Wave** backend for true quantum execution.
* Add **multi-vehicle** routing and **delivery-time** constraints.

---

## 🙌 Acknowledgments

* [Qiskit by IBM](https://qiskit.org/)
* [Mapbox](https://www.mapbox.com/)
* [Docplex Optimization](https://ibmdecisionoptimization.github.io/docplex-doc/)

---

